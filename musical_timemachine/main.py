from user_actions import UserActions
from web_scrapper import WebScrapper
from spotify_playlist import SpotifyPlaylist

user_input = UserActions()
user_date = user_input.take_user_input()

web_scrap = WebScrapper()
# Generate music titles for the user date
music_titles = web_scrap.scrap_website(user_input.user_date_choice)

sp_playlist = SpotifyPlaylist()
# Generate user_id for whom playlist is to be created
user_id = sp_playlist.get_authenticated_user()

# Generate track URI's
sp_playlist.generate_spotify_uri(music_titles, user_date)

# Generate spotify playlist and add tracks
sp_playlist.generate_playlist(user_id, web_scrap.playlist_title,user_date)


