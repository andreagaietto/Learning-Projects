#gathers remaining keyword arguments in a dictionary
def fav_colors(**kwargs):
    print(kwargs)

fav_colors(colt="purple", ruby="red", ethel="teal")

def favorite_colors(**kwargs):
    for person, color in kwargs.items():
        print(person, color)

favorite_colors(colt="purple", ruby="red", ethel="teal")