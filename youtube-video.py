#!/usr/bin/env python3
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
        print("Converting file...")
    elif d["status"] == "downloading":
        sys.stdout.write("\r%s of %s..." % (d["_percent_str"], d["_total_bytes_str"]))
        sys.stdout.flush()

ydl_opts = {
    "format": "bestvideo+bestaudio",
    "logger": MyLogger(),
    "progress_hooks": [my_hook],
    "noplaylist" : True,
}

print("Type YouTube url:")
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([input()])