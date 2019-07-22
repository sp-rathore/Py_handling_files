import requests
import simplejson as json
import PIL
from PIL import Image
import os

##f = open("./scraping.json", "w+")

if os.path.isfile("./scraping.json") and os.stat("./scraping.json").st_size != 0:
    old_file1 = open("./scraping.json", "r+")
    data = json.loads(old_file1.read())
    print('Current name is: ', data["name"], ', current age is: ', data["age"], ', current gender is :', data["gender"])
    data["age"] = data["age"] + 5
    print("Current name is: ", data["name"], ", current age is: ", data["age"], ", current gender is :", data["gender"])
else:
    old_file1 = open("./scraping.json", "w+")
    data= {"name" : "Shishupal", "age" : 40, "gender" : "M"}
    print("Writing the file for first time with name as: ", data["name"], ", age as: ", data["age"], ",  and gender as :", data["gender"])

old_file1.seek(0)
old_file1.write(json.dumps(data))