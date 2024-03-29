import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


class SpotifyPlaylist:

    def __init__(self):
        self.CLIENT_ID = os.environ.get("CLIENT_ID")
        self.CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
        self.REDIRECT_URI = os.environ.get("REDIRECT_URI")
        self.scope = "playlist-modify-private"
        self.token = ""
        self.spotify_object = self.generate_spotify_object()
        self.spotify_uri = []

    def get_oauth_object(self):
        """Connects to spotify using client id/secret and get an oAuth object"""
        oauth_object = spotipy.SpotifyOAuth(client_id=self.CLIENT_ID, client_secret=self.CLIENT_SECRET,
                                            redirect_uri=self.REDIRECT_URI, scope=self.scope)
        token_data = oauth_object.get_access_token()
        self.token = token_data["access_token"]

        return oauth_object

    def generate_spotify_object(self):
        """Generates the spotify object"""
        oauth_object = self.get_oauth_object()

        return spotipy.Spotify(oauth_manager=oauth_object)

    def get_authenticated_user(self):
        """Returns authenticated user ID"""
        return self.spotify_object.current_user()["id"]

    def generate_spotify_uri(self, music_titles, user_date):
        """Generates the spotify uri corresponding to the title's selected from web-scrapping"""

        year = user_date.split("-")[0]
        for title in music_titles:
            query = f"track={title}&year={year}"
            try:
                result = self.spotify_object.search(q=query, limit=1, type="track", market="US")
                uri = result["tracks"]["items"][0]["uri"]
            except Exception:
                print(f"Oops! No record found for track - {title}")
            else:
                self.spotify_uri.append(uri)

    def generate_playlist(self, user_id, playlist_title, user_date):
        """Creates playlist for the user and adds song tracks from titles coming from the web scrapping"""
        playlist = self.spotify_object.user_playlist_create(
            user=user_id,
            name=f"{user_date} {playlist_title}",
            public=False,
            description="Playlist")

        playlist_id = playlist["id"]

        self.spotify_object.playlist_add_items(playlist_id=playlist_id, items=self.spotify_uri)
        print("Completed! Please check your Spotify page for the new playlist. Enjoy!")

