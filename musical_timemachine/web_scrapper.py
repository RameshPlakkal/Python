from bs4 import BeautifulSoup
import requests

BASE_URL = "https://www.billboard.com/charts/hot-100/"


class WebScrapper:

    def __init__(self):
        self.user_choice = ""
        self.playlist_title = ""

    def scrap_website(self, user_choice):
        """Scraps the web URL to find the top 100 music title for the date provided by the user (in user_choice)"""
        self.user_choice = user_choice

        scrap_url = f"{BASE_URL}{self.user_choice}"

        response = requests.get(scrap_url)
        web_data = response.text

        web_soup = BeautifulSoup(web_data, "html.parser")
        self.playlist_title = web_soup.title.string

        music_title = web_soup.select(selector="li ul li h3", limit=100)
        title = [title.getText().strip() for title in music_title]

        return title

