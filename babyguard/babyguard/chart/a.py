import urllib
import datetime
from urllib.request import urlopen

data = {}
data['day'] = datetime.datetime.now().strftime('%Y-%m-%d')
data['desc'] = 'crawl_add' 
data['cnt'] = '1' 
url = 'http://123.206.69.25:8000/chart/test'
post_data = urllib.parse.urlencode(data)
req = urlopen(url, post_data.encode(encoding='UTF8'))
content = req.read()
