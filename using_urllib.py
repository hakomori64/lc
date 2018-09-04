import urllib.request, urllib.parse
import time
import json

for i in range(10000):
  params = {
    "zipcode" : "10" + str(i).zfill(5),
  }
  p = urllib.parse.urlencode(params)
  url = "http://zipcloud.ibsnet.co.jp/api/search?" + p
  print(url)

  with urllib.request.urlopen(url) as res:
    html = res.read().decode("utf-8")

  parsed_obj = json.loads(html)

  if parsed_obj["results"] != None:
    print(parsed_obj["results"][0]["address1"] + parsed_obj["results"][0]["address2"] + parsed_obj["results"][0]["address3"])

  time.sleep(1)

