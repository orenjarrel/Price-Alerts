from src.models.alerts.alert import Alert
from src.common.database import Database


Database.initialize()

alerts_needing_update = Alert.find_needing_update()


for alert in alerts_needing_update:
    alert.load_item_price()
    alert.send_email_if_price_reached()


# saved DB entry
# { "_id" : "4b394e96d3fa47918b7b5d2cd5dcd1e6", "name" : "John Lewis", "url_prefix" : "https://www.johnlewis.com", "tag_name" : "p", "query" : { "class" : "price--large" } }
