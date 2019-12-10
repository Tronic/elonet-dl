import json
import sys
from subprocess import PIPE, Popen
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup as bs

url = sys.argv[1] if len(sys.argv) == 2 else input("elonet URL to download:\n")
print("Downloading...")

# Extract playlist URL
soup = bs(requests.get(url).text, "html.parser")
name = soup.find("h1", dict(property="name")).text + ".mp4"
assert "/" not in name and "\\" not in name and not name.startswith("."), name
sources = soup.find("span", dict(id="video-data"))["data-video-sources"]
sources = json.loads(sources)
url = next(s['src'] for s in sources if s['type'] == 'application/x-mpegURL')

# Load playlist for another playlist...
url = urljoin(url, next(line for line in requests.get(url).text.split("\n") if line.endswith(".m3u8")))

# Get actual playlist of chunks
ts_files = [
    urljoin(url, line)
    for line in requests.get(url).text.split("\n")
    if line.endswith(".ts")
]

# Download TS files and remux into MP4
cmd = "ffmpeg -hide_banner -loglevel warning -y -i - -c copy".split(" ")
with Popen([*cmd, name], stdin=PIPE) as proc:
    for ts in ts_files:
        print(">>> ", ts.split("/")[-1])
        proc.stdin.write(requests.get(ts).content)

print(name, "downloaded")
