from youtube import YouTube


client_secrets_file = '/home/lyle/Downloads/search.json'
youtube_client = YouTube(client_secret_file=client_secrets_file)
youtube_client_object = youtube_client.authenticate()
youtube_client.youtube_client = youtube_client_object
