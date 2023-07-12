import requests
from constants import client_id, client_secret, redirect_url
# Replace the placeholders with your actual client ID, client secret, and redirect URL


# Step 1: Redirect the user to the authorization URL
authorization_url = f'https://api.instagram.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_url}&scope=user_profile,user_media&response_type=code'

# Step 2: Once the user grants permission, obtain the Authorization Code
# Write the code to handle the redirection and retrieve the Authorization Code

# Step 3: Exchange the Authorization Code for an Access Token
exchange_url = 'https://api.instagram.com/oauth/access_token'
payload = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'authorization_code',
    'redirect_uri': redirect_url,
    'code': authorization_code  # Replace with the actual Authorization Code
}
response = requests.post(exchange_url, data=payload)

# Step 4: Extract the Access Token from the response
access_token = response.json()['access_token']

print(access_token)
'''# Replace the placeholder with your actual access token
access_token = 'your_access_token'

# Define the endpoint URL to fetch the latest posts
endpoint_url = f'https://graph.instagram.com/me/media?fields=id,caption,media_type,media_url,thumbnail_url,permalink&access_token={access_token}'

# Send a GET request to the endpoint URL
response = requests.get(endpoint_url)

# Check if the request was successful
if response.status_code == 200:
    # Extract the posts data from the response
    posts_data = response.json()['data']

    # Loop through the posts and display the details
    for post in posts_data:
        caption = post.get('caption', '')
        media_type = post['media_type']
        media_url = post['media_url']
        thumbnail_url = post['thumbnail_url']
        permalink = post['permalink']

        print('-----------------------------')
        print('Caption:', caption)
        print('Media Type:', media_type)
        print('Media URL:', media_url)
        print('Thumbnail URL:', thumbnail_url)
        print('Permalink:', permalink)
        print('-----------------------------')
else:
    print('Error:', response.status_code)
'''