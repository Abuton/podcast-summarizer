import feedparser
import requests

podcast_feed_url = "http://feeds.feedburner.com/TEDTalks_audio"
podcast_feed = feedparser.parse(podcast_feed_url)

file_name = f'{podcast_feed.entries[0].title.replace(" ", "_").replace("|", "_")}.mp3'


for item in podcast_feed.entries[0].links:
    if item['type'] == 'audio/mpeg':
        episode_url = item.href

    response = requests.get(episode_url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"File '{file_name}' downloaded successfully.")
    else:
        print(f"Failed to download file from URL: {episode_url}")
