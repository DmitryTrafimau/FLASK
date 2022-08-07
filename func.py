import json


def data_saver():
    with open('data_goods.json', 'w') as f:
        json.dump(database, f, indent=2)


def donator():
    global reply
    if not database:
        reply = 'Извините, ничего нет. Зайдите позже.'
    elif database[0].get('qty') > 1:
        reply = f'Вот вам {database[0].get("name")}'
        database[0].update({'qty': (database[0].get('qty') - 1)})
    elif database[0].get('qty') == 1:
        reply = f'Вот вам {database[0].get("name")}'
        database.pop(0)
    return reply


def fifo():
    donator()
    data_saver()


def lifo():
    database.reverse()
    donator()
    database.reverse()
    data_saver()


with open('data_goods.json') as k:
    database = json.load(k)
