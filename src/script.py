import os
import ctypes

from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix.helpers import safe_filename
from datetime import timedelta
from enum import Enum


os.chdir(os.path.join(os.environ['USERPROFILE'], 'Downloads'))
ctypes.windll.kernel32.SetConsoleTitleW("YouTube Downloader")

if not os.path.exists("YT Downloads"):
    os.mkdir("YT Downloads")

OP: str = "YT Downloads"


green = "\n\033[32m"
red = "\033[31m"
white = "\033[37m"


class ReturnCodes(Enum):
    OK = 0
    Back = 1
    UserQuit = 2


def codes(value: str):
    if value == "quit":
        return ReturnCodes.UserQuit
    if value == "back":
        return ReturnCodes.Back

    return ReturnCodes.OK


def mainRun():
    while True:
        option = input("Video or Audio?\n>> ").lower()

        if option == 'video':
            ret = VidDownload()

        if option == 'audio':
            ret = AudDownload()

        if option == 'caption':
            ret = CapDownload()

        if ret is ReturnCodes.UserQuit:
            print(f"{red}You have exited the program. Have a great day!{white}")
            break


def prettify_numb(number: str) -> str:
    token_list = list(str(number))
    formatted = []

    count = 0

    for index in range(len(token_list) - 1, -1, -1):
        token = token_list[index]

        formatted.append(token)

        count += 1

        if count == 3 and index != 0:
            formatted.append(",")
            count = 0

    formatted.reverse()

    return "".join(formatted)


def VidDownload():
    link = input("Enter the link for the youtube video you want to download:\n>> ")

    if link == "exit":
        return ReturnCodes.UserQuit

    if link == "back":
        return ReturnCodes.Back

    yt = YouTube(link, use_oauth=False, allow_oauth_cache=True, on_progress_callback=on_progress)
    ys = yt.streams

    '''if "vevo" in yt.author.lower():
        auth = yt.author.sp'''

    if yt.author in yt.title:
        info = f'{safe_filename(yt.title)}.mp4'
    else:
        info = f'{safe_filename(yt.author + " - " + yt.title)}.mp4'

    if info in OP:
        return print("This video is already in the folder. Please choose another.")

    views = prettify_numb(f"{yt.views}")
    dur = timedelta(seconds=yt.length)

    print(f"{green}Successful! Found the video. Commencing download.")
    print(f"{white}Title           : ", yt.title)
    print("Uploader        : ", yt.author)
    print("Number of views : ", views)
    print("Length of video : ", dur)

    download = ys.get_highest_resolution()
    download.download(output_path=OP, filename=f"{info}", max_retries=3)

    if download.filesize_mb > 1024:
        size = f"{round(download.filesize_gb, 2)}gb"
    else:
        size = f"{round(download.filesize_mb, 2)}mb"

    print(f"{green}→Successful!")
    print(f"{white}     ↪ Saved in {os.environ['USERPROFILE']}\\Downloads\\{OP}\\{info}")
    print(f"     File Size: {download.filesize_kb}kb || {size}")
    print("-" * 40 + "\n")


def AudDownload():
    link = input("Enter the link for the youtube video audio you want to download:\n>> ")

    if link == "exit":
        return ReturnCodes.UserQuit

    if link == "back":
        return ReturnCodes.Back

    yt = YouTube(link, use_oauth=False, on_progress_callback=on_progress)
    ys = yt.streams.filter(only_audio=True).first()

    if yt.author in yt.title:
        info = f'{safe_filename(yt.title)}.mp3'
    else:
        info = f'{safe_filename(yt.author + " - " + yt.title)}.mp3'

    if info in OP:
        return print("This video is already in the folder. Please choose another.")

    views = prettify_numb(f"{yt.views}")
    dur = timedelta(seconds=yt.length)

    print(f"{green}Successful! Found the video. Commencing download.")
    print(f"{white}Title           : ", yt.title)
    print("Uploader        : ", yt.author)
    print("Number of views : ", views)
    print("Length of audio : ", dur)

    ys.download(output_path=OP, filename=f"{info}", max_retries=3)

    if ys.filesize_mb > 1024:
        size = f"{round(ys.filesize_gb, 2)}gb"
    else:
        size = f"{round(ys.filesize_mb, 2)}mb"

    print(f"{green}→Successful!")
    print(f"{white}     ↪ Saved in {os.environ['USERPROFILE']}\\Downloads\\{OP}\\{info}")
    print(f"     File Size: {ys.filesize_kb}kb || {size}")
    print("-" * 40 + "\n")


def CapDownload():
    link = input("Enter the link for the youtube video captions you want to download:\n>> ")

    if link == "exit":
        return ReturnCodes.UserQuit

    if link == "back":
        return ReturnCodes.Back

    yt = YouTube(link, use_oauth=False, on_progress_callback=on_progress)

    langCode = input(f"Enter the language code you wish to have out of:\n{yt.captions}\n>> ")

    info = f'{safe_filename(yt.author + " - " + yt.title)}.srt'

    if info in OP:
        return print("This video is already in the folder. Please choose another.")

    print(f"{green}Successful! Found the video captions. Commencing download.")
    print(f"{white}Title           : ", yt.title)
    print("Uploader        : ", yt.author)

    caption = yt.captions.get_by_language_code(lang_code=langCode)
    caption.generate_srt_captions()
    print(caption)
    caption.download(title=yt.title, output_path=OP)

    print(f"{green}→Successful!")
    print(f"{white}     ↪Saved in {os.environ['USERPROFILE']}\\Downloads\\{OP}\\{info}")
    # print(f"     File Size: {download.filesize_kb}kb || {download.filesize_mb}mb")
    print("-" * 40 + "\n")


if __name__ in '__main__':
    mainRun()
