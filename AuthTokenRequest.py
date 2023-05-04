import requests
import secrets

def getRefreshToken():
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

def getAuthToken():
    pass


if __name__ == "__main__":
    #getAuthToken()
    getRefreshToken()
