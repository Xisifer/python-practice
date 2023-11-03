from char_creation_menus import *

<<<<<<< HEAD
=======

>>>>>>> d2dd8ba138b78c6065bd45583648c624f1cbf8b4
def roll(dictionary):
    # When provided with a dictionary consisting of Keys as strings adn Values as probabilities-out-of-100, roll according to probabilities and output the result.
    rolled = random.choices(list(dictionary.keys()), weights=dictionary.values(), k=1)
    rolled_string = rolled[0] # just the string of the result

    dict_items = list(dictionary.items())
    rolled_index = [id for id, key in enumerate(dict_items) if key[0] == rolled_string] # index of the result, used for conditionally targeting specific table results 
    # [ex. favorite drink; if you roll Milk, stop; if you roll Soda, ask what kind]

    # pack both string and index into a tuple for export
    return (rolled_string, rolled_index[0])

def roll_race(stuff):
    # from char_creation_menus import races
    race_result = roll(races)
    return race_result

def roll_homeland(race_result):
    match race_result:
        case 'Human' | 'Dwarf':
            char_home = roll(human_homes)
<<<<<<< HEAD
            # print(f'returning:  {char_home}')
=======
>>>>>>> d2dd8ba138b78c6065bd45583648c624f1cbf8b4
            return char_home

        case 'Elf' | 'Halfling' | 'Gnome':
            char_home = roll(fey_homes)
<<<<<<< HEAD
            # print(f'returning:  {char_home}')
=======
>>>>>>> d2dd8ba138b78c6065bd45583648c624f1cbf8b4
            return char_home
        
        case 'Dragonborn' | 'Orc' | 'Goblin' | 'Kobold' | 'Gnoll':
            char_home = roll(savage_homes)
<<<<<<< HEAD
            # print(f'returning:  {char_home}')
=======
>>>>>>> d2dd8ba138b78c6065bd45583648c624f1cbf8b4
            return char_home
        case _:
            print('ERROR: Race not valid!')

def roll_origin(race_result):
    
<<<<<<< HEAD

    match race_result:
        case 'Human' | 'Dwarf':

            char_origin = roll(human_origins)
            print(char_origin[0])
=======
    print(f'Inside roll_origin, the inserted race_result data is: {race_result}')
    # Incoming race_result is a tuple, for some reason. Converting it to a string so it can be interpreted
    char_home = race_result[1]
    race_result = race_result[0]

    # print('Character is what?')
    
    match race_result:
        case 'Human' | 'Dwarf':
            # print('Result: Human or Dwarf.')
            char_origin = roll(human_origins)
            # print(char_origin)
>>>>>>> d2dd8ba138b78c6065bd45583648c624f1cbf8b4
            origin_flavor = roll(urban_flavor)
            print(origin_flavor[0])
            return char_origin

        case 'Elf' | 'Halfling' | 'Gnome':
<<<<<<< HEAD

            char_origin = roll(fey_origins)
            print(char_origin[0])
            origin_flavor = roll(wild_flavor)
=======
            # print('Result: Elf, Halfling or Gnome.')
            char_origin = roll(fey_origins)
            # print('Result of roll(fey_origins) is:')
            # print(char_origin)
            origin_flavor = roll(wild_flavor)
            # print('Result of roll(wild_flavor) is:')
>>>>>>> d2dd8ba138b78c6065bd45583648c624f1cbf8b4
            print(origin_flavor[0])
            return char_origin
        
        case 'Dragonborn' | 'Orc' | 'Goblin' | 'Kobold' | 'Gnoll':
<<<<<<< HEAD

            char_origin = roll(savage_origins)
            print(char_origin[0])
=======
            # print('Result: Dragonborn, Orc, Goblin, Kobold or Gnoll.')
            char_origin = roll(savage_origins)
>>>>>>> d2dd8ba138b78c6065bd45583648c624f1cbf8b4
            origin_flavor = roll(savage_flavor)
            print(origin_flavor[0])
            return char_origin

def roll_family_fate(race_result):
<<<<<<< HEAD


    char_family_status = roll(family_status)
    char_family_status_index = char_family_status[1]
=======
    print(f'Inside roll_family_fate(), race_result is: {race_result}')

    char_family_status = roll(family_status)
    print(f'Result of roll(family_status) is: {char_family_status}')
    char_family_status_index = char_family_status[1]
    
    print(f'char_family_status_index is: {char_family_status_index}')
>>>>>>> d2dd8ba138b78c6065bd45583648c624f1cbf8b4
    if char_family_status_index == 0:
        print('Your family is alive and well.')
        return char_family_status
    else:
        print('Something happened to your family.')
<<<<<<< HEAD
        print(f'Your race is: {race_result}')
=======
        print(f'Checking race_result {race_result}...')
>>>>>>> d2dd8ba138b78c6065bd45583648c624f1cbf8b4
        match race_result:
            case 'Human' | 'Dwarf':

                char_family_fate = roll(family_fate_human)
<<<<<<< HEAD
                print(f'returning char_family_fate as: {char_family_fate}')
=======
>>>>>>> d2dd8ba138b78c6065bd45583648c624f1cbf8b4
                return char_family_fate

            case 'Elf' | 'Halfling' | 'Gnome':

                char_family_fate = roll(family_fate_fey)
                return char_family_fate
            
            case 'Dragonborn' | 'Orc' | 'Goblin' | 'Kobold' | 'Gnoll':

                char_family_fate = roll(family_fate_savage)
                return char_family_fate

<<<<<<< HEAD
def roll_parents(char_race):
=======
def roll_parents(race_result):
>>>>>>> d2dd8ba138b78c6065bd45583648c624f1cbf8b4

    char_parents_status = roll(parents_status)
    char_parents_status_index = char_parents_status[1]

    if char_parents_status_index == 0:
        return char_parents_status
    else:
        char_parents_fate = roll(parents_fate)
<<<<<<< HEAD
        print(char_parents_fate)
        char_parents_fate_index = char_parents_fate[1]
        if char_parents_fate_index == 0:
            char_father_fate = roll(father_fate)
            print(char_father_fate)
            return char_father_fate
        else:
            char_mother_fate = roll(mother_fate)
            print(char_mother_fate)
            return char_mother_fate

# def roll_family_events():
    

def roll_life_events(race_result, char_age, life_milestones):
    # print('Expecting an incoming tuple. Need 3 pieces of data.')

    from char_creator import ask_reroll

    life_events_num = len(life_milestones)

    def roll_event(life_age): 
        print(f'At age {life_age}...')
        
        
        # print(f'You rolled: {event_category} with ID {event_category_index}')

        retry = True
        while retry :
            question_text = f'At age {life_age}...'
            event_category = roll(life_event)
            event_category_index = event_category[1]
            event_category_result = event_category[0]
            retry = ask_reroll(question_text, event_category_result) 
        if event_category_index == 0: # Fortune or Misfortune
            # print('Fortune or Misfortune...')
            # even_odd = flip()

            retry = True
            while retry :
                question_text = 'Fortune or Misfortune? '
                even_odd = roll(fortune_misfortune)
                even_odd_result = even_odd[0]
                even_odd_index = even_odd[1]
                retry = ask_reroll(question_text, even_odd_result) 


            if even_odd_index == 0: #Fortune
                retry = True
                while retry :
                    question_text = 'You had a Fortunate event: '
                    fortune_tuple = roll(fortunes)
                    fortune_result = fortune_tuple[0]
                    fortune_index = fortune_tuple[1]
                    retry = ask_reroll(question_text, fortune_result) 
            else: # Misfortune
                retry = True
                while retry :
                    question_text = 'You sufered Misfortune: '
                    misfortune_tuple = roll(misfortunes)
                    misfortune_result = misfortune_tuple[0]
                    misfortune_index = misfortune_tuple[1]
                    retry = ask_reroll(question_text, misfortune_result) 


        elif event_category_index == 1: # Allies and Enemies
            print('Allies and Enemies')
            retry = True
            while retry :
                question_text = 'You made an Ally? Or an Enemy? '
                even_odd = roll(allegiance)
                even_odd_result = even_odd[0]
                even_odd_index = even_odd[1]
                retry = ask_reroll(question_text, even_odd_result) 
            if even_odd_index == 0: #Ally
                retry = True
                while retry :
                    question_text = 'You made an Ally: '

                    ally_gender = roll(gender)
                    complete_ally = roll_ally(ally_gender)
                    print(f'complete_ally is: {complete_ally}')
                    ally_summary = f'You met a {ally_gender[0]} {complete_ally[1]}, and {complete_ally[2]}. \nYou became {complete_ally[3]} for many years. \nEventually you parted ways in {complete_ally[4]}. \nToday, {complete_ally[5]}.'
                    # complete_ally = [
                    #     al_gender,
                    #     al_position,
                    #     al_meeting,
                    #     al_relationship,
                    #     al_location,
                    #     al_fate
                    # ]
                    print(ally_summary)
                    retry = ask_reroll(question_text, 'Accept?') 
            else: # Enemy
                retry = True
                while retry :
                    question_text = 'You made an Enemy: '
                    misfortune_tuple = roll(misfortunes)
                    misfortune_result = misfortune_tuple[0]
                    misfortune_index = misfortune_tuple[1]
                    retry = ask_reroll(question_text, misfortune_result) 
        else: #Romance
            print('Romance')
    print(f'You have had {life_events_num} events.')

    for life_age in life_milestones:
        roll_event(life_age)
=======
        # print(char_parents_fate)
        char_parents_fate_index = char_parents_fate[1]
        if char_parents_fate_index == 0:
            char_father_fate = roll(father_fate)
            # print(char_father_fate)
            return char_father_fate
        else:
            char_mother_fate = roll(mother_fate)
            # print(char_mother_fate)
            return char_mother_fate


def roll_life_events(life_event_data):
    print('Expecting an incoming tuple. Need 3 pieces of data.')
    print(f'Incoming data is: {life_event_data}')
    race_result = life_event_data[0]
    char_age = life_event_data[1]
    life_milestones = life_event_data[2]

    life_events_num = len(life_milestones)

# def roll_event(life_age): 
        

    event = roll(life_event)
    
    # retry = True
    # while retry :
    #     question_text = f'At age {life_age}...'
    #     event_category = roll(life_event)
        # event_category_index = event_category[1]
        # event_category_result = event_category[0]
    #     retry = ask_reroll(question_text, event_category_result) 
    # if event_category_index == 0: # Fortune or Misfortune
        # print('Fortune or Misfortune...')
        # even_odd = flip()
def roll_fortune():
    retry = True
    while retry :
        question_text = 'Fortune or Misfortune? '
        even_odd = roll(fortune_misfortune)
        even_odd_result = even_odd[0]
        even_odd_index = even_odd[1]
        retry = ask_reroll(question_text, even_odd_result) 


    if even_odd_index == 0: #Fortune
        retry = True
        while retry :
            question_text = 'You had a Fortunate event: '
            fortune_tuple = roll(fortunes)
            fortune_result = fortune_tuple[0]
            fortune_index = fortune_tuple[1]
            retry = ask_reroll(question_text, fortune_result) 
    else: # Misfortune
        retry = True
        while retry :
            question_text = 'You sufered Misfortune: '
            misfortune_tuple = roll(misfortunes)
            misfortune_result = misfortune_tuple[0]
            misfortune_index = misfortune_tuple[1]
            retry = ask_reroll(question_text, misfortune_result) 

def roll_npc: 
    # elif event_category_index == 1: # Allies and Enemies
    print('Allies and Enemies')
    retry = True
    while retry :
        question_text = 'You made an Ally? Or an Enemy? '
        even_odd = roll(allegiance)
        even_odd_result = even_odd[0]
        even_odd_index = even_odd[1]
        retry = ask_reroll(question_text, even_odd_result) 
    if even_odd_index == 0: #Ally
        retry = True
        while retry :
            question_text = 'You made an Ally: '

            ally_gender = roll(gender)
            complete_ally = roll_ally(ally_gender)
            print(f'complete_ally is: {complete_ally}')
            ally_summary = f'You met a {ally_gender[0]} {complete_ally[1]}, and {complete_ally[2]}. \nYou became {complete_ally[3]} for many years. \nEventually you parted ways in {complete_ally[4]}. \nToday, {complete_ally[5]}.'
            # complete_ally = [
            #     al_gender,
            #     al_position,
            #     al_meeting,
            #     al_relationship,
            #     al_location,
            #     al_fate
            # ]
            print(ally_summary)
            retry = ask_reroll(question_text, 'Accept?') 
    else: # Enemy
        retry = True
        while retry :
            question_text = 'You made an Enemy: '
            misfortune_tuple = roll(misfortunes)
            misfortune_result = misfortune_tuple[0]
            misfortune_index = misfortune_tuple[1]
            retry = ask_reroll(question_text, misfortune_result) 

def roll_romance: 
    print('Romance')
    print(f'You have had {life_events_num} events.')

for life_age in life_milestones:
roll_event(life_age)
>>>>>>> d2dd8ba138b78c6065bd45583648c624f1cbf8b4

