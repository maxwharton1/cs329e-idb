import json
from models import app, db, Shark, Investment


def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()
    return jsn


def create_sharks():
    sharks = load_json('sharks.json') #loads the recently created json file

    for oneShark in sharks['sharks']:
        name = oneShark['name']
        invested = oneShark['invested']
        deals = oneShark['deals']
        episodes = oneShark['episodes']
        picture = oneShark['picture']
        investments = oneShark['investments']

        newShark = Shark(name = name,
                        invested = invested,
                        deals = deals,
                        episodes = episodes,
                        picture = picture,
                        investments = investments)

        db.session.add(newShark)
        db.session.commit()

def create_deals():
    deals = load_json('sharks.json')

    for oneDeal in deals['deals']:
        name = oneDeal["name"]
        id = oneDeal["id"]
        episode = oneDeal["episode"]
        founders = oneDeal["founders"]
        location = oneDeal["location"]
        description = oneDeal["description"]
        investment = oneDeal["investment"]
        equity = oneDeal["equity"]
        picture = oneDeal["picture"]
        sharks = oneDeal["sharks"]

        newDeal= Shark(name = name,
                        id = id,
                        episode = episode,
                        founders = founders,
                        location = location,
                        description = description,
                        investment = investment,
                        equity = equity,
                        picture = picture,
                        sharks = sharks)

        db.session.add(newDeal)
        db.session.commit()



create_sharks()
create_deals()
 # end of create_db.py
