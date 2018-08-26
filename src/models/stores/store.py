import uuid
import src.models.stores.constants as StoreConstants
from src.common.database import Database
import src.models.stores.errors as StoreErrors


class Store(object):
    def __init__(self, name, url_prefix, tag_name, query, _id=None):
        self.name = name
        self.url_prefix = url_prefix
        self.tag_name = tag_name
        self.query = query
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Store {}".format(self.name)

    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "url_prefix": self.url_prefix,
            "tag_name": self.tag_name,
            "query": self.query
        }

    @classmethod
    def get_store_by_id(cls, id):
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"_id": id}))

    def save_store_to_mongo(self):
        Database.insert_method(StoreConstants.COLLECTION, self.json())

    @classmethod
    def get_store_by_name(cls, store_name):
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"name": store_name}))

    @classmethod
    def get_store_by_url_prefix(cls, url_prefix):
        """

        If we're given http:///www.johnlewis, we will know this belongs to JohnLewis.com
        :param url_prefix:
        :return:
        """

        # the $regex variable is a mongodb option that allows pattern matching in the database
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"url_prefix": {"$regex": '^{}'.format(url_prefix)}}))

    @classmethod
    def find_by_url(cls, url):
        """
        Return a store from a url like: http://www.johnlewis.com/item/<hex num>.html
        :param url: the item's URL
        :return: a Store, or raises a StoreNotFoundException if no store matches the URL
        """

        for i in range(0, len(url)+1):
            try:
                store = cls.get_store_by_url_prefix(url[:i])
                return store
            except:
                raise StoreErrors.StoreNotFoundException("The URL Prefix did not yield a result")