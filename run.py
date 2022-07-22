import os 

from spotify_client import SpotifyClient
from youtube_client import YoutubeClient

def run(): 
    #get list of playlists from youtube 
    youtube_client = YoutubeClient('./creds/client)secret.json')
    spotify_client = SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'))
    playlists = youtube_client.get_playlists()

    #ask which playlist we want to get music videos from 
    for index, playlist in enumerate(playlists):
        print(f"{index}: {playlist.title}")

    choice = int(input("Enter your choice: "))
    chosen_playlist = playlists[choice]
    print(f"You selected: {chosen_playlist.title}")

    #for each video in playlist get the song info from youtube 
    songs = youtube_client.get_videos_from_playlist(chosen_playlist.id)
    print(f"Attempting to add {len(songs)}")

    #search for songs on spotify 
    for song in songs:
        spotify_song_id = spotify_client.search_song(song.artist, song.track)
        if spotify_song_id:
            added_song = spotify_client.add_song_to_spotify(spotify_song_id)
            if added_song:
                print(f"Added {song.artist}")


if __name__ == '__main__':
    run()