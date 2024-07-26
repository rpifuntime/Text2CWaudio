# Text2CWaudio
Converts a text file into CW and saves as an mp3


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

