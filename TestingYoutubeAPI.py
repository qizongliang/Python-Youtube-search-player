from youtubesearchpython import SearchVideos
import pafy
import vlc
import json
import time

instance = vlc.Instance('--input-repeat=-1') # always keep playing
player = instance.media_list_player_new() #new player


media_list = instance.media_list_new() #new media list

search = SearchVideos("netnobody song", offset = 1, mode = "json", max_results = 20) #search up youtube and every music found
#[NCS Release]

json_file= json.loads(search.result()) # load string into JSON and convert it to dictionary


for i in json_file["search_result"]: # in every search result
    url = pafy.new(i["link"]) # pass int the link and convert every video to a media
    audiostreams = url.audiostreams
    media = instance.media_new(url.getbestaudio().url)
    media_list.add_media(media) # add media to a list
    print("Loaded: " + i["title"])

    



player.set_media_list(media_list)
player.play() #play medialist

input("Enter to exit")
