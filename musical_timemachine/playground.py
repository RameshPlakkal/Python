import datetime

print(datetime.date.today())

list = {'collaborative': False, 'description': '', 'external_urls': {'spotify': 'https://open.spotify.com/playlist'
                                                                                '/2jPT0o9r8ayyAyvYowh5p2'},
        'followers': {'href': None, 'total': 0}, 'href':
            'https://api.spotify.com/v1/playlists/2jPT0o9r8ayyAyvYowh5p2', 'id': '2jPT0o9r8ayyAyvYowh5p2',
        'images': [], 'primary_color': None, 'name': 'Billboard Hot 100™', 'type': 'playlist',
        'uri': 'spotify:playlist:2jPT0o9r8ayyAyvYowh5p2',
        'owner': {'href': 'https://api.spotify.com/v1/users'
                                                                        '/931a3f6d002643d39096d56fedefb729',
                                                                    'id': '931a3f6d002643d39096d56fedefb729',
                                                                    'type': 'user',
                                                                    'uri':
                                                                        'spotify:user:931a3f6d002643d39096d56fedefb729', 'display_name': None, 'external_urls': {'spotify': 'https://open.spotify.com/user/931a3f6d002643d39096d56fedefb729'}}, 'public': False, 'snapshot_id': 'MSw2YTc1YjJhODJjZjVjYmEyMjg1NjNkMmY5NDc3NjY2MDIxYWJjYWIw', 'tracks': {'limit': 100, 'next': None, 'offset': 0, 'previous': None, 'href': 'https://api.spotify.com/v1/playlists/2jPT0o9r8ayyAyvYowh5p2/tracks', 'total': 0, 'items': []}}


list = ['Smooth', 'Back At One', 'I Wanna Love You Forever', 'My Love Is Your Love', 'I Knew I Loved You', 'I Need To Know', 'Hot Boyz', "U Know What's Up", 'Bring It All To Me', 'Girl On TV', 'What A Girl Wants', '24/7', 'Blue (Da Ba Dee)', 'Then The Morning Comes', "He Can't Love U", 'Waiting For Tonight', "That's The Way It Is", 'The Christmas Song (Chestnuts Roasting On An Open Fire)', "Dancin'", 'Steal My Sunshine', 'Get It On Tonite', 'Learn To Fly', 'Big Deal', 'Meet Virginia', 'Unpretty', 'Breathe', 'Back That Thang Up', '4, 5, 6', 'Stay The Night', "Don't Say You Love Me", 'Where My Girls At?', 'Mambo No. 5 (A Little Bit Of...)', 'Hanginaround', 'Take A Picture', 'Get Gone', 'Someday', "He Didn't Have To Be", 'Got Your Money', 'Shake Your Bon-Bon', 'If You Love Me', 'Black Balloon', 'Rhythm Divine', 'Thank God I Found You', 'Satisfy You', 'Amazed', 'What Do You Say', 'You Can Do It', 'Cowboy Take Me Away', 'When I Said I Do', 'My Best Friend', 'Got To Get It', 'All The Small Things', 'This Gift', 'Auld Lang Syne', 'Angels', 'Say My Name', 'Pop A Top', 'Caught Out There', '15 Minutes', 'Heartbreaker', 'Higher', 'Bling Bling', 'Will 2K', 'Deep Inside', 'All Things Considered', 'I Love You', 'Sexual (Li Da Di)', 'None Of Ur Friends Business', 'Deck The Halls', 'Left & Right', 'Smile', 'The Great Beyond', 'Bug A Boo', 'Show Me The Meaning Of Being Lonely', "We Can't Be Friends", '(You Drive Me) Crazy', 'One Night Stand', 'N 2 Gether Now', 'No More Rain (In This Cloud)', 'Home To You', 'The Chemicals Between Us', 'Tha Block Is Hot', 'Guerrilla Radio', 'Live, Laugh, Love', 'Notorious B.I.G.', "She Thinks My Tractor's Sexy", 'Larger Than Life', 'There She Goes', 'The Greatest Romance Ever Sold', 'The Rockafeller Skank', 'Give You What You Want (Fa Sure)', 'Music Of My Heart', 'A Country Boy Can Survive (Y2K Version)', 'I Wanna Know', 'Re-arranged', 'L.A. Song', 'Gotta Man', "The Quittin' Kind", 'Steam', 'NAStradamus']

token= "BQDol6h30LSoQtsN1Ss-zHojQ0aBdCwVMzj-vvSIwyj_J-XjLrXRtBNLFN79QbmSzvZcMlAtxcavEATSkcfQqZTV8QJMdlQzZfN-rhhhzCIrKBA0ijzmVyMPlrQJY9bYR8vECHmQO7weVps253GI3RPm2elYDKrm_y-jU4eKyEsD5ZMNinpWMFYbv0InHXNqk1H6lOZuQQuE3teKhuqpvf6RZMgLUN6OfnsOhg"


# Method 2 to identify track uri's

# spotify_url = "https://api.spotify.com/v1/search"
# spotify_headers = {
#     "Authorization": f"Bearer {self.token}"
# }
# # spotify_params = {
# #     "q": query,
# #     "market": "US",
# #     "type": "track",
# #     "limit": 1,
# # }
#
#
# # response = requests.get(url=spotify_url, params=spotify_params, headers=spotify_headers)
# # data = response.json()
# # uri = data["tracks"]["items"][0]["uri"]
# #
