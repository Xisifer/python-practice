

class LifeEvent:
    def __init__(self, age):
        self.age = age       
        self.event_type = LifeEventType.random()
        match self.self.event_type:
            case LifeEventType.FORTUNE:
                print(f'rolled fortune {self.event_type}')
            case LifeEventType.MISFORTUNE:
                print(f'rolled misfortune {self.event_type}')
            case LifeEventType.ALLY: 
                print(f'rolled ally {self.event_type}')
            case LifeEventType.ENEMY: 
                print(f'rolled enemy {self.event_type}')
            case LifeEventType.ROMANCE:
                print(f'rolled romance {self.event_type}')

