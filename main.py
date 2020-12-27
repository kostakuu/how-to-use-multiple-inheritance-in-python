from models import Human, Robot, Cyborg

if __name__ == '__main__':
    print('HUMAN'.center(100, '='))
    human = Human('Kosta', 'Kupresak')
    print(human.start_conversation())
    print(human.introduce_me())

    print('ROBOT'.center(100, '='))
    robot = Robot('F3R', 'SRB')
    print(robot.get_energy_level())
    print(robot.introduce_me())

    print('CYBORG'.center(100, '='))
    cyborg = Cyborg('Ana', 'Anic', '3FA', 'SRB', 'Flying')
    print(f'My code is {cyborg.code} and I am from {cyborg.origin}.')
    print(cyborg.start_conversation())
    print(f'My superpower is {cyborg.superpower}.')
    print(cyborg.introduce_me())

    print('METHOD RESOLUTION ORDER'.center(100, '='))
    humanoid_cyborg = Cyborg('Pera', 'Peric', '4MX', 'SRB', 'Replication')
    print(humanoid_cyborg.what_i_am_more())
