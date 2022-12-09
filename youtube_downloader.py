from pytube import YouTube

download_path = 'output'


def input_equal_stop(string_to_check: str):
    if string_to_check == 'stop':
        quit()


while True:
    video_link = input("\nEnter a video link or type 'stop' to end the program\n:")
    input_equal_stop(video_link)
    yt = YouTube(video_link)

    print(f"Title:      {yt.title}\nAuthor:     {yt.author}\nViews:      {yt.views}\n\nChannel URL:  {yt.channel_url}"
          f"\nVideo URL:    {video_link}\n")

    x = input("Do you want to download the video? [y/n]\n:").lower()
    if x != "y":
        input_equal_stop(x)
    else:
        print("Loading...")
        try:
            yt.streams.get_highest_resolution().download(download_path)
            print('Download was successful\n')
        except:
            print("It was not possible to download the video\n")

    print("-" * 120)
