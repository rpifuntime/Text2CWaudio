import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pydub import AudioSegment
from pydub.generators import Sine
import PyPDF2

# Specify the path to ffmpeg if needed
AudioSegment.converter = "/usr/local/bin/ffmpeg"  # Update this path according to your system


# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '!': '-.-.--', '@': '.--.-.',
    ' ': ' '
}

# Function to extract text from a PDF file
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text

# Function to convert text to Morse code
def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
    return morse_code

# Function to generate Morse code audio
def morse_to_audio(morse_code, output_file, wpm, farnsworth_wpm, tone_freq):
    dot_duration = 1200 / wpm  # milliseconds (one dot is 1.2 seconds divided by WPM)
    dash_duration = 3 * dot_duration
    intra_char_space = dot_duration
    char_space = 3 * dot_duration
    word_space = 7 * dot_duration

    # If Farnsworth speed is used, adjust the character and word spacing
    if farnsworth_wpm > 0:
        farnsworth_dot_duration = 1200 / farnsworth_wpm
        char_space = 3 * farnsworth_dot_duration
        word_space = 7 * farnsworth_dot_duration

    audio = AudioSegment.silent(duration=0)  # Start with an empty audio segment

    for symbol in morse_code:
        if symbol == '.':
            audio += Sine(tone_freq).to_audio_segment(duration=dot_duration) + AudioSegment.silent(duration=intra_char_space)
        elif symbol == '-':
            audio += Sine(tone_freq).to_audio_segment(duration=dash_duration) + AudioSegment.silent(duration=intra_char_space)
        elif symbol == ' ':
            audio += AudioSegment.silent(duration=char_space)
        elif symbol == '/':
            audio += AudioSegment.silent(duration=word_space)

    audio.export(output_file, format="mp3")

# Main function to process the file and generate the Morse code audio
def process_file(input_file, output_file, wpm, farnsworth_wpm, tone_freq):
    if input_file.lower().endswith('.pdf'):
        text = extract_text_from_pdf(input_file)
    elif input_file.lower().endswith('.txt'):
        with open(input_file, 'r') as file:
            text = file.read()
    else:
        raise ValueError("Unsupported file format")

    morse_code = text_to_morse(text)
    morse_to_audio(morse_code, output_file, wpm, farnsworth_wpm, tone_freq)

# GUI Application
class MorseCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Morse Code Audio Converter")

        self.label = tk.Label(root, text="Select a text or PDF file:")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select File", command=self.select_file)
        self.select_button.pack(pady=5)

        self.speed_label = tk.Label(root, text="Set speed (words per minute):")
        self.speed_label.pack(pady=10)

        self.speed_var = tk.IntVar(value=20)
        self.speed_entry = tk.Entry(root, textvariable=self.speed_var)
        self.speed_entry.pack(pady=5)

        self.farnsworth_label = tk.Label(root, text="Set Farnsworth speed (words per minute, 0 to disable):")
        self.farnsworth_label.pack(pady=10)

        self.farnsworth_var = tk.IntVar(value=0)
        self.farnsworth_entry = tk.Entry(root, textvariable=self.farnsworth_var)
        self.farnsworth_entry.pack(pady=5)

        self.tone_label = tk.Label(root, text="Set tone frequency (Hz):")
        self.tone_label.pack(pady=10)

        self.tone_var = tk.IntVar(value=700)
        self.tone_entry = tk.Entry(root, textvariable=self.tone_var)
        self.tone_entry.pack(pady=5)

        self.convert_button = tk.Button(root, text="Convert to Morse Code Audio", command=self.convert_to_morse_audio)
        self.convert_button.pack(pady=20)

        self.file_path = ''

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("PDF files", "*.pdf")])
        if self.file_path:
            self.label.config(text=os.path.basename(self.file_path))

    def convert_to_morse_audio(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select a file first")
            return

        wpm = self.speed_var.get()
        farnsworth_wpm = self.farnsworth_var.get()
        tone_freq = self.tone_var.get()
        if wpm <= 0:
            messagebox.showerror("Error", "Words per minute must be greater than 0")
            return

        output_file = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if not output_file:
            return

        try:
            process_file(self.file_path, output_file, wpm, farnsworth_wpm, tone_freq)
            messagebox.showinfo("Success", "Morse code audio file created successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = MorseCodeApp(root)
    root.mainloop()
