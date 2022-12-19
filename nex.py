from pytube import Playlist
playlist = Playlist('https://www.youtube.com/watch?v=fmJsqBWkXm4&list=PLlxQJeQRaKDRnvgIvfHTV6ZY8M2eurH95')
print('Number of videos in playlist: %s' % len(playlist.video_urls))

# Loop through all videos in the playlist and download them
for video in playlist.videos:
    video.streams.filter(type="video" ,res="720p" , progressive=True , file_extension="mp4").order_by("resolution").first().download()
    
