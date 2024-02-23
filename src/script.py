import os

from pytube import YouTube
from pytube.cli import on_progress
from pytube.helpers import safe_filename
from datetime import timedelta


def mainRun():
    while True:
        option = input(str("Video or Audio?\n>> ")).lower()

        if option == 'video':
            VidDownload()

        if option == 'audio':
            AudDownload()


def prettify_numb(number: str) -> str:
    token_list = list(str(number))
    formatted = []

    count = 0

    for index in range(len(token_list)-1, -1, -1):
        token = token_list[index]

        formatted.append(token)

        count += 1

        if count == 3 and index != 0:
            formatted.append(",")
            count = 0

    formatted.reverse()

    return "".join(formatted)


def VidDownload():
        link = input(str("Enter the link for the youtube video you want to download:\n>> "))

        if link == "exit":
            return print("\033[31mYou have exited the program. Have a great day!")

        yt = YouTube(link, use_oauth=True, on_progress_callback=on_progress)
        ys = yt.streams

        os.chdir(os.path.join(os.environ['USERPROFILE'], 'Downloads'))
        os.listdir()

        if 'YT Downloads' in os.listdir():
            op = './YT Downloads/'

        else:
            os.mkdir('YT Downloads')
            op = './YT Downloads/'

        if yt.length > 360:
            return print("\033[31mThis file is over the limit of 6 minutes.\033[37m")

        info = f'{safe_filename(yt.author + " - " + yt.title)}.mp4'

        if info in op:
            return print("This video is already in the folder. Please choose another.")

        views = prettify_numb(f"{yt.views}")
        dur = timedelta(seconds=yt.length)

        print("\n\033[32mSuccessful! Found the video. Commencing download.")
        print("\033[37mTitle: ", yt.title)
        print("Uploader: ", yt.author)
        print("Number of views: ", views)
        print("Length of video: ", dur)

        download = ys.get_highest_resolution()
        download.download(output_path=op, filename=f"{info}", max_retries=3)

        print(f"\033[32m→Successful!")
        print(f"\033[37m     ↪Saved in Downloads: {op}{info}")
        print(f"     File Size: {download.filesize_kb}kb || {download.filesize_mb}mb")
        print("-"*40 + "\n")


def AudDownload():
        link = input(str("Enter the link for the youtube video audio you want to download:\n>> "))

        if link == "exit":
            return print("\033[31mYou have exited the program. Have a great day!")

        yt = YouTube(link, use_oauth=True, on_progress_callback=on_progress)
        ys = yt.streams.filter(only_audio=True).first()

        os.chdir(os.path.join(os.environ['USERPROFILE'], 'Downloads'))
        os.listdir()

        if 'YT Downloads' in os.listdir():
            op = './YT Downloads/'

        else:
            os.mkdir('YT Downloads')
            op = './YT Downloads/'

        if yt.length > 360:
            return print("\033[31mThis file is over the limit of 6 minutes.")

        info = f'{safe_filename(yt.author + " - " + yt.title)}.mp3'

        if info in op:
            return print("This video is already in the folder. Please choose another.")

        views = prettify_numb(f"{yt.views}")
        dur = timedelta(seconds=yt.length)

        print("\n\033[32mSuccessful! Found the video. Commencing download.")
        print("\033[37mTitle: ", yt.title)
        print("Uploader: ", yt.author)
        print("Number of views: ", views)
        print("Length of video: ", dur)

        # download = ys.get_highest_resolution()
        ys.download(output_path=op, filename=f"{info}", max_retries=3)

        print(f"\033[32m→Successful!")
        print(f"\033[37m     ↪Saved in Downloads: {op}{info}")
        print(f"     File Size: {ys.filesize_kb}kb || {ys.filesize_mb}mb")
        print("-"*40 + "\n")


if __name__ in '__main__':
    mainRun()
