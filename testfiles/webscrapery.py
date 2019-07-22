from bs4 import BeautifulSoup
import requests

search = input("Enter the term you want to search here :  ")
params = {"q": search}

r=requests.get("https://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.find_all("li", {"class": "b_algo"})


for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        try:
            #print(item_text)
            #print(item_href)
            print("Parent: ", item.find("a").parent)
            print("Summary : ", item.find("a").parent.parent.find("p").text)

            #children = item.find("h2")
            #print("Next sibling of h2: ", children.next_sibling)
            #print("Previous sibling of h2: ", children.previous_sibling)
            #for child in children:
            #    print("Children ", child)
        except:
            print("Parent or Summary not found for the search query")

#print(soup.prettify())
