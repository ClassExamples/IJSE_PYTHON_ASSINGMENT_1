import sys
import json
import os

__session_file__ = "db/session.db"
__item_folder__ = "db/item"
__item__last_id__ = "db/item_id.db"


def __get_logged_user():
    f = open(__session_file__, "r")
    username = f.readline()
    return username


def view():
    username = __get_logged_user()
    print(username)


def login(username):
    f = open(__session_file__, "w")
    f.write(username)
    f.close()


class Item:
    def __init__(self):
        if os.path.exists(__item__last_id__):
            with open(__item__last_id__, "r") as last_id_f:
                self.last_id = int(last_id_f.readline())
        else:
            self.last_id = 0

    def save(self):
        id = self.last_id+1

        # Save database item
        _data_ = {
            "id": id,
            "name": self.name,
            "price": self.price,
            "sellingPrice": self.selling_price
        }
        with open(f"{__item_folder__}/{id}.db", "w") as item_file:
            json.dump(_data_, item_file)

        # Save next id
        self.last_id += 1
        with open(__item__last_id__, "w") as f:
            f.write(str(self.last_id))

    def find(self, id):
        with open(f"{__item_folder__}/{id}.db", "r") as item_file:
            _data_ = json.load(item_file)
            self.id = _data_["id"]
            self.name = _data_["name"]
            self.price = _data_["price"]
            self.selling_price = _data_["sellingPrice"]


def item_create(name, price, selling_price):
    item = Item()
    item.name = name
    item.price = price
    item.selling_price = selling_price
    item.save()


def item_all():
    print("Item All")


def item_view(id):
    item = Item()
    item.find(id)
    print(item.id, item.name, item.price, item.selling_price)


if __name__ == "__main__":
    arguments = sys.argv[1:]

    section = arguments[0]
    command = arguments[1]
    params = arguments[2:]

    if section == "user":
        if command == "login":
            login(*params)
        elif command == "view":
            view()
    elif section == "item":
        if command == "create":
            item_create(*params)
        elif command == "all":
            item_all()
        elif command == "view":
            item_view(*params)
