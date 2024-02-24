# Hello there!
This is just a simple CLI based YouTube downloader using PyTube v15. It's more for my personal use, but I don't mind sharing it and developing it for myself as others to use. It's going to be built by me and maintained in my free time. Hope you find it useful! The default download path is `%userprofile%/Downloads` or `C:\Users\<AccName\Downloads`

# Why did I decide to build this instead of using one of the many websites currently out there?
The answer is simple! I am bored with trying to find the least sketchy YouTube video downloader to use which won't compromise my system with broken/corrupted files that could cause harm in some way, shape or form! 

# Checklist of features I am intending on including later on in the releases:
- [] Caption downloading (inc audio/video file with it) - if able to via PyTube
- [] Custom download path output
- [] Graphical User Interface
- [] Windows executable package (for ease of use for non-developers and/or people who don't want to mess with Python install.)

# I don't want to wait for the EXE release! How do I run it now?
Well, simple answer is to download python from [here](https://www.python.org/downloads/release/python-3122/) and during install, add it to PATH. *Please note that I recommend you install the Recommended package for your operating system for best experience*. Once you have done so, navigate to the unzip location of this program and run `pip install -r requirements.txt` to install all the dependencies. After that, I have personally just made a batch file with the following to run it:
```
@echo off
"python3 -m "<path to extract>\src\script.py"
```

## Batch breakdown: 
Basically, `python3` tells Windows you are wanting to run the rest with Python. You need to use the path of the extraction where I put `path to extract` aka the folder you put it in. The `@echo off` is not needed but helps clean up the terminal and remove the windows information at the top for the cleaner interface. 
#