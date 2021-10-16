import sys

__session_file__ = "db/session.db"

def view():
    f = open(__session_file__,"r")
    username=f.readline()
    print(username)

def login(username):
    f = open(__session_file__,"w")
    f.write(username)
    f.close()


def item_create(name,price,selling_price):
    print(name,price,selling_price)

def item_all():
    print("Item All")

def item_view(id):
    print("View item ",id)


if __name__=="__main__":
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
    