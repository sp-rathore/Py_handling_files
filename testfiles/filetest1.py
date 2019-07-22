import simplejson as json
import os
"""
newfile = open("newfile.txt", "w+")

string = " I am gonna use this data to write to the new file"

newfile.write(string)
"""

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    old_file = open("./ages.json", "r+")
    data = json.loads(old_file.read())
    print("Current age is ", data["age"], "--adding a year")
    data["age"] = data["age"] + 1
    print("New age is ", data["age"])
else:
    old_file = open("./ages.json", "w+")
    data ={"name": "Nick", "age" : 25}
    print("No file found, setting age to ", data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))
