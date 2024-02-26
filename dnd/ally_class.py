
class Ally(NPC):
    def __init__(self, job=None): 
        super().__init__()
        if not job:
            self.job = AllyJob.random()
        else:
            self.job = job



        # print(f'before match: Ally is {self.gender}')
        match self.gender:
            case Gender.MALE: 
                # print(f'in match male: Ally is {self.gender}')
                self.he_she = 'he'
                self.him_her = 'him'
                self.his_hers = 'his'
                self.is_are = 'is'
            case Gender.FEMALE:
                # print(f'in match female: Ally is {self.gender}')
                self.he_she = 'she'
                self.him_her = 'her'
                self.his_hers = 'hers'
                self.is_are = 'is'
            case Gender.NB:
                # print(f'in match NB: Ally is {gender}')
                self.he_she = 'they'
                self.him_her = 'them'
                self.his_hers = 'their'
                self.is_are = 'are'
        print('=====================')
        print(f'In your travels, you met {self.name}, a {self.gender} {self.job}.')


        self.meeting_circumstance = AllyMeeting.random()

        
        match self.meeting_circumstance:
            case AllyMeeting.SAVED_THEM:
                print(f'You saved {self.him_her} from something')
            case AllyMeeting.SAVED_YOU:
                print(f'{self.he_she} saved you from something'.capitalize())
            case AllyMeeting.TAVERN:
                print(f'You met {self.him_her} in a tavern and were drinking buddies')
            case AllyMeeting.ALLIES:
                print(f'You fought together against something')
            case AllyMeeting.TRAPPED:
                print(f'You were both trapped in a dangerous situation and had to cooperate to survive.')
            case AllyMeeting.TRAVELING:
                print(f'You met {self.him_her} while traveling.')
            case AllyMeeting.HIRED_THEM:
                print(f'You hired {self.him_her} to do something for you.')
            case AllyMeeting.HIRED_YOU:
                print(f'{self.he_she} hired you to do something for {self.him_her}'.capitalize())
            case AllyMeeting.ENEMIES:
                print(f'You fought against each other and came to mutual respect through battle. Decide with your GM who won the encounter.')
            case AllyMeeting.RELUCTANT_ALLY:
                print(f'You were once reluctantly forced to work together with {self.him_her} against a common foe.')


        print('Over the time, the two of you became..... ')
        self.friendship_level = AllyRelation.random()
        match self.friendship_level:
            case AllyRelation.ACQUAINTANCE:
                print('just casual acquaintances')
            case AllyRelation.FRIEND:
                print('Friends')
            case AllyRelation.CLOSE_FRIEND:
                print('Close friends')
            case AllyRelation.INSEPERABLE:
                print('Totally inseperable')
            case AllyRelation.SWORN:
                print('Sworn blood bond companions')
        
        print(f'Today, {self.he_she} lives in...')
        self.location = AllyLocation.random()
        match self.location:
            case AllyLocation.TOWN:
                print(f'a nearby town')
            case AllyLocation.CAPITOL:
                print(f'the country\'s grand capitol')
            case AllyLocation.VILLAGE:
                print(f'a peaceful village in the countryside')
            case AllyLocation.HUT:
                print(f'a small hut in the middle of nowhere')
        print('=====================')

