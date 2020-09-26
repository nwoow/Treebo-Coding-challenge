# Define Level in list of objects
level = []
rooms_by_level = []

# Initialize Rooms and Level
def initialize_level(levelnew,room):
    if levelnew and room:
        for i in range(5):
            level_and_room = {"level":i, "room":room, "available_room":room,"alloted_room":0}
            level.append(level_and_room)
            for j in range(1,6):
                rooms = {"room_number": j, "level": i,"alloted": False}
                rooms_by_level.append(rooms)
    else:
        print("Wrong Arguments")


def search_rooms(room_quantity):
    available_rooms = []
    if level and room_quantity:
        for item in range(len(level)):
            if level[item]["available_room"] > 0:
                if level[item]["available_room"] == 0:
                    print("Rooms Not available")
                    pass
                else:
                    available_rooms.append({"level": level[item]["level"], "rooms_available": level[item]["available_room"]})
            else:
                print("Rooms Not available")
        return available_rooms       
    else:
        print("Wrong Arguments") 



def allot_rooms(room_quantity,room_level):
    alloted_rooms = []
    for i in range(len(rooms_by_level)):
        if rooms_by_level[i]['level'] == room_level["level"]:
            rooms_by_level[i]['alloted'] = True
            alloted_rooms.append(rooms_by_level[i])
    return alloted_rooms

def check_in(room_quantity):
    if room_quantity:
        # Search Room 
        rooms = search_rooms(room_quantity)
        if len(rooms) > 0:
            for item in rooms:
                if item['rooms_available'] > 0 or item['rooms_available'] <= room_quantity:
                    # allot room based on search result
                    level[item["level"]]["available_room"] = level[item["level"]]["available_room"] - room_quantity
                    level[item["level"]]["alloted_room"] = room_quantity
                    return allot_rooms(room_quantity,level[item["level"]])
                    break
                else:
                    pass
        else:
            print("rooms not available")
    else:
        print("No value") 


# print(level)
initialize_level(5,5)
print(check_in(5))
print(check_in(5))
print(check_in(5))
print(check_in(5))

# check_in(5)
# check_in(4)
# check_in(1)
# check_in(5)


# print(rooms_by_level)


