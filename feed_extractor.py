import json

pattern = "https://www.youtube.com/feeds/videos.xml?channel_id="

with open('./data.json', 'r') as file:
    data = json.load(file)

for sub in data['subscriptions']:
	rss_url = sub['url'].replace('https://www.youtube.com/channel/', pattern)
	print('feed ' + "'" + sub['name'] + "'" + ' ' + "'" + rss_url + "'")
