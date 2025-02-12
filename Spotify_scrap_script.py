import requests
import base64

# Spotify API credentials
CLIENT_ID = ' ' #Spotify API client ID
CLIENT_SECRET = ' '#Spotify API client secret

# Get an access token
def get_access_token(client_id, client_secret):
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    headers = {
        'Authorization': f'Basic {auth_header}'
    }
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(auth_url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        print(f"Error getting access token: {response.status_code} - {response.text}")
        return None

# Search for tracks from a specific year
def search_tracks(year, access_token):
    url = 'https://api.spotify.com/v1/search'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    params = {
        'q': f'year:{year}',
        'limit': 50,
        'offset': 0,
        'type': 'track',  
        'market': 'US'  
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching tracks: {response.status_code} - {response.text}")
        return None

# Step 3: Process and display the results
def display_tracks(data):
    if data and 'tracks' in data:
        tracks = data['tracks']['items']
        for track in tracks:
            name = track['name']
            artist = track['artists'][0]['name']
            album = track['album']['name']
            print(f"Track: {name}, Artist: {artist}, Album: {album}")
    else:
        print("No tracks found.")

def main():
    # Get access token
    access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)
    if not access_token:
        return

    # Search for tracks from the year 2017
    year = 2017
    data = search_tracks(year, access_token)
    if data:
        display_tracks(data)

# Run the script
if __name__ == '__main__':
    main()