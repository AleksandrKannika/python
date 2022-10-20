from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=Fe6iZLIM1j8")
g = yt.streams.filter(res="720p").first().download()
# f = yt.streams
# for i in f:
#     print(i)
# print()
# c = yt.streams.get_by_itag(22)    
# print(c)
