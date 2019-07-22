import bs4
from bs4 import BeautifulSoup
import io
from io import BytesIO
import requests
from PIL import Image


search = input("Enter the parameter for Search: ")

params = {"q" : search}

r=requests.get("https://www.bing.com/images/search", params = params)
soup = BeautifulSoup(r.text, "html.parser")

links = soup.find_all("a", {"class" : "thumb"})
for item in links:
    img_obj = requests.get(item.attrs["href"])
    print(" Link to the image is: ", item.attrs["href"])
    title = item.attrs["href"].split("/")[-1]
    img = Image.open(BytesIO(img_obj.content))
    #print ("format of image is " , img.format)
    img.save("./image_store/" + title, img.format)