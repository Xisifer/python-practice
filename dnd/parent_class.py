from dnd.character_class import Character
from dnd.race import Race
from dnd.jobs_menu import PlayerJob, NPCJob, AllyJob
from dnd.gender import Gender

from dnd.childhood import Birth


# Define the Parent class with a race property
class Parent(Character):
    def __init__(self, gender=None, race=None, job=None, kin=None, **kwargs):
        super().__init__()
        self.gender = gender

        # pc_childhood starts empty
        pc_childhood = ''
        print('Generating parents...')
        # By default, every character has a birth mother

        self.gender = Gender.FEMALE
        if kin:
            self.race = kin.race
        else: 
            self.race = Race.random()
        self.job = NPCJob.random()



        # Second parent defaults to Father, but this can change
        pc_parent2 = Parent()
        pc_parent2.gender = Gender.MALE
        pc_parent2.race = player_char.race
        pc_parent2.job = NPCJob.random()

        num_parents = 2

        player_char.bg_birth = Birth.random()
        
        match player_char.bg_birth:
            case Birth.ORPHAN:
                pc_childhood += 'You are an orphan.'
                pc_parent2=None
                pc_parent1=None
            case Birth.BORN:
                s = "s" if num_parents > 1 else ""
                pc_childhood += f"As a {player_char.race}, you were born to {num_parents} {player_char.race} parent{s}.\n"
                for parent in pc_parent1, pc_parent2:
                    if parent:
                        if parent.gender == Gender.FEMALE: 
                            pc_childhood += "Your mother is a {}.\n".format(parent.job)
                        elif parent.gender == Gender.MALE: 
                            pc_childhood += "Your father is a {}.\n".format(parent.job)
                        else:
                            pc_childhood += "Your non-binary parent is a {}.\n".format(parent.job)
            case Birth.ADOPTED:
                pc_parent2 = random.choice([None, pc_parent2])
                num_parents = bool(pc_parent1) + bool(pc_parent2)

                for parent in pc_parent1, pc_parent2:
                    if parent:
                        parent.race = Race.random()
                        parent.gender = Gender.random()

                s = "s" if num_parents > 1 else ""
                pc_childhood += "You are a {}, but you were adopted by {} parent{}.\n".format(player_char.race, num_parents, s)
                for parent in pc_parent1, pc_parent2:
                    if parent:
                        if parent.gender == Gender.FEMALE: 
                            pc_childhood += "Your mother is a {} {}.\n".format(parent.race,parent.job)
                        elif parent.gender == Gender.MALE: 
                            pc_childhood += "Your father is a {} {}.\n".format(parent.race,parent.job)
                        else:
                            pc_childhood += "Your parent is a non-binary {} {}.\n".format(parent.race,parent.job)
            case _:
                print ('This should never happen.')
    
        parents = []
        for parent in pc_parent1, pc_parent2:
            if parent:
                parents.append(parent)
        finished_childhood = pc_childhood
        print(finished_childhood)
        return finished_childhood, parents

# Example usage:
# Create a few Parent instances to demonstrate the randomness
# for _ in range(5):
#     parent = Parent()
#     print(f'Created a {parent.race} parent.')

