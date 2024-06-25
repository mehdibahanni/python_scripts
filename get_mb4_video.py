import requests 
import m3u8
import subprocess # Importing subprocess for running command line commands

# you most install 'ffmpeg' tool,
# to ensur that you can convert segment to file with extension of .mp4

master_url = 'https://spe.mwdy.club/hls/urlset/master.m3u8'

try:
    # Requesting the master.m3u8 file
    r = requests.get(master_url)
    r.raise_for_status()  # Raise an error if the request was not successful (4xx or 5xx status codes)

    # Parsing the master.m3u8 file content
    m3u8_master = m3u8.loads(r.text)
    print(m3u8_master)

    # Extracting the playlist URL from the master.m3u8 file
    playlist_url = m3u8_master.data['playlists'][0]['uri']

    # Requesting the playlist file
    play_r = requests.get(playlist_url)
    play_r.raise_for_status()  # Raise an error if the request was not successful (4xx or 5xx status codes)

    # Parsing the playlist file content
    m3u8_master_play = m3u8.loads(play_r.text)
    m3_data = m3u8_master_play.data

    # Downloading and writing each segment to 'video.ts'
    with open('video.ts', 'wb') as fs:
        for segment in m3_data['segments']:
            uri = segment['uri']
            if not uri.startswith('http'):
                uri = 'https://' + uri  # Adding the protocol if it's missing
            print(uri)
            r = requests.get(uri)
            r.raise_for_status()  # Raise an error if the request was not successful (4xx or 5xx status codes)
            fs.write(r.content)

    # Converting 'video.ts' to 'video.mp4' using ffmpeg
    subprocess.run(['ffmpeg', '-i', 'video.ts', 'video.mp4'])

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")

except m3u8.M3U8Exception as e:
    print(f"M3U8 parsing error: {e}")

except subprocess.CalledProcessError as e:
    print(f"ffmpeg error: {e}")
