import random

# Class declarations


class weapon:
    damage = 0
    name = " "
    crit_range = 0


class char:
    weap = weapon()
    hp = 0
    dialogue = " "
    name = " "
    drop = 0
    chance = 0


# Character object
user = char()
user.hp = 65
user.dialogue = "Can't we just talk this out?"

# A class to house the char class. This allows functions to manipulate
# a larger object without needing the exact name of the enemy type passed in


class enemy:
    en = char()


# Weapon objects: player
Sword = weapon()
Sword.damage = 5
Sword.name = "Sword"
Sword.crit_range = 6

Axe = weapon()
Axe.damage = 9
Axe.name = "Axe"
Axe.crit_range = 12

Dagger = weapon()
Dagger.damage = 3
Dagger.name = "Dagger"
Dagger.crit_range = 4

# Weapon objects: enemy
Nibble = weapon()
Nibble.damage = 2
Nibble.name = "Nibble"
Nibble.crit_range = 20

Chomp = weapon()
Chomp.damage = 6
Chomp.name = "Chomp"
Chomp.crit_range = 10

Knife = weapon()
Knife.damage = 5
Knife.name = "Knife"
Knife.crit_range = 8

Slime_Spike = weapon()
Slime_Spike.damage = 10
Slime_Spike.name = "Slime Spike"
Slime_Spike.crit_range = 9

Club = weapon()
Club.damage = 9
Club.name = "Club"
Club.crit_range = 17

# Special droppable weapons

Slime_Sabre = weapon()
Slime_Sabre.damage = 17
Slime_Sabre.name = "Slime Sabre"
Slime_Sabre.crit_range = 6


# Enemy objects
Rat = char()
Rat.weap = Nibble
Rat.hp = 10
Rat.dialogue = "Rats cannot speak human languages"
Rat.name = "Rat"
Rat.drop = "NO"
Rat.intro = f""" 
                Lookout, a Rat has crawled into the ring!
                """

Giant_Rat = char()
Giant_Rat.weap = Chomp
Giant_Rat.hp = 25
Giant_Rat.dialogue = ""
Giant_Rat.name = "Giant Rat"
Giant_Rat.drop = "NO"
Giant_Rat.intro = f""" 

                Lookout, a Giant Rat has crawled into the ring!
                """

Bandit = char()
Bandit.weap = Knife
Bandit.hp = 18
Bandit.dialogue = "I'm gonna enjoy killin ya!"
Bandit.name = "Bandit"
Bandit.drop = 1
Bandit.chance = 5
Bandit.intro = f""" 
                Lookout, a dirty Bandit has leapt into the ring!
            """

Orc = char()
Orc.weap = Club
Orc.hp = 27
Orc.dialogue = "For the Horde!"
Orc.name = "Orc"
Orc.drop = 2
Orc.chance = 5
Orc.intro = f""" 
                Lookout, an Orc has stomped into the ring!
                """

Slime = char()
Slime.weap = Slime_Spike
Slime.hp = 20
Slime.dialogue = "The slime changed shape to look like you...not cool!"
Slime.name = "Slime"
Slime.drop = 3
Slime.chance = 1
Slime.intro = f""" 

                Lookout, a gellatenous Slime has oozed into the ring!
"""
# Initializing values
game_on = 1
battle_on = 1
opponent = enemy()
temp = char()
opponent.en = temp
opponent.en.hp = 0
battle_menu = """

****Battle Time****
1. Attack
2. Talk it Out
"""
en_alive = 1
u_alive = 1
damage_counter = 0
en_counter = 0
user_heal = 15

# Function declarations
# This function takes in damage and hp values to calculate and return battle damage, as well as a crit
# range to determine critical hits


def deal_damage(damage, hp, crit):

    # Adding a random number between -1 and 1 adds some damage variation
    var = random.randint(-2, 3)
    damage += var
    # Determine if attack was critical with passed in crit info
    critical = random.randint(0, crit+1)
    if critical == crit:
        damage *= 2
    if critical == crit:
        print("A critical hit!")

    return damage

# This function takes in a weapon id and a drop chance from the current enemy object, and uses those values
# to determine if the user should be presented with the option of picking up a new weapon or not.
# The Slime drops a pretty cool on ;)


def weap_drop(weap_id, drop_chance):

    weap_drop = random.randint(0, drop_chance+1)
    if weap_drop == drop_chance:
        temp_weap = weapon()
        if weap_id == 1:
            temp_weap.name = Knife.name
        if weap_id == 2:
            temp_weap.name = Club.name
        if weap_id == 3:
            temp_weap.name = Slime_Sabre.name
        choice = input(f""" 
        Hey, it looks like that {opponent.en.name} dropped a {temp_weap.name}.
        Would you like to pick it up?
        1. Yes
        2. No
        : 
        """)
        while choice != "1" and choice != "2":
            choice = input("""
            This is no time for funny business!
            Pick up the weapon or don't!
            : 
            """)
        if choice == "1":
            if weap_id == 1:
                user.weap = Knife
            if weap_id == 2:
                user.weap = Club
            if weap_id == 3:
                user.weap = Slime_Sabre
            print(f"You picked up the {user.weap.name}!")
        if choice == "2":
            print("Alright then, back to the fighting!")

    return 0


# This function takes in damage and hp values, prints out appropriate damage messaging,
# and returns a new hp value
def hp_check(damage, hp):
    new_hp = hp - damage
    x = f"{damage} damage was dealt!"
    y = "What precision! 0 HP left. "
# If the target is left standing
    if new_hp > 0:

        print(x)


# If hp after attack is 0
    if new_hp == 0:
        message = f"{x} {y}"
        print(message)
    if new_hp < 0:
        print(x)

    return new_hp


# This functions determines if the target is alive, and returns an appropriate value
def death_check(target):

    if target.hp <= 0:
        return -1
    if target.hp > 0:
        return 1


en_list = []
# Different Enemy Lists
list_1 = [Rat, Bandit, Orc]
list_2 = [Orc, Rat, Giant_Rat]
list_3 = [Rat, Bandit, Rat]
list_4 = [Bandit, Rat, Slime]
list_5 = [Rat, Giant_Rat, Giant_Rat]

# Main loop
while game_on == 1:
    # Reinstate health values at top level when game loop is restarted
    Rat.hp = 10
    Giant_Rat.hp = 25
    Bandit.hp = 18
    Orc.hp = 30
    Slime.hp = 20

    print("""Welcome to Battle World!
    Choose your weapon!
    Enter 1 for a Sword
    Enter 2 for an Axe
    Enter 3 for a Dagger
    """)

    choice = input(": ")
    while choice != "1" and choice != "2" and choice != "3":
        print(""" 
        Hm...I am not sure we have that weapon in stock...
        """)
        choice = input("""
        Please, choose your weapon!
        Enter 1 for a Sword
        Enter 2 for an Axe
        Enter 3 for a dagger
        : 
        """)
    if choice == "1":
        user.weap = Sword
    if choice == "2":
        user.weap = Axe
    if choice == "3":
        user.weap = Dagger

    p = f"{user.weap.name}, good choice. Let the fights begin!"
    print(p)

 # Determine initial enemy list
    rand_num = random.randint(1, 6)
    if rand_num == 1:
        en_list = list_1
    if rand_num == 2:
        en_list = list_2
    if rand_num == 3:
        en_list = list_3
    if rand_num == 4:
        en_list = list_4
    if rand_num == 5:
        en_list = list_5

# # Reinstate health values
#     Rat.hp = 10
#     Bandit.hp = 18
#     Orc.hp = 30
#     user.hp = 40

    battle_on = 1
    while battle_on == 1:
        opponent.en = en_list[en_counter]
        print(opponent.en.intro)
 # Start main battle loop
        while opponent.en.hp > 0 and u_alive == 1:
            print(battle_menu)
            # Read outs of enemy hps for debugging
            #print(f"{Rat.hp} {Bandit.hp} {Orc.hp}")
            print(f"HP Remaining: {user.hp}")
 # Check that the player is alive
            u_alive = death_check(user)
            if u_alive == 1:

                choice = input(": ")

                if choice == "1":
                    print(f"You attack with your {user.weap.name}: ")
                    damage_dealt = deal_damage(
                        user.weap.damage, opponent.en.hp, user.weap.crit_range)
                    opponent.en.hp = hp_check(damage_dealt, opponent.en.hp)
                    damage_counter += damage_dealt
 # Check if the enemy is alive or not after attack
                    en_alive = death_check(opponent.en)
                    if en_alive == 1:
                        print(
                            f"The {opponent.en.name} attacks with a {opponent.en.weap.name}:")
                        damage_dealth = deal_damage(
                            opponent.en.weap.damage, user.hp, opponent.en.weap.crit_range)
                        user.hp = hp_check(damage_dealt, user.hp)
                    if en_alive == -1:
                        print(f"The {opponent.en.name} falls! A clean kill!")

                        en_counter += 1
                        if opponent.en.drop != "NO":
                            weap_drop(opponent.en.drop, opponent.en.chance)
                        if en_counter <= 2:
                            if opponent.en.name == en_list[en_counter].name:
                                # Reinstate health values to allow multiple enemies of the same name to combat the player in one run
                                if opponent.en.name == "Rat":
                                    opponent.en.hp = 10
                                if opponent.en.name == "Giant Rat":
                                    opponent.en.hp = 25
                                if opponent.en.name == "Bandit":
                                    opponent.en.hp = 18
                                if opponent.en.name == "Orc":
                                    opponent.en.hp = 30
                                if opponent.en.name == "Slime":
                                    opponent.en.hp = 20
                            opponent.en = en_list[en_counter]
                            print(opponent.en.intro)

                if choice == "2":
                    print(user.dialogue)
                    en_dialogue = f"The {opponent.en.name} says: {opponent.en.dialogue}"
                    print(en_dialogue)
# If player is dead at the end of the combat, present appropriate options
        if u_alive == -1:
            print(f""" 
                
            You have been slain! A fine tribute to the Battle World!
            You dealt {damage_counter} damage. Not too shabby.
 
            """)
            choice = input("""
            Would you like another go?
            1. for yes
            2. for no
            : """)

            while choice != "1" and choice != "2":
                print("""
                Sorry, I can't understand your accent. 
                """)
                choice = input("""
            Would you like another go?
            1. for yes
            2. for no
            : """)
            if choice == "1":
                # Reset game values to make another run
                u_alive = 1
                en_alive = 1
                en_spawn = 1
                en_counter = 0
                damage_counter = 0
                battle_on = 0

            if choice == "2":
                choice = input("Goodbye")
                battle_on = 0
                en_alive = 0
                game_on = 0
# If enemy is dead at the end of combat, present appropriate options
        if en_alive == -1:
            print(f"""
            
            All enemies have been defeated!

            """)
            choice = input("""Would you like to fight another round?
            1. for yes
            2. for no
            : """)
            while choice != "1" and choice != "2":
                print("""
                Sorry, I can't understand your accent. 
                """)
                choice = input("""Would you like to fight another round?
            1. for yes
            2. for no
            : """)

            if choice == "1":
                u_alive = 1
                en_alive = 1
                en_spawn = 1
                en_counter = 0
                Rat.hp = 10
                Bandit.hp = 18
                Orc.hp = 30
                print(""" 
                Alright, lets get you patched up a bit.
                *Healing noises* *Healing noises*
                Back to the ring!
                """)
                # Heal the player in between successful rounds, and increase the amount the player is healed the next round
                user.hp += user_heal
                user_heal += 5
                # Select next enemy list
                rand_num = random.randint(1, 6)
                if rand_num == 1:
                    en_list = list_1
                if rand_num == 2:
                    en_list = list_2
                if rand_num == 3:
                    en_list = list_3
                if rand_num == 4:
                    en_list = list_4
                if rand_num == 5:
                    en_list = list_5
            if choice == "2":
                choice = input("Goodbye")
                battle_on = 0
                en_alive = 0
                game_on = 0
