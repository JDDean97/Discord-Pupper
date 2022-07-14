import os
import requests
import random
from dotenv import load_dotenv

def getImgUrl(term):
    load_dotenv()
    # key = os.getenv('GOOGLE_KEY')
    key = os.environ["GOOGLE_TOKEN"]
    _url = "https://www.googleapis.com/customsearch/v1"
    offset = random.randint(1,50)
    _params = {'key':key,'q':term,'num':'1','start':offset,'searchType':"image",'cx':"4426fb15ed7f0c118"}
    r = requests.get(url=_url, params=_params)
    data = r.json()
    imgLink = data['items'][0]['link']
    return imgLink


# print(getImgUrl())