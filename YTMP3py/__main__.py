import YTsearchdownload
cursor = YTsearchdownload.YTcursor("/Users/jgavin/Documents/ffmpeg", "/Users/jgavin/Desktop/YTMP3py/songs")
link = cursor.searchYoutube("deez nuts", 5)
cursor.downloadVideo(link, "audio")
print(cursor.downloadLocation)
"""
downloadTo="/Volumes/DJG/MISC"
ffmpegLocation="/Users/jgavin/Documents/ffmpeg"
"""
