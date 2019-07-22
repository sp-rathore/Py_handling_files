import simplejson as json
import requests


payload = {"longUrl" : "http://example.com"}

url_short = "https://www.googleapis.com/urlshortener/v1/url"

headers = {"Content-Type": "application/json"}

r = requests.post(url_short, json=payload, headers=headers)

##print(json.loads(r.text)["error"]["errors"][0])

##print(json.loads(r.text))


print(r.headers)

print(r.history)

