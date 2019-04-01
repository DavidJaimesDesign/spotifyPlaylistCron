import datetime
import spotipy
import spotipy.util as util
import os

scope = "user-library-read playlist-modify-public playlist-modify-private"
spotify_client_id = os.environ['SPOTIFY_CLIENT_ID']
spotify_client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
playlistID = os.environ['SPOTIFY_PLAYLIST_ID']
username = os.environ['SPOTIFY_USERNAME']


def get_tracks_in_discover_weekly(sp):
    rawpl = sp.user_playlist('spotify', playlistID)['tracks']
    track_ids = []
    for i, item in enumerate(rawpl['items']):
        track_ids.append(item['track']['id'])

    return track_ids


def create_empty_playlist(sp):
    sp.trace = False
    now = datetime.datetime.now()
    name = "DW-" + str(now.year) + "-" + str(now.month) + "-" + str(now.day)
    sp.user_playlist_create(username, name, True)

    # Since the method does not return anything have to search for the playlist ID

    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['name'] == name:
            return playlist['id']

def main():
    token = util.prompt_for_user_token(username, scope, client_id=spotify_client_id,client_secret=spotify_client_secret,
                                       redirect_uri='http://localhost:8080')
    sp = spotipy.Spotify(auth=token)
    tracks_to_add = get_tracks_in_discover_weekly(sp)
    new_playlist = create_empty_playlist(sp)
    sp.user_playlist_add_tracks(username,new_playlist,tracks_to_add)

if __name__ == '__main__':
    main()
