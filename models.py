import random


class Hello:
    def __init__(self, **kwargs):
        pass

    def introduce_me(self):
        return f'I am {self.__class__.__name__}.'


class Robot(Hello):
    def __init__(self, code, origin, **kwargs):
        super(Robot, self).__init__(**kwargs)
        self.code = code
        self.origin = origin

    def get_energy_level(self):
        return f'The energy level of #{self.code} is {random.randint(1, 100)}%'

    def what_i_am_more(self):
        return 'Robot!'


class Human(Hello):
    def __init__(self, first_name, last_name, **kwargs):
        super(Human, self).__init__(**kwargs)
        self.first_name = first_name
        self.last_name = last_name

    def start_conversation(self):
        return f'Hi, I am {self.first_name} {self.last_name}. How are you?'

    def what_i_am_more(self):
        return 'Human!'


class Cyborg(Robot, Human):
    def __init__(self, first_name, last_name, code, origin, superpower):
        super(Cyborg, self).__init__(first_name=first_name, last_name=last_name, code=code, origin=origin)
        self.superpower = superpower
