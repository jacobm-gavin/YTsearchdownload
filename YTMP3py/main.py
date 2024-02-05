from pytube import YouTube
from youtubesearchpython import VideosSearch
import os
import sys 
from time import sleep
#from sclib import SoundcloudAPI, Track, Playlist
from json import loads
from requests import get

guest_client_id = 'b45b1aa10f1ac2941910a7f0d10f8e28'

"""
def soundCloudSearch(query):
    global guest_client_id
    search_url = 'https://api.soundcloud.com/search?q=%s&facet=model&limit=10&offset=0&linked_partitioning=1&client_id='+guest_client_id
    url = search_url % query
    while url:
        response=get(url)
        if response.status_code!= 200:
            return
        try:
            doc = loads(response.text)
        except:
            return
        for entity in doc['collection'][:5]:
            if entity['kind'] == 'track':
                print( entity['permalink_url'])
        url = doc.get('next_href')

"""

def mainLoop(args) -> None:

    if sys.argv[-1] == "-b":
        fixRate = True
    while True:
        try:
            print("Enter Search Term: ",end="")
            searchTerm = input()
            """
            if searchTerm[:2] == '-s':
                ##SEARCH IN SOUNDCLOUD
                print("CLOUD SEARCH")
                print(soundCloudSearch(searchTerm[2:]))
            """




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

            destination = "/Users/jgavin/Desktop/DJG Backup"
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

        print(f"[0] {yt.title} DOWNLOADED")
        #print("\n"*100)
