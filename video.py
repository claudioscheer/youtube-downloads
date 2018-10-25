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
        status = (d["downloaded_bytes"] / d["total_bytes"]) * 100
        print(f"{round(status, 2)}%")


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
