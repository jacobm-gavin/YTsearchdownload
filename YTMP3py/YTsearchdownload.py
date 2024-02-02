from pytube import YouTube
from youtubesearchpython import VideosSearch
import os
import sys 
from time import sleep
from json import loads
from requests import get

downloadTo="/Volumes/DJG/NEW"

ffmpegLocation="/Users/jgavin/Documents/ffmpeg"

"""
class YTcursor:
    def __init__(self, ffmpegLocation, downloadLocation, fixRate = True) -> None:
        assert(os.path.exists(downloadLocation))
        self.ffmpegLocation = ffmpegLocation
        self.downloadLocation = downloadLocation
        self.fixRate = fixRate

    def searchYoutube(self, query: str, maxresults: int, autodownload: bool = False) -> str:
        ##TODO finish autodownload implementation
        videos = VideosSearch(query)
        for i in range(maxresults):
            print(f"[{i}] - [{videos.result()['result'][i]['duration']}] " + videos.result()['result'][i]['title'])
        toDownload = int(input("Enter a download index:  "))
        try:
            downloadLink = videos.result()['result'][toDownload]['link']
            return downloadLink
        except:
            print("ERROR [1] while downloading video")

    def downloadVideo(self, link: str, downloadtype: str) -> str:
        yt = YouTube(link)
        if downloadtype == "video":
            video = yt.streams.filter().first()
        elif downloadtype == "audio":
            video = yt.streams.filter(only_audio=True).first()
        else:
            raise Exception

        outfile = video.download(output_path=self.downloadLocation)
        base, ext = os.path.splitext(outfile)
        new_file = base + '.mp3'
        os.rename(outfile, new_file)

        return "/".join([self.downloadLocation, new_file])

    def changebitrate(self, filepath: str, bitrate: str) -> None:
        print("repairing audio")
        bitFixedPath = "/".join(filepath.split("/")[:-1]) + "/[240k] "
        bitFixedName = filepath.split("/")[-1]
        ffmpeg_command = f"{self.ffmpegLocation} -i '{filepath}' -b:a {bitrate} '{bitFixedPath}{bitFixedName}' -loglevel panic"
        os.system(ffmpeg_command)
        os.remove(filepath)


    def mainloop(self):
        
        downloadType = -1
        while downloadType != "A" and downloadType != "V":
            downloadType = input(" (A)udio or (V)ideo download?")
        match downloadType:
            case "A":
                downloadType = "audio"
            case "V":
                downloadType = "video"
        while True:
            query = input("Enter a search term: ")
            maxResults = int(input("# of results to display?"))
            downloadLink = self.searchYoutube(query, maxResults)
            
            
"""
fixRate = True #Fix bitrate, needed to use in SERATO DJ



while True:
    try:
        print("Enter Search Term: ",end="")
        searchTerm = input()
        print("\n"*100)
        videos = VideosSearch(searchTerm, limit = 5)
        for i in range(5):
            print(f"[{i}] - [{videos.result()['result'][i]['duration']}] "+videos.result()['result'][i]['title'])
        toDownload = int(input("Enter A download Index: "))
        try:
            downloadLink = videos.result()['result'][toDownload]['link']
        except:
            print("Aborting...")
            
            continue
        yt = YouTube(downloadLink)
        video = yt.streams.filter(only_audio=True).first()

        destination = "/Users/jgavin/Desktop/DJG Backup"            ##CHANGE THIS LOCATION FOR PARTIES
        if os.path.exists(downloadTo):
            destination = downloadTo
        ## TODO fix destination setting
        print("[0] downloading...")
        outfile = video.download(output_path=destination)
        base, ext = os.path.splitext(outfile)
        new_file = base + '.mp3'
        os.rename(outfile, new_file)
        if fixRate:
            print("repairing audio")
            for i in range(100):
                print(f"[{i}%]     ", end="\r")
                sleep(0.01)
            print("Cleaning up")
            bitFixedPath = "/".join(new_file.split("/")[:-1]) + "/[240k] "
            bitFixedName = new_file.split("/")[-1]
            command = f"/Users/jgavin/Documents/ffmpeg -i '{new_file}' -b:a 240k '{bitFixedPath}{bitFixedName}' -loglevel panic"
            os.system(command)
            os.system(f"rm '{new_file}'")
            

    except Exception as e:
        print(f"[1] Exception occurred. Enter to continue")
        print(e)
        input()
        continue
    print("\n"*100)
    print(destination)
    print(f"[0] {yt.title} DOWNLOADED")
    #print("\n"*100)

print('[0] Process finished')