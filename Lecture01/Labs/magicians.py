magicians = ["Duo", "Jie", "Lillian"]

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    great_magicians = []
    for magician in magicians:
        great_magicians.append("Great " + magician)
    return great_magicians

show_magicians(magicians)       # show the list of the original names
great_magicians = make_great(magicians)
show_magicians(great_magicians) # show the list with Greate added to each magician's name