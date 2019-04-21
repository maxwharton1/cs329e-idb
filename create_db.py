import json
from models import app, db, Shark, Investment


def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()
    return jsn


def create_sharks():
    sharks1 = load_json('sharks.json') #loads the recently created json file

    for oneShark in sharks1['sharks']:
        name = oneShark['name']
        url = oneShark['url']
        invested = oneShark['invested']
        deals = oneShark['deals']
        episodes = oneShark['episodes']
        base = oneShark['base']
        picture = oneShark['picture']
        investments = oneShark['investments']
        investmentsURL = oneShark['investmentsURL']

        newShark = Shark(name = name,
                        url = url,
                        invested = invested,
                        base = base,
                        deals = deals,
                        episodes = episodes,
                        picture = picture,
                        investments = investments,
                        investmentsURL = investmentsURL)

        db.session.add(newShark)
        db.session.commit()

def create_deals():
    deals = load_json('sharks.json')

    for oneDeal in deals['deals']:
        name = oneDeal["name"]
        id = oneDeal["id"]
        url = oneDeal["url"]
        base = oneDeal['base']
        episode = oneDeal["episode"]
        founders = oneDeal["founders"]
        location = oneDeal["location"]
        description = oneDeal["description"]
        investment = oneDeal["investment"]
        equity = oneDeal["equity"]
        picture = oneDeal["picture"]
        sharks = oneDeal["sharks"]
        sharksURL = oneDeal["sharksURL"]

        newDeal= Investment(name = name,
                        id = id,
                        url = url,
                        episode = episode,
                        founders = founders,
                        location = location,
                        base = base,
                        description = description,
                        investment = investment,
                        equity = equity,
                        picture = picture,
                        sharks = sharks,
                        sharksURL = sharksURL)

        db.session.add(newDeal)
        db.session.commit()



create_sharks()
create_deals()
 # end of create_db.py
