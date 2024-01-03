# YouTube Assistant

## Overview

This is your personal assistant that helps you perform various tasks on youtube by simply chatting with it. This includes:
- Searching for videos, playlists and channels using various criteria, for example: ``Find me atleast ten videos from the freecodecamp.org youtube channel that teach begineers how to develop web applications using FatsAPI and were uploaded after June of 2023.``
- Creating playlists and adding videos to those playlists, for example ``Create a private playlist called Daily videos. Add the following videos to that playlist: How to set an annual budget from cnbc, 2023 in seven minitues from Vox``.
- Viewing comments for a particular video, commenting on a particular video and answering comments on a particular video.
- Uploading videos to youtube and updating the video and channel details.

## Getting Started

To get started, you need a verified Google Account and Google API keys with the correct permissions as well as an openai api key.

### How to Get A Google API Key
Follow the instructions in this short [article](https://medium.com/@lyle-okoth/how-to-get-a-google-api-key-d3c38649eaae) to get an API key.

1. Clone the github repo:
```sh
git clone https://github.com/twyle/youtube-assistant
```
2. Navigate to the clode repo
```sh
cd youtube-assistant
```
3. Create the environment secrets. They should look like the ``.env_example`` provided
```sh
touch .env
```
4. Start the application:
```sh
chainlit run assistant.py
```
