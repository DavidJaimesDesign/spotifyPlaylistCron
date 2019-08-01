# SpotifyPlaylistCron
I have been manually saving Spotify's discover weekly into their own seperate playlists for a while now. I got tired of that,
so I created this script that does that for me. I have it setup on a raspberrry pi and runs as a cron job. Setup information is bellow.
c. Python 3 only

## Dependcies
You must pip install 'spotipy' to use this script http://spotipy.readthedocs.io/en/latest/

## Spotify API
1. Register your application with Spotify to get the neccessary api clients and secrets
2. Add those values as environment variables on the machine you want to run it as
3. Add the redirect domain `http://locahost:8080` to your valid redirect domains on your application

## Setup
1. Add the following environment variables to your .bashrc file or other corresponding file
```
export SPOTIFY_CLIENT_ID=$YOUR_CLIENT_ID
export SPOTIFY_CLIENT_SECRET=$YOUR_CLIENT_SECRET
export SPOTIFY_PLAYLIST_ID=$YOUR_DISCOVER_WEEKLY_ID
export SPOTIFY_USERNAME=$YOUR_SPOTIFY_USERNAME
```

2. Run the script `python script.py`
3. The script will open a browser with an authentication window
4. Go through the flow and enter your credentials this will rederict you to a localhost address
5. Copy that address and paste it into your terminal
6. Your application shown be authorized now

## Server support
Now with server support be sure to install the required values
```
pip install flask flask-jsonpify flask-sqlalchemy flask-restful
```
Then run the application with python server.py

I have my server running in the background on a raspberry pi that runs a cron job that curls the create playlist every monday
