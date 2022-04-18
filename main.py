# All the imports to be used in the program
import os
import re
import time
import random
from typing import Optional

import pygame
import math
from pygame.locals import *

from classes import user, Room, Item, HitlerSubordinates
from caesarcipher import CaesarCipher

# Object Instantiation
Room_Key = Item('Broadcast room key')
knife = Item('knife')
Gun = Item('gun')
poison_vial = Item('Poison Vial')
main_hall = Room("Main Hall", "This the enthralling main hallway of the the Fuhrer himself, proceed with caution", None)
generals_room = Room("Generals' Room", 'This is where all the planning happens', Room_Key)
broadcast_room = Room("The Broadcast Room", "The department that makes sure Germans get their daily dose of propaganda",
                      None)
dining_hall = Room("Dining Hall", "A communal place for all the soldiers to meet, greet and eat", poison_vial)
shooting_range = Room("The Shooting Range", "The range where soldiers are required to aim", None)
main_hall.link_room(generals_room, "east")
generals_room.link_room(main_hall, "west")
main_hall.link_room(dining_hall, 'west')
dining_hall.link_room(main_hall, 'east')
dining_hall.link_room(broadcast_room, 'north')
broadcast_room.link_room(dining_hall, 'south')
generals_room.link_room(shooting_range, "south")
shooting_range.link_room(generals_room, "north")
General_Aladeen = HitlerSubordinates('Aladeen', 'General', 'In charge of ammunition and organized sieges', 2,
                                     'knife', 2, 4, 'kids')
Dining_Hall_Soldier = HitlerSubordinates('Sawcon', 'Private', 'In charge of the dining hall mess', 1, 'gun', 3, 3,
                                         'body')
Dining_Hall_Soldier.change_inventory(Room_Key, True)
General_Aladeen.change_inventory(Gun, True)

user1: Optional[user] = None


# General subroutines
def intro():
    print('''you wake up between 2 doors, both equally daunting, and as you look
around you, there are towering walls surrounding you from every direction
leaving you in a pitch dark state except for the slight glimmer coming from
either of the doors.''')
    print("one says:")
    print("")
    print('1) Explore the enigmatic environment behind Nazi Germany')
    print("the other says")
    print("2) Explore the escape of Napoleon Bonaparte")


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platform
        _ = os.system('cls')


def assign_points():
    total = 8
    x1, x2, x3, x4, x5 = 0, 0, 0, 0, 0

    while total != 0:

        try:
            x1 = abs(int(input("charisma: ")))
            x2 = abs(int(input("passion: ")))
            x3 = abs(int(input("skill: ")))
            x4 = abs(int(input("charm: ")))
            x5 = abs(int(input("fame: ")))

            total -= x1 + x2 + x3 + x4 + x5

        except Exception:

            print("invalid input try again")
            return assign_points()

        if total < 0:
            x1 = 0
            x2 = 0
            x3 = 0
            x4 = 0
            x5 = 0
            print("u have exceeded the limit, try again ")
            return assign_points()

    return x1, x2, x3, x4, x5


def user_setup():
    print("customize your character, you have 8 points to assign to your characters attributes, these points would be "
          "distributed between passion, charisma, skill, fame and charm. Any negative inputs would be taken as absolute"
          " positive values")
    charisma, passion, skill, charm, fame = assign_points()
    pattern = "[A-Za-z]+"
    name = input("name: ")
    while not re.fullmatch(pattern, name):
        name = input("invalid name try again: ")
    global user1
    user1 = user(name, charisma, passion, skill, charm, fame)
    print("your charisma is:", user1.charisma)
    print("your passion is:", user1.passion)
    print("your skill is:", user1.skill)
    print("your charm is:", user1.charm)
    print('your fame is:', user1.fame)
    print("your name is :", user1.name)


def current_user_stats():
    print("your charisma is:", user1.charisma)
    print("your passion is:", user1.passion)
    print("your skill is:", user1.skill)
    print("your charm is:", user1.charm)
    print('your current hp is:', user1.hp)
    lst = []
    for i in user1.inventory:
        temp = i.name
        lst.append(temp)
    print('your current inventory is:', lst)


def menu(character, room):
    selection = 0
    tries = 0
    while selection != '6' and tries < 5:
        print("you have between 6 options:\n1) Steal from", character.name, "\n2) Search",
              room.name, "\n3) Salute", character.name, "\n4) Fight", character.name, '\n5) Compliment',
              character.name, "\n6) Exit Menu")
        selection = input("> ")
        if selection == "1":
            character.steal(user1)
            current_user_stats()
            tries += 1
            selection = 0
        elif selection == "2":
            room.search_room(user1)
            current_user_stats()
            tries += 1
            selection = 0
        elif selection == "3":
            character.salute(user1)
            current_user_stats()
            tries += 1
            selection = 0
        elif selection == "4":
            character.fight(user1)
            current_user_stats()
            tries += 1
            selection = 0
        elif selection == '5':
            character.compliment(user1)
            current_user_stats()
            tries += 1
            selection = 0
        elif selection == '6':
            current_user_stats()
            break
        else:
            continue


def binary_decision_function(expression, fn1, fn2):
    selection = 0
    print(expression)
    while selection not in ('1', '2'):
        try:
            selection = input("> ")
            if selection == '1':
                fn1()
            elif selection == '2':
                fn2()
        except Exception:
            pass


def binary_decision_general(user_defined_input, input1, input2):
    selection = 0
    while selection not in ('1', '2'):
        try:
            selection = int(input(user_defined_input))
            if selection == '1':
                print(input1)
            elif selection == '2':
                print(input2)
                pass
        except Exception:
            pass


def validation():
    temp = False
    input1 = 0
    while not temp:
        try:
            input1 = int(input("Enter (integer): "))
            temp = True
        except Exception:
            pass
        print("try again")
    return input1


def level1(time_):
    cipher1 = CaesarCipher('Fuhrer', offset=14)
    cipher2 = CaesarCipher('War', offset=14)
    cipher3 = CaesarCipher('Rations', offset=14)
    cipher4 = CaesarCipher('Revolution', offset=14)
    cipher5 = CaesarCipher('Economy', offset=14)

    print('your offset is 14')
    print(cipher1.encoded, cipher2.encoded, cipher3.encoded, cipher4.encoded, cipher5.encoded)
    timer(time_)
    screen_clear()


def level2(time_):
    lst = []
    for x in range(5):
        lst.append(random.randint(1, 25))

    cipher1 = CaesarCipher('Fuhrer', offset=lst[0])
    cipher2 = CaesarCipher('War', offset=lst[1])
    cipher3 = CaesarCipher('Rations', offset=lst[2])
    cipher4 = CaesarCipher('Revolution', offset=lst[3])
    cipher5 = CaesarCipher('Economy', offset=lst[4])

    for x in range(len(lst)):
        print('your offset is:', lst[x])

    print(cipher1.encoded, cipher2.encoded, cipher3.encoded, cipher4.encoded, cipher5.encoded)
    timer(time_)
    screen_clear()


def level3(time_):
    lst = []
    for x in range(5):
        lst.append(random.randint(1, 25))

    cipher1 = CaesarCipher('Fuhrer', offset=lst[0])
    cipher2 = CaesarCipher('War', offset=lst[1])
    cipher3 = CaesarCipher('Rations', offset=lst[2])
    cipher4 = CaesarCipher('Revolution', offset=lst[3])
    cipher5 = CaesarCipher('Economy', offset=lst[4])
    print("a = 1 and ' = 0")

    for x in range(len(lst)):
        z = lst[x] // 10
        y = lst[x] % 10
        print('your offset is:', chr(z + 96), chr(y + 96))

    print(cipher1.encoded, cipher2.encoded, cipher3.encoded, cipher4.encoded, cipher5.encoded)
    timer(time_)
    screen_clear()


def timer(amount_of_time):
    t = amount_of_time
    temp = True
    while temp:
        while t != 0:
            mins = t // 60
            secs = t % 60
            timer_ = '{:02d}:{:02d}'.format(mins, secs)
            print(f"\r{timer_}", end="", flush=True)
            time.sleep(1)
            t -= 1
        temp = False


def room_transition(rt_input1, rt_input2, rt_input3, rt_function1, rt_function2):
    current_state = True
    while current_state:
        print("\n")
        rt_input3.get_details()
        print("Where do you want to go: ")
        command = input("> ")
        current_room = rt_input3.move(command.lower().strip())
        if current_room == rt_input1:
            rt_function1()
            current_state = False
        elif current_room == rt_input2:
            rt_function2()
            current_state = False


# Mini-Game subroutines
def aimTrainer(time_limit):
    pygame.init()
    # Constants to be set
    WIDTH = 900
    HEIGHT = 600
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    text_x = 10
    text_y = 10
    time_limit = time_limit

    # Colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    purple = (128, 0, 128)
    grey = (128, 128, 128)
    sky = (0, 0, 220)
    blue = (85, 206, 255)
    orange = (255, 127, 80)
    red = (200, 0, 0)
    light_red = (255, 0, 0)
    green = (0, 200, 0)
    light_green = (0, 255, 0)
    colors = [white, grey, purple, sky, blue, orange, red, light_red, green, light_green]

    clock = pygame.time.Clock()  # To set the frame rate

    # Changing variables

    score = 0
    start_time = time.time()

    # Setting up screen and circles

    font = pygame.font.SysFont('verdana', 32)
    cx = random.randint(100, WIDTH - 100)
    cy = random.randint(100, HEIGHT - 100)
    width_of_circle = random.randint(14, 20)
    pygame.draw.circle(SCREEN, random.choice(colors), (cx, cy), width_of_circle)

    # Function to show score
    def show_score(z, y):
        score_value = font.render('Score: ' + str(score), True, (255, 255, 255))
        SCREEN.blit(score_value, (z, y))

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return score
        # Keep a check of time elapsed since start of game
        elapsed_time = time.time() - start_time
        # check if time is over, then finish the subroutine and return the score
        if elapsed_time > time_limit:
            print('game over')
            pygame.quit()
            return score

        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        click = pygame.mouse.get_pressed()

        sqx = (x - cx) ** 2
        sqy = (y - cy) ** 2

        if math.sqrt(sqx + sqy) < width_of_circle and click[0] == 1:
            SCREEN.fill(black)  # Reset the screen
            cx = random.randint(20, WIDTH - 20)
            cy = random.randint(20, HEIGHT - 20)
            width_of_circle = random.randint(14, 20)
            pygame.draw.circle(SCREEN, random.choice(colors), (cx, cy), width_of_circle)
            score += 1

        show_score(text_x, text_y)
        pygame.display.update()
        clock.tick()


def breakout(user_lives, speed):
    pygame.init()

    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600

    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption('BreakMe')

    font = pygame.font.SysFont('Constantia', 30)
    # background color
    bg = (234, 218, 184)

    # brick colors
    brick_red = (242, 85, 96)
    brick_green = (86, 174, 87)
    brick_blue = (89, 177, 232)
    # paddle colors
    paddle_color = (142, 135, 123)
    paddle_outline = (100, 100, 100)
    text_colour = (78, 81, 139)

    # game variables
    COLS = 6
    ROWS = 6
    clock = pygame.time.Clock()
    FPS = 60
    live_ball = False
    game_over = 0
    lives = user_lives
    ball_speed = speed

    def write_text(text, _font, text_col, x, y):
        image = _font.render(text, True, text_col)
        SCREEN.blit(image, (x, y))

    # classes
    class Wall:
        def __init__(self):
            self.brick = None
            self.width = SCREEN_WIDTH // COLS
            self.height = 50

        def create_wall(self):
            self.brick = []
            strength = None
            # empty list for single block
            brick_individual = []
            for row in range(ROWS):
                # reset the block row list
                brick_row = []
                # iterate through each col in the row
                for col in range(COLS):
                    # produce x and y positions and create rectangle from these positions
                    brick_x = col * self.width
                    brick_y = row * self.height
                    rect = pygame.Rect(brick_x, brick_y, self.width, self.height)
                    # assign brick strength based on the rows:
                    if row < 2:
                        strength = 3
                    elif row < 4:
                        strength = 2
                    elif row < 6:
                        strength = 1
                    # creating list to store rectangle and its color
                    brick_individual = [rect, strength]
                    # appending individual brick to the brick row
                    brick_row.append(brick_individual)
                # adding row to the whole list of the blocks
                self.brick.append(brick_row)

        def draw_wall(self):
            brick_color = None
            for row in self.brick:
                for brick in row:
                    # set a color based on brick level strength
                    if brick[1] == 3:
                        brick_color = brick_blue
                    elif brick[1] == 2:
                        brick_color = brick_green
                    elif brick[1] == 1:
                        brick_color = brick_red
                    # drawing the bricks
                    pygame.draw.rect(SCREEN, brick_color, brick[0])
                    # to draw a border for each brick to be differentiated
                    pygame.draw.rect(SCREEN, bg, (brick[0]), 1)

    class Paddle:
        def __init__(self):
            # setting paddle variables
            self.height = 20
            self.width = int(SCREEN_WIDTH / COLS)
            self.x = int((SCREEN_WIDTH / 2) - (self.width / 2))
            self.y = SCREEN_HEIGHT - (self.height * 2)
            self.speed = 10
            self.rect = Rect(self.x, self.y, self.width, self.height)
            self.direction = 0

        def move(self):
            # resets the direction of the movement
            self.direction = 0
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.speed
                self.direction = -1
            if key[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
                self.rect.x += self.speed
                self.direction = 1

        def draw(self):
            pygame.draw.rect(SCREEN, paddle_color, self.rect)
            pygame.draw.rect(SCREEN, paddle_outline, self.rect, 3)

        def reset(self):
            self.height = 20
            self.width = int(SCREEN_WIDTH / COLS)
            self.x = int((SCREEN_WIDTH / 2) - (self.width / 2))
            self.y = SCREEN_HEIGHT - (self.height * 2)
            self.speed = 10
            self.rect = Rect(self.x, self.y, self.width, self.height)
            self.direction = 0

    class Ball:
        def __init__(self, x, y, _speed):
            self.radius = 10
            self.x = x - self.radius
            self.y = y
            self.rect = Rect(self.x, self.y, self.radius * 2, self.radius * 2)
            self.speed_x = _speed
            self.speed_y = -_speed
            self.max_speed = _speed + 1
            self.game_over = 0

        def move(self, _lives):
            collision_threshold = 5
            player_lives = _lives

            # checking for collision with walls - assuming wall has been destroyed completely
            wall_destroyed = 1
            row_counter = 0
            for row in wall.brick:
                item_counter = 0
                for item in row:
                    # checking for collision
                    if self.rect.colliderect(item[0]):
                        # collision from above
                        if abs(self.rect.bottom - item[0].top) < collision_threshold and self.speed_y > 0:
                            self.speed_y *= -1
                        # collision from below
                        if abs(self.rect.top - item[0].bottom) < collision_threshold and self.speed_y < 0:
                            self.speed_y *= -1
                        # collision from the right
                        if abs(self.rect.right - item[0].left) < collision_threshold and self.speed_x > 0:
                            self.speed_x *= -1
                        # collision from the left
                        if abs(self.rect.left - item[0].right) < collision_threshold and self.speed_x < 0:
                            self.speed_x *= -1
                        # reducing brick strength
                        if wall.brick[row_counter][item_counter][1] > 1:
                            wall.brick[row_counter][item_counter][1] -= 1
                        else:
                            wall.brick[row_counter][item_counter][0] = (0, 0, 0, 0)
                    # check if any brick exists
                    if wall.brick[row_counter][item_counter][0] != (0, 0, 0, 0):
                        wall_destroyed = 0
                    # increment item counter
                    item_counter += 1
                # increment row counter
                row_counter += 1
            # checking if wall is destroyed after going through all bricks
            if wall_destroyed == 1:
                self.game_over = 1

            if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
                self.speed_x *= -1
            if self.rect.top < 0:
                self.speed_y *= -1
            if self.rect.bottom > SCREEN_HEIGHT:
                self.game_over = -1
                player_lives -= 1
            # collision with paddle
            if self.rect.colliderect(user_paddle):
                # check for only collisions from top:
                if (abs(self.rect.bottom - user_paddle.rect.top) < collision_threshold) and (self.speed_y > 0):
                    self.speed_y *= -1
                    self.speed_x += user_paddle.direction
                    if self.speed_x > self.max_speed:
                        self.speed_x = self.max_speed
                    elif self.speed_x < 0 and self.speed_x < - self.max_speed:
                        self.speed_x = - self.max_speed
                else:
                    self.speed_x *= -1

            self.rect.x += self.speed_x
            self.rect.y += self.speed_y

            return self.game_over, player_lives

        def draw(self):
            pygame.draw.circle(SCREEN, paddle_color, ((self.rect.x + self.radius), (self.rect.y + self.radius)),
                               self.radius)
            pygame.draw.circle(SCREEN, paddle_outline, ((self.rect.x + self.radius), (self.rect.y + self.radius)),
                               self.radius, 3)

        def reset(self, x, y, _speed):
            self.radius = 10
            self.x = x - self.radius
            self.y = y
            self.rect = Rect(self.x, self.y, self.radius * 2, self.radius * 2)
            self.speed_x = _speed
            self.speed_y = -_speed
            self.max_speed = _speed + 1
            self.game_over = 0

    # creating objects
    wall = Wall()
    wall.create_wall()
    user_paddle = Paddle()
    ball = Ball(user_paddle.x + (user_paddle.width // 2), user_paddle.y - user_paddle.height, ball_speed)

    run = True

    while run and lives > 0:
        clock.tick(FPS)
        SCREEN.fill(bg)

        # drawing the wall
        wall.draw_wall()
        user_paddle.draw()
        ball.draw()
        if live_ball:
            user_paddle.move()
            game_over, lives = ball.move(lives)
            if game_over != 0:
                live_ball = False

        # player instructions
        if not live_ball:
            if game_over == 0:
                write_text('Click anywhere to start', font, text_colour, 150, SCREEN_HEIGHT // 2 + 100)
            elif game_over == 1:
                write_text('You won', font, text_colour, 250, SCREEN_HEIGHT // 2 + 50)
                pygame.quit()
                return lives
            elif game_over == -1:
                write_text('You lost', font, text_colour, 250, SCREEN_HEIGHT // 2)
                write_text(('You have ' + str(lives) + ' try(s) left'), font, text_colour, 165, SCREEN_HEIGHT // 2 + 50)
                write_text('Click anywhere to start', font, text_colour, 150, SCREEN_HEIGHT // 2 + 100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return lives
            if event.type == pygame.MOUSEBUTTONDOWN and live_ball is False:
                live_ball = True
                ball.reset(user_paddle.x + (user_paddle.width // 2), user_paddle.y - user_paddle.height, ball_speed)
                user_paddle.reset()
                wall.create_wall()

        pygame.display.update()

    pygame.quit()
    return lives


# Story Subroutines
def main():
    binary_decision_function("select your adventure: ", nazi_regime, bonaparte_escape)


def rallying_speech():
    time_amount = 8
    print('as you make up your mind to give the speech a small envelope is shoved into your pocket')
    print('it contains the following words: ')
    print('decrypt this message to find out what stirs soldiers towards rebellion and include it in your speech')
    if user1.skill <= 0:
        time_amount = 7
    elif user1.skill > 2:
        time_amount = 20

    if user1.passion <= 0:
        level3(time_amount)

    elif user1.passion > 2:
        level1(time_amount)

    else:
        level2(time_amount)

    temp = 0
    user_speech = input('enter your speech:\n> ')
    user_speech.split(' ')
    lst = ['fuhrer', 'war', 'revolution', 'rations', 'economy']
    for x in range(len(lst)):
        if lst[x] in user_speech:
            temp += 1
    if temp == 5:
        user1.change_charisma(True)
        user1.change_fame(True)
        user1.change_charm(True)
        print('your speech caused the whole infantry to erupt in applause, you are carried on their soldiers as a'
              ' messiah')
    elif 3 <= temp < 5:
        user1.change_fame(True)
        user1.change_charisma(True)
        print('your speech caused a disturbance among most soldiers as they nod their head in agreement')

    elif 1 <= temp < 3:
        user1.change_fame(True)
        print('your speech arouses a few suspicious looks around but you also see a few approving looks')
    else:
        user1.change_charisma(False)
        user1.change_fame(False)
        print('you are booed off the stage for your speech and you look for an escape before anyone reports your name')


def nazi_regime():
    print("given 2 options")
    print('live the life of a soldier in the nazi regime or experience the pain of being one of the prisoners')
    binary_decision_function("select your adventure: :", Main__Hall, jew_path)


def Main__Hall():
    global main_hall
    while not main_hall.room_visited:
        print('You are walking down the path when a soldier in a stunning black uniform walks up to u and says:\n"Ah',
              user1.name,
              'what are you doing here, General Aladeen is waiting for you"')
        print('While the soldier accompanies along you decide to engage in small talk. The soldier is unaware and is '
              'about to reveal crucial information about the general however you notice a scintillating object')
        print('You have to make a choice if you would rather 1) choose to pickpocket the mysterious object or '
              '2) listen to the crucial information')
        selection = 0
        while selection not in ('1', '2'):
            try:
                selection = input("> ")
                if selection == '1':
                    print(
                        'You decide to pickpocket the item and quickly escape the conversation to avoid being detected')
                    user1.change_inventory(knife, True)
                elif selection == '2':
                    print('[soldier]: I have heard he has an absurd fear when it comes to knives, however if you do'
                          'want to please him do mention his kids. I have also heard he has a gun ')
            except Exception:
                pass
        main_hall.change_room_status()
        room_transition(generals_room, dining_hall, main_hall, Generals_Room, Dining_Hall)
    print('You are back in the main hall where would u want go now')
    room_transition(generals_room, dining_hall, main_hall, Generals_Room, Dining_Hall)


def Generals_Room():
    while not generals_room.room_visited:
        print("You enter the room and are greeted by everyone")
        print("u say... greetings general...")
        user_test1 = input("> ")
        if user_test1.lower() == General_Aladeen.name.lower():
            print("[General]: I see you respect me")
        else:
            user1.change_charisma(False)
            print("[General]: That's not my name soldier")
        print('[General]: Anyways moving on... we need to decide which ally to send aid to')
        user_test2 = input("> ")
        allies = ['italy', 'japan']
        if user_test2.lower() in allies:
            print("[General]: Good decision")
            user1.change_passion(True)
        else:
            print("[General]: They not our ally...")
            user1.change_passion(False)
        print("[General]: Finally the topic to discuss we need a plan to attack...")
        user_decision1 = input("> ")
        if user_decision1.lower() == "russia":
            print("[General]: That might be interesting provided russia winters have just passed")
            user1.change_charisma(True)
        elif user_decision1.lower() == "belgium":
            print("[General]: Ah as per the original plan one would say")
            user1.change_passion(True)
        else:
            print('[General]: Why would you attack them??')
            user1.change_passion(False)
        print("[General]: Is there any particular way you would like to lay siege?")
        user_test3 = input("> ")
        if user_test3.lower() == 'blitzkrieg':
            user1.change_passion(True)
            print('[General]: Original to the plan')
        else:
            print('[General]: Hmm i really doubt that would work but thank you for your input regardless')
        print('[General]: You are free to go soldier however you might soon want to head to the shooting range to the '
              'right for daily practice')
        current_user_stats()
        print('You need to search the room till you find a key to progress')
        menu(General_Aladeen, generals_room)
        generals_room.change_room_status()
        room_transition(main_hall, shooting_range, generals_room, Main__Hall, Shooting_Range)
    print('You have been here before')
    room_transition(main_hall, shooting_range, generals_room, Main__Hall, Shooting_Range)


def Dining_Hall():
    while not dining_hall.room_visited:
        if not generals_room.room_visited:
            print('You enter into a rather quite room ')
            print('Yet another soldier reminds you that the general is waiting for you')
            room_transition(main_hall, broadcast_room, dining_hall, Main__Hall, Broadcast_Room)
        if not shooting_range.room_visited:
            print('The general has informed you to go practice at the shooting range first it is recommended '
                  'you proceed accordingly')
            room_transition(main_hall, broadcast_room, dining_hall, Main__Hall, Broadcast_Room)
        else:
            print('[Private Sawcon]: Oye', user1.name, 'we be hearing')
            print('[Private Sawcon]: That you had a meeting with good ol Aladeen')
            print('[Private Sawcon]: you think you are better than us?')
            print('You are given a choice')
            print('Either:\n1) Bad mouth the general or \n2) stand up for yourself')
            binary_decision_function("choose an option:", user1.change_charisma, user1.change_passion)
            print('[Private Sawcon]: "I-')
            print("As the  soldier is about to reply to you, there is an announcement about daily rations for "
                  "soldiers which causes a commotion")
            print("do you take this opportunity to \n1) make a rallying speech or \n2) use it as an distraction to "
                  "find an essential tool next to the kitchen")
            selection = 0
            print("make a choice: ")
            while selection not in ('1', '2'):
                try:
                    selection = input("> ")
                    if selection == '1':
                        rallying_speech()
                    elif selection == '2':
                        user1.change_inventory(knife, True)
                        print('you scour the room and successfully find a mini knife')
                except Exception:
                    pass
            current_user_stats()
            menu(Dining_Hall_Soldier, dining_hall)
            generals_room.change_room_status()
            room_transition(main_hall, broadcast_room, dining_hall, Main__Hall, Broadcast_Room)
    print('You have been here already')
    room_transition(main_hall, broadcast_room, dining_hall, Main__Hall, Broadcast_Room)


def word_check(num):
    word = None
    pattern = "[A-Za-z]+"
    for x in range(num):
        while not re.fullmatch(pattern, word):
            word = input("Is this your input to the masses? Pathetic, invalid input try again: ")


def Broadcast_Room():
    while Room_Key in user1.inventory:
        while not broadcast_room.room_visited:
            print('You find the Broadcast Room deserted and empty, and you find this as your opportunity '
                  'to put the final nail in the coffin')
            print('For every life you conserve you get to broadcast a single word to the masses disillusioned by his'
                  ' fantasies')
            time.sleep(2)
            number_of_lives = 4
            if user1.skill < 0:
                number_of_lives = 3
            elif user1.skill > 2:
                number_of_lives = 5
            speed = 3
            if user1.charisma < 0:
                speed = 4
            elif user1.charisma > 2:
                speed = 2
            score = breakout(number_of_lives, speed)
            if score == 5:
                print('You get to broadcast 5 times: ')
                word_check(5)
                user1.change_skill(True)
                user1.change_passion(True)
                user1.change_fame(True)
                user1.change_charisma(True)
                user1.change_charm(True)
            elif score == 4:
                print('You get to broadcast 4 times: ')
                word_check(4)
                user1.change_skill(True)
                user1.change_passion(True)
                user1.change_fame(True)
                user1.change_charisma(True)
            elif score == 3:
                print('You get to broadcast 3 times: ')
                word_check(3)
                user1.change_skill(True)
                user1.change_passion(True)
                user1.change_fame(True)
            elif score == 2:
                print('You get to broadcast 2 times: ')
                word_check(2)
                user1.change_skill(True)
                user1.change_passion(True)
            elif score == 1:
                print('You get to broadcast once: ')
                word_check(1)
                user1.change_skill(True)
            else:
                print('You could not complete the game ')
                user1.change_skill(False)
                user1.change_passion(False)
                user1.change_fame(False)
                user1.change_charisma(False)
                user1.change_charm(False)
            broadcast_room.change_room_status()
            room_transition(dining_hall, None, broadcast_room, Dining_Hall, None)
        print('You have been here before')
    print('You do not have the key to this room')
    room_transition(dining_hall, None, broadcast_room, Dining_Hall, None)


def Shooting_Range():
    if shooting_range.room_visited:
        user1.change_skill(False)
    print("[Guard]: Welcome to the shooting range")
    print("The guard at the shooting range seems bored, he has decided to play a game with you")
    print('Since he despises the soldier in charge of the dining hall because he bullies everyone the guard '
          'decides to share vital information about him, the twist being the higher the score you get the more'
          ' information he dispels')
    time.sleep(5)
    time_limit = 60
    if user1.skill < 0:
        time_limit = 45
    elif user1.skill > 2:
        time_limit = 75
    score = aimTrainer(time_limit)
    print('Your score is:', score)
    time.sleep(1)
    if score == 69:
        print('[Guard]: Nice')
        print('[Guard]: Private Sawcon always has the key to the broad cast room in his pocket')
        user1.skill += 2
    elif score > 100:
        print('[Guard]: Officer you are cracked')
        print('[Guard]: Private Sawcon is really obsessed with his body, if you want to woo him mention his body')
        print('[Guard]: Private Sawcon has always been scared of guns')
        print('[Guard]: Private Sawcon always has the key to the broad cast room in his pocket')
        user1.skill += 3
    elif score > 75:
        print('[Guard]: You are quite the sharpshooter, but always remember switching to your pistol is '
              'faster than reloading')
        print('[Guard]: Private Sawcon has always been scared of guns')
        print('[Guard]: Private Sawcon always has the key to the broad cast room in his pocket')
        user1.skill += 2
    elif score > 60:
        print('[Guard]: Well done officer, looks like you are still in form to go the battlefield')
        print('[Guard]: Private Sawcon always has the key to the broad cast room in his pocket')
        user1.skill += 1

    else:
        print('[Guard]: Officer your performance has been subpar to the standards I recommend coming back in a'
              ' few hours, I have no information to give you due to such abysmal performance')
    room_transition(generals_room, None, shooting_range, Generals_Room, None)


def bonaparte_escape():
    print('lesgo')


def jew_path():
    print('u are a jew')


user_setup()
intro()
main()
print('Game over')
