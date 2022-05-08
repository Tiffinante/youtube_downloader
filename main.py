from pytube import YouTube

url = input("url :")
my_video = YouTube(url)

print(my_video.title)

print(my_video.thumbnail_url)

# TODO
# Error: re.error: missing ), unterminated subpattern at position 48

# my_video = my_video.streams.get_lowest_resolution()
# my_video.download()

