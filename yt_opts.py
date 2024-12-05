import yt_dlp
def get_playlist_info(url):
    ydl_opts = {
        'quiet': True,  # Suppress output
        'extract_flat': True,  # Only get metadata
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        playlist_info = ydl.extract_info(url, download=False)
        
    for video in playlist_info['entries']:
        print(f"Title: {video['title']}")
        print(f"Uploader: {video['uploader']}")
        print(f"Duration: {video['duration']} seconds")
        print("-" * 100)

# URL of playlist
playlist_url = input("Enter YouTube Playlist URL: ")
get_playlist_info(playlist_url)
