# Text2CWaudio
Converts a text file into CW and saves as an mp3 file for playback.


There are a couple of dependancies that can be resolved following the steps below.

Step 1: Verify ffmpeg Installation
Make sure ffmpeg is installed correctly on your system.

macOS

Install Homebrew (if not already installed):
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Install FFmpeg using Homebrew:
brew install ffmpeg


Windows

Download FFmpeg:
Go to the FFmpeg download page.
Select the build appropriate for your system (e.g., Windows builds from gyan.dev).
Extract and Set PATH:
Extract the downloaded FFmpeg zip file.
Add the bin directory to your system's PATH environment variable:
Right-click on 'This PC' or 'Computer' on the desktop or in File Explorer, and select 'Properties'.
Click on 'Advanced system settings'.
Click the 'Environment Variables' button.
In the 'System variables' section, find the 'Path' variable and click 'Edit'.
Add the path to the bin directory of the extracted FFmpeg folder.


Linux

Install FFmpeg using the package manager:

sudo apt update
sudo apt install ffmpeg

Step 2: Verify ffmpeg Path
Ensure that ffmpeg is correctly installed and the path is set. Run the following command in your terminal or command prompt:
ffmpeg -version

This should display the version information of ffmpeg. If it doesn't, it means the ffmpeg executable is not in your system's PATH.



Instructions for use:

1. Open terminal, type this and modify the path to the file: python3 /PATH/TO/text2CW.py
2. Press return or enter
3. Select file to convert (pdf only at the moment)
4. Set word per minute speed.
5. Set Farnsworth speed(optional, leave set to 0 to disable)
6. set tone frequency
7. Click convert button, name file, choose location and click save.
8. Please be patient while your mp3 is created


Future revisions will see the ability to:

1. open differnt file types
2. save as different audio file types
coming soon in next update, open .wav audio files for converting to
cw
