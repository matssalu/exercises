import sys
import urllib.request
import re
import json

artist = re.sub(" ", "%20", sys.argv[1])
nummer = re.sub(" ", "%20", sys.argv[2])

url = f"https://api.lyrics.ovh/v1/{artist}/{nummer}"


with urllib.request.urlopen(url) as input:
    data = json.loads(input.read())
    print(data['lyrics'])
