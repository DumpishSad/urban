team1 = 'Мастера кода'
team2 = 'Волшебники данных'


def number_participants(team1_num, team2_num):
    print('В команде %s участников: %s!' % (team1, team1_num))
    print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))


score1 = 40
score2 = 42


def number_tasks(team2_time=0, tasks_total=0):
    print('Команда {} решила задач: {}!'.format(team2_time, score2))
    print('{} решили задачи за {} cек.!'.format(team2_time, team2_time))


def challenge_result(tasks_total=0, time_avg=0):
    print(f'Команды решили {score1} и {score2} задач')
    if score1 > score2:
        print(f'Результат битвы: победа команды {team1}!')
    else:
        print(f'Результат битвы: победа команды {team2}!')
    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу')


number_participants(5, 6)
number_tasks(1552.512, 2153.31451)
challenge_result(tasks_total=82, time_avg=45.2)