import requests
import simplejson as json
from io import BytesIO
from PIL import Image

'''
params = {"#q": "pizza"}

r = requests.get("https://www.bing.com/search", params=params)

print("Status of request to google is:", r.status_code)

print(r.url)

print(r.text)

f = open("./page.html", "w+")
f.write(r.text)
'''

'''
r = requests.get("http://1.bp.blogspot.com/-djfbp-imKIk/UPklywOCqrI/AAAAAAAAGwk/iYVRFYQLHCw/s1600/India_Gate+indin+flag+hd+wallpaper.jpg")

print("Status of request is:", r.status_code)

image1 = Image.open(BytesIO(r.content))

path = "./image1." + image1.format

print(image1.size, image1.format, image1.mode)

try:
    image1.save(path, image1.format)
except IOError:
    print("Cannot Save Image: Sorrrrryyy")
'''

my_data = {"name": "Shishupal", "email": "spsr@gmail.com"}

r = requests.post("https://www.w3schools.com/php/welcome.php", data=my_data)

f = open("myfile.html", "w+")
f.write(json.loads(r.text))
