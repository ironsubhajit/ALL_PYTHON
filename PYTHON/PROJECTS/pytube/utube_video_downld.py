from pytube import YouTube

YouTube('https://youtu.be/v4OGQDH2e3g?list=RDv4OGQDH2e3g').streams.get_highest_resolution().download()
#yt = YouTube('https://youtu.be/v4OGQDH2e3g?list=RDv4OGQDH2e3g')
#print(yt.title)
