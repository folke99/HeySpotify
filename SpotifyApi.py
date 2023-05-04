import requests
import socket

class SpotifyApi:
    def __init__(self, access_token):
        self.base_url = "https://api.spotify.com/v1"
        self.headers = {"Authorization": f"Bearer {access_token}"}

    def play_song(self, song_name):
        # Search for the song
        query = f"track:{song_name}"
        search_url = f"{self.base_url}/search?q={query}&type=track"
        response = requests.get(search_url, headers=self.headers).json()
        print("Response:", response)

        # Get the first result
        track_uri = None
        if response.get("tracks", {}).get("items"):
            track_uri = response["tracks"]["items"][0]["uri"]
        print("Track URI:", track_uri)

        # Get the user's available devices and their IDs
        devices_url = f"{self.base_url}/me/player/devices"
        response = requests.get(devices_url, headers=self.headers).json()
        print("Devices response:", response)

        # Find the ID of the device you want to play music on
        device_id = None
        print(socket.gethostname())
        for device in response.get("devices", []):
            if device.get("name") == socket.gethostname().upper():
                device_id = device.get("id")
                break

        # Start playback on the specified device
        if track_uri and device_id:
            playback_url = f"{self.base_url}/me/player/play?device_id={device_id}"
            data = {"uris": [track_uri]}
            try:
                response = requests.put(playback_url, headers=self.headers, json=data)
                print("Play response:", response.json())
            except:
                print("Error: json data is not valid")

    def pause(self):
        pause_url = f"{self.base_url}/me/player/pause"
        try:
            response = requests.put(pause_url, headers=self.headers)
            print("Pause response:", response.json())
        except:
            print("Error: json data is not valid")

    def unpause(self):
        unpause_url = f"{self.base_url}/me/player/play"
        try:
            response = requests.put(unpause_url, headers=self.headers)
            print("Unpause response:", response.json())
        except:
            print("Error: json data is not valid")

    def next_song(self):
        next_url = f"{self.base_url}/me/player/next"
        try:
            response = requests.post(next_url, headers=self.headers)
            print("Next response:", response.json())
        except:
            print("Error: json data is not valid")

    def previous_song(self):
        previous_url = f"{self.base_url}/me/player/previous"
        try:
            response = requests.post(previous_url, headers=self.headers)
            print("Previous response:", response.json())
        except:
            print("Error: json data is not valid")