import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

SPOTIFY_CLIENT_ID = "e6059e9e2b544756bb10a9a1d2a1427d"
SPOTIFY_CLIENT_SECRET = "cf5735ba52b14a0196994662d56a734d"


date = input('Which year-month-day do you want to travel to? Type the date in this format YYYY-MM-DD: \n>> ')

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")

url = response.text

soup = BeautifulSoup(url, "html.parser")

name_of_song = [name.getText().strip() for name in soup.select(".o-chart-results-list-row-container ul li ul li h3")]
print(name_of_song)

sp = spotipy.Spotify(
	auth_manager=SpotifyOAuth(
		scope="playlist-modify-private",
		redirect_uri="http://example.com",
		client_id = SPOTIFY_CLIENT_ID, 
		client_secret=SPOTIFY_CLIENT_SECRET,
		show_dialog=True,
		cache_path="token.txt",
	)
)

user_id = sp.current_user()["id"]
song_uris = []
year = date.split("-")[0]
for song in name_of_song:
	result = sp.search(q=f"track:{song} year:{year}", type="track")
	# print(result)
	try:
		uri = result["tracks"]["items"][0]["uri"]
		song_uris.append(uri)
	except IndexError:
		print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(
									user=user_id,
									name = f"{date} Billboard 100", 
									public=False)

sp.playlist_add_items(playlist_id = playlist["id"], items = song_uris)
