import time
from buildings import OreFactory, Conveyor, Building
tick = 0

player_input = "[x]====>"


buildings: list[Building] = []


def make_building(building_prefix: str, x: int, y: int):
    if building_prefix == "x":
        new_building = OreFactory("OreFactory", x, y)
        buildings.append(new_building)


def init_map(play_map: str):
    for i, char in enumerate(play_map):
        if char == "x":
            new_orefactory = OreFactory("OreFactory", len(buildings), 0)
            buildings.append(new_orefactory)
        if char == "=":
            new_conveyor = Conveyor("Conveyor", len(buildings), 0, "=")
            buildings.append(new_conveyor)
        if char == ">":
            new_conveyor = Conveyor("Conveyor", len(buildings), 0, ">")
            buildings.append(new_conveyor)
    
    for building in buildings:
        if isinstance(building, OreFactory):
            building.after_init(buildings)
            
    print(buildings)


def recreate_map() -> str:
    map_string = ""
    for building in buildings:
        map_string += building.get_prefix()
    return map_string


init_map(player_input)


while True:
    tick += 1
    for building in buildings:
        time.sleep(0.2)
        building.update(tick)
        print(recreate_map())
    



# iets met string map en de building map klopt niet