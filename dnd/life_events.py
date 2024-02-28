from dnd.event_type import LifeEventType
from dnd.character_class import Character

class LifeEvent:
    
    def __init__(self, age):
        self.age = age       
        
    @staticmethod
    def create_event(gender=None, race='Human', age=None, job=None, biological=True):
        # race = Player.race
        event_type = LifeEventType.random()
        match event_type:
            case LifeEventType.FORTUNE:
                print(f'rolled fortune {event_type}')
            case LifeEventType.MISFORTUNE:
                print(f'rolled misfortune {event_type}')
            case LifeEventType.ALLY: 
                print(f'rolled ally {event_type}')
            case LifeEventType.ENEMY: 
                print(f'rolled enemy {event_type}')
            case LifeEventType.ROMANCE:
                print(f'rolled romance {event_type}')

# LifeEvent.create_event()