import sys
import youtube_dl


class MyLogger():
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d["status"] == "finished":
        print("\nConverting file...")
    elif d["status"] == "downloading":
        status = (d["downloaded_bytes"] / d["total_bytes"]) * 100
        sys.stdout.write(f"\r{status}%")
        sys.stdout.flush()


ydl_opts = {
    "format": "bestvideo+bestaudio",
    "logger": MyLogger(),
    "progress_hooks": [my_hook],
    "noplaylist": True,
}

print("Type YouTube url:")
inputs = []
url = input()
if url:
    while (url):
        inputs.append(url)
        url = input()
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(inputs)
