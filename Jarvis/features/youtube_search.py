import webbrowser, urllib, re
import urllib.parse
import urllib.request

domain = input("Enter the song name: ")
song = urllib.parse.urlencode({"search_query" : domain})
print("Song" + song)

# fetch the ?v=query_string
result = urllib.request.urlopen("http://www.youtube.com/results?" + song)
print(result)

# make the url of the first result song
search_results = re.findall(r'href=\"\/watch\?v=(.{4})', result.read().decode())
print(search_results)

# make the final url of song selects the very first result from youtube result
url = "http://www.youtube.com/watch?v="+str(search_results)

# play the song using webBrowser module which opens the browser 
# webbrowser.open(url, new = 1)
webbrowser.open_new(url)