import os
import threading
import time
from datetime import datetime, timedelta
import requests
import secrets


def get_refresh_token():
    client_id = secrets.SPOTIFY_CLIENT_ID
    client_secret = secrets.SPOTIFY_CLIENT_SECRET
    refresh_token = secrets.SPOTIFY_REFRESH_TOKEN
    auth_response = requests.post('https://accounts.spotify.com/api/token', {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': client_id,
        'client_secret': client_secret,
    })

    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    print(access_token)


def refresh_token():
    """Refreshes the access token and updates the environment variable"""
    print("Refreshing token...")
    client_id = secrets.SPOTIFY_CLIENT_ID
    client_secret = secrets.SPOTIFY_CLIENT_SECRET
    refresh_token = secrets.SPOTIFY_REFRESH_TOKEN
    auth_response = requests.post('https://accounts.spotify.com/api/token', {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': client_id,
        'client_secret': client_secret,
    })

    # Check if token refresh was successful
    if auth_response.status_code == 200:
        access_token = auth_response.json()["access_token"]
        expires_in = auth_response.json()["expires_in"]

        # Update the environment variable with new token and expiry time
        secrets.SPOTIFY_AUTH_TOKEN = access_token
        secrets.SPOTIFY_TOKEN_EXPIRY = str(
            datetime.now() + timedelta(seconds=expires_in)
        )
        print("Token refreshed successfully")
    else:
        print("Failed to refresh token")



def token_refresh_loop():
    """Continuously refreshes the token before it expires"""
    while True:
        token_expiry = datetime.fromisoformat(
            secrets.SPOTIFY_TOKEN_EXPIRY
        )

        # Refresh the token before it expires
        if datetime.now() + timedelta(minutes=5) >= token_expiry:
            refresh_token()

        # Wait for some time before checking again
        time.sleep(60)

def start_token_refresh_loop():
    # Start the token refresh loop in a separate thread
    refresh_thread = threading.Thread(target=token_refresh_loop)
    refresh_thread.start()
