import bs4
from bs4 import BeautifulSoup
import io
from io import BytesIO
import requests
from PIL import Image
import os

def SearchImages():
    search = input("Enter the parameter for Search: ")
    params = {"q" : search}
    dir_name = search.replace(" ", "_").lower() ## creating a new dynamic directory by replacing spaces with _

    if not os.path.isdir(dir_name): # checking if the directory exists or not
        os.makedirs(dir_name)    # if not exists then using os.makedirs method to create a new directory

    r=requests.get("https://www.bing.com/images/search", params = params)
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.find_all("a", {"class" : "thumb"})

    for item in links:
        try:
            img_obj = requests.get(item.attrs["href"])
            print(" Link to the image is: ", item.attrs["href"])
            title = item.attrs["href"].split("/")[-1]
            try:
                img = Image.open(BytesIO(img_obj.content))
                #print ("format of image is " , img.format)
                #img.save("./image_store/" + title, img.format)
                img.save("./" + dir_name + "/" +  title, img.format)
            except:
                print("Print error saving image from net.")
        except:
                print("Could not retrieve image from net.")
    SearchImages()

SearchImages()