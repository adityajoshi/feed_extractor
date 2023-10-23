import json
import ipdb

pattern = "https://www.youtube.com/feeds/videos.xml?channel_id="

with open('./data.json', 'r') as file:
    data = json.load(file)

#breakpoint()
for subs in data['subscriptions']:
	rss_url = subs['url'].replace('https://www.youtube.com/channel/', pattern)
	print('feed ' + "'" + subs['name'] + "'" + ' ' + "'" + rss_url + "'")
