import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print msg

def my_hook(d):
    if d["status"] == "finished":
        print "Converting file..."
    elif d["status"] == "downloading":
        print "%s of %s..." % (d["_percent_str"], d["_total_bytes_str"])

ydl_opts = {
    "format": "bestaudio/best",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "256",
    }],
    "logger": MyLogger(),
    "progress_hooks": [my_hook],
}

print "Type YouTube url:"
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([raw_input()])
