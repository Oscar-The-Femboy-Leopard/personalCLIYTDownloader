# Hello there!
This is just a simple CLI based YouTube downloader using Python. It's more for my personal use, but I don't mind sharing
it and developing it for myself as others to use. It's going to be built by me and maintained in my free time. Hope you
find it useful! The default download path is `%userprofile%/Downloads` or `C:\Users\<AccName>\Downloads` and it will
make its own folder there called `YT Downloads` (or the custom location if no folder exists - once I get that
integrated). The playlist downloads have a custom folder inside `YT Downloads` called `Playlist Download` to separate it
for viewing ease. 

# Why did I decide to build this instead of using one of the many websites currently out there?
The answer is simple! I am bored with trying to find the least sketchy YouTube video downloader to use which won't
compromise my system with broken/corrupted files that could cause harm in some way, shape or form! It also provides me
a project to enjoy and show.

# The Windows Executable is now live with this update!
The update is nothing too much, just some refactors to make it work better in the executable format as well as prettify
the UI. Just download the zip from the [releases page](https://github.com/SpiritingAuto04/personalCLIYTDownloader/releases/new)
and extract! You then just need to run the executable, and it will bring up its interface! ***HOWEVER***, due to how
Python projects are packed into Windows Executable files (exe), Microsoft Defender may quarantine and attempt to remove
the software. It is a common issue, especially with Python being such a useful and powerful language and being made for
viruses. 

# I care too much about my PC to run a random executable!
I fully agree. Packed executables aren't always the safest thing to run on your system hence why I have already run it
through [virustotal](https://www.virustotal.com/gui/file/54547c3cf13a77c6dc6d7cd0a27adfb8c02e76c77ce421bbab9f5d970d1be59f?nocache=1),
but this specific set of false positives also a common issue known with python applications and even dealt with on
[PyInstaller's GitHub](https://github.com/pyinstaller/pyinstaller/issues?q=is%3Aissue+virus+is%3Aclosed). If you are
truly worried about the risks but still wish to use the project, you can always do the manual python install below. 

# Checklist of features I am intending on including later on in the releases:
- [] Caption downloading (inc audio/video file with it) - if captions are available. 
- [] Custom download path output
- [✓] ~~Playlist Downloading~~
- [] Downloading from Search
- [] Graphical User Interface
- [] Logging System
- [✓] ~~Windows executable package (for ease of use for non-developers and/or people who don't want to mess with Python install.)~~

# I don't want to wait for the EXE release! How do I run it now?
Well, simple answer is to download python from [here](https://www.python.org/downloads/release/python-3122/) and during
install, add it to PATH. *Please note that I recommend you install the Recommended package for your operating system for
best experience*. Once you have done so, navigate to the unzip location of this program and run
`pip install -r requirements.txt` to install all the dependencies. After that, I have personally just made a batch file
with the following to run it:
```bash
@echo off
python3 -m "<path to extract>\src\script.py"
```

If that bash doesn't work due to an error mentioning not having Python installed, or it's not found, try the following:
```bash
@echo off
py -3 -m "<path to extract>\src\script.py"
```

## Batch breakdown: 
Basically, `python3` tells Windows you are wanting to run the rest with Python. You need to use the path of the
extraction where I put `path to extract` aka the folder you put it in. The `@echo off` is not needed but helps clean up
the terminal and remove the windows information at the top for the cleaner interface. 
#