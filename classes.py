from random import randint


class user:
    def __init__(self, name, charisma, passion, skill, charm, fame):
        self.name = name
        self.charisma = charisma
        self.passion = passion
        self.skill = skill
        self.hp = 2
        self.charm = charm
        self.inventory = []
        self.fame = fame

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def charm(self):
        return self._charm

    @charm.setter
    def charm(self, value):
        self._charm = value

    @property
    def charisma(self):
        return self._charisma

    @charisma.setter
    def charisma(self, value):
        self._charisma = value

    @property
    def skill(self):
        return self._skill

    @skill.setter
    def skill(self, value):
        self._skill = value

    @property
    def passion(self):
        return self._passion

    @passion.setter
    def passion(self, value):
        self._passion = value

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value

    @property
    def fame(self):
        return self._fame

    @fame.setter
    def fame(self, value):
        self._fame = value

    def change_charisma(self, d):
        if d:
            self.charisma += 1
        else:
            self.charisma -= 1

    def change_passion(self, d):
        if d:
            self.passion += 1
        else:
            self.passion -= 1

    def change_skill(self, d):
        if d:
            self.skill += 1
        else:
            self.skill -= 1

    def change_hp(self, d):
        if d:
            self.hp += 1
        else:
            self.hp -= 1

    def change_inventory(self, item, value):
        if value:
            self.inventory.append(item)
            print('You have successfully acquired', item.name)
        else:
            self.inventory.remove(item)

    def change_charm(self, d):
        if d:
            self.charm += 1
        else:
            self.charm -= 1

    def change_fame(self, d):
        if d:
            self.fame += 1
        else:
            self.fame -= 1


class Item:
    def __init__(self, name):
        self.name = name
        self.description = None
        self.item_placement = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    def set_item_placement(self):
        ls = [[0, 0, None], [0, 1, None], [0, 2, None], [1, 0, None], [1, 1, None], [1, 2, None]]
        ls[randint(0, len(ls) - 1)][2] = self.name

        for x in range(len(ls)):
            if ls[x][2] == self.name:
                self.item_placement.append(ls[x][0])
                self.item_placement.append(ls[x][1])
            else:
                continue

        return self.item_placement


class Characters:
    def __init__(self, name, role, description, risk, weakness, fame):
        self.name = name
        self.role = role
        self.description = description
        self.risk = risk
        self.weakness = [weakness]
        self.fame = fame
        self.inventory = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def weakness(self):
        return self._weakness

    @weakness.setter
    def weakness(self, value):
        self._weakness = value

    @property
    def risk(self):
        return self._risk

    @risk.setter
    def risk(self, value):
        self._risk = value

    @property
    def fame(self):
        return self._fame

    @fame.setter
    def fame(self, value):
        self._fame = value

    def fight(self, user_attribute):
        temp = None
        combat_item = input("What do u decide to fight with\n>").lower().strip()
        for i in user_attribute.inventory:
            if i.name == combat_item:
                temp = i.name

        if combat_item == temp:
            if combat_item in self.weakness:
                print(self.name, 'apologizes for picking a fight with you')
                print('you defeat', self.name, 'but you lose your item too')
                user_attribute.change_fame(True)
                for i in user_attribute.inventory:
                    temp = i.name
                    if temp == combat_item:
                        user_attribute.change_inventory(i, False)
                        break
            else:
                print('You lost to', self.name, 'your reputation has been tarnish')
                user_attribute.change_fame(True)
        else:
            print('Sorry you do not own this item')

    def steal(self, user_attribute):
        temp = None
        command = input('What would you like to steal\n> ').lower().strip()
        for i in self.inventory:
            temp = i.name
        if temp == command:
            if user_attribute.charisma >= self.risk:
                print('you successfully have stolen', command, 'from', self.name)
                for i in self.inventory:
                    temp = i.name
                    if temp == command:
                        user_attribute.change_inventory(i, True)
                        self.change_inventory(i, False)
                        break
            else:
                print('you are caught red handed and now your reputation is tarnished')
                user_attribute.change_fame(False)
        else:
            print('This item does not exist in', self.name, "'s inventory")

    def salute(self, user_attribute):
        if user_attribute.fame < self.fame:
            print('you salute', self.name)
            print('you gain their respect')
            user_attribute.change_charisma(True)
        else:
            print('[', self.name, ']', ':', 'oh thank you sir for saluting me')
            user_attribute.change_charisma(True)
            user_attribute.change_fame(False)

    def change_inventory(self, item, value):
        if value:
            self.inventory.append(item)
        else:
            self.inventory.remove(item)


class HitlerSubordinates(Characters):
    def __init__(self, name, role, description, risk, weakness, fame, loyalty, vulnerability):
        super().__init__(name, role, description, risk, weakness, fame)
        self.loyalty = loyalty
        self.vulnerability = vulnerability

    @property
    def loyalty(self):
        return self._loyalty

    @loyalty.setter
    def loyalty(self, value):
        self._loyalty = value

    def change_loyalty(self, d1):
        if d1:
            self.loyalty += 1
        else:
            self.loyalty -= 1

    def compliment(self, _user):
        compliment = (input('your compliment: ')).split()
        if self.vulnerability in compliment:
            print('you successfully charm', self.name)
            _user.change_fame(True)
        else:
            print('how dare you to try to sweet talk me')
            _user.change_fame(True)


class Hitler(Characters):
    def __init__(self, name, role, description, risk, weakness, fame, hp):
        super().__init__(name, role, description, risk, weakness, fame)
        self.hp = hp


class Room:
    def __init__(self, room_name, room_description, room_items):
        self.name = room_name
        self.description = room_description
        self.linked_rooms = {}
        self.room_visited = False
        self.room_items = []
        self.room_items.append(room_items)

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def search_room(self, user_attributes):
        room_item = self.room_items[0]
        _user_attributes = user_attributes

        def search_room_item(_room_item, _user_attributes):
            print('you have 3 tries to search the room using numbers, you cannot search the same place '
                  'again')
            lst = []
            for i in range(3):
                user_input1, user_input2 = None, None
                while (user_input1 is None and user_input2 is None) or ([user_input1, user_input2] in lst):
                    try:
                        user_input1 = int(input("enter row:"))
                        user_input2 = int(input("enter column:"))
                    except Exception:
                        print('invalid input')
                lst.append([user_input1, user_input2])

            ls = _room_item.set_item_placement()

            if ls in lst:
                print('You have found', _room_item.name)
                _user_attributes.change_inventory(_room_item, True)
            else:
                print('You plundered and plundered but could not find anything')

        search_room_item(room_item, user_attributes)
        self.room_items.remove(room_item)

    def describe(self):
        print(self.description)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        # print( self.name + " linked rooms :" + repr(self.linked_rooms) )

    def get_details(self):
        print(self.name)
        print("--------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            # print(f"{type(room)}, {type(direction)}")
            print("The " + room.name + " is to the " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

    def change_room_status(self):
        self.room_visited = True
