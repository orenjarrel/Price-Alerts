import requests, re, uuid
from bs4 import BeautifulSoup
from src.common.database import Database
import src.models.items.constants as ItemConstants


class Item(object):
    def __init__(self, name, url, store, _id=None):
        self.name = name
        self.url = url
        self.store = store
        tag_name = store.tag_name
        query = store.query
        self.price = self.load_price(tag_name, query)
        self._id = uuid.uuid4().hex if _id is None else _id


    def __repr__(self):
        return "<Item {} with URL {}>".format(self.name, self.url)

    def load_price(self, tag_name, query):
        # Amazon: <span id="priceblock_ourprice" .. >
        request = requests.get(self.url)
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(tag_name, query)
        string_price = element.text.strip()

        pattern = re.compile("(\d+.\d+)") # this allows us to extract the actual numbers
        match = pattern.search(string_price) # this allows us to pull only 1 set of numbers

        return match.group()

    def save_item_to_mongo(self):
        # insert JSON representation
        Database.insert_method(ItemConstants.COLLECTION, self.json())

    def json(self):
        return {
            "name": self.name,
            "url": self.url
        }