class Room:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__rooms = {}

    def set_description(self, description: str) -> None:
        self.__description = description

    def set_character(self, character: object) -> None:
        self.character = character

    def set_item(self, item: object) -> None:
        self.__item = item

    def get_details(self) -> None:
        print(self.name)
        print('--------------------')
        print(self.__description)
        for direction, room in self.__rooms.items():
            print(f'The {room.name} is {direction}')

    def get_character(self) -> object:
        try:
            return self.character
        except AttributeError:
            return None

    def get_item(self) -> object:
        try:
            return self.__item
        except AttributeError:
            return None

    def link_room(self, room: object, direction: str) -> None:
        self.__rooms[direction] = room

    def move(self, direction: str) -> object:
        return self.__rooms[direction]


defeated = 0
class Enemy:
    def __init__(self, name: str, description: str) -> None:
        self.__name = name
        self.__description = description

    def set_conversation(self, conversation: str) -> None:
        self.__conversation = conversation

    def set_weakness(self, weakness: str) -> None:
        self.__weakness = weakness

    def describe(self) -> None:
        print(f'{self.__name} is here!')
        print(self.__description)

    def talk(self) -> None:
        print(f'[{self.__name} says]: {self.__conversation}')

    def fight(self, fight_with: str) -> bool:
        if fight_with == self.__weakness:
            global defeated
            defeated += 1
            return True
        return False

    def get_defeated(self) -> int:
        global defeated
        return defeated


class Item:
    def __init__(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_description(self, description: str) -> None:
        self.__description = description

    def describe(self) -> None:
        print(f'The [{self.__name}] is here - {self.__description}')
