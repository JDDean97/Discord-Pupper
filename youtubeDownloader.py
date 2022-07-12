from pytube import YouTube

async def main(url):
    link = url
    yt = YouTube(link)
    print("Title: ", yt.title)
    print("Views: ",yt.views)
    print("Video Length: ",yt.length," seconds")
    print("Description: ",yt.description)
    print(yt.streams.filter(only_audio=True))
    ys = yt.streams.filter(only_audio=True)[0]
    ys.download()

async def getInfo(url):
    link = url
    yt = YouTube(link)
    return yt.title