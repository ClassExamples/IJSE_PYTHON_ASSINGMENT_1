import sys

user = "__no_user__"

def view():
    print(user)

def login(username):
    user = username

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
    