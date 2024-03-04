def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    my_list = list()
    for name in names:
        my_list.append(f"Hello, my name is {name}.")
        # print(my_list)
    return my_list

def assign_rooms(names):
    rooms =  8
    guests = len(names)
    if guests <= rooms:
        my_list = list()
        room = 1
        for name in names:
            my_list.append(f"Hello, {name}! You'll be assigned to room {room}!")
            room += 1
    return my_list

def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)
    for badge in badges:
        print(badge)

    for room in rooms:
        print(room)