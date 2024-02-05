import YTsearchdownload
import os
os.chdir(os.path.dirname(__file__))
with open("settings.txt", 'r') as file:
    fixBitRate: bool =      file.readline().split(':')[1].strip() == '1'
    downloadLocation: str = file.readline().split(':')[1].strip()
    ffmpegPath: str =       file.readline().split(':')[1].strip()


args = {
    "fixBitRate": fixBitRate,
    "downloadLocation": downloadLocation,
    "ffmpegPath": ffmpegPath
}

YTsearchdownload.mainLoop(args)