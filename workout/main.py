import os
import datetime


PLAN = {
    0: {
        'type': 'abs + legs',
        'workout1': 'https://www.youtube.com/watch?v=D0K-U0pFj4k',
        'workout2': 'https://www.youtube.com/watch?v=841gJUczmzg'
        },
    1: {
        'type': 'abs + chest',
        'workout1': 'https://www.youtube.com/watch?v=D0K-U0pFj4k',
        'workout2': 'https://www.youtube.com/watch?v=0Av02v-gMw8'
        },
    2: {
        'type': 'abs + handstand',
        'workout1': 'https://www.youtube.com/watch?v=D0K-U0pFj4k',
        'workout2': 'hand stand hold, hand stand scissors'
        },
    3: {
        'type': 'abs + arms',
        'workout1': 'https://www.youtube.com/watch?v=D0K-U0pFj4k',
        'workout2': 'https://www.youtube.com/watch?v=JyV7mUFSpXs'
        },
    4: {
        'type': 'abs + chest',
        'workout1': 'https://www.youtube.com/watch?v=D0K-U0pFj4k',
        'workout2': 'https://www.youtube.com/watch?v=0Av02v-gMw8'
        },
    5: {
        'type': 'abs',
        'workout1': 'https://www.youtube.com/watch?v=D0K-U0pFj4k',
        'workout2': 'https://www.youtube.com/watch?v=D0K-U0pFj4k'
        },
    6: {
        'type': 'REST',
        'workout1': 'REST',
        'workout2': 'REST'
    }
}
OUTPUT_FILE = 'output.txt'


def write_output(workout_info):
    with open(OUTPUT_FILE, 'w') as fh:
        fh.write(workout_info)


def show_output():
    try:
        cmd = f'start "" {OUTPUT_FILE}'
        os.system(cmd)
    except Exception as ex:
        raise ex


def poll_workout():
    week_day = datetime.datetime.now().weekday()
    match week_day:
        case 0:
            workout ='Monday\n\n'
        case 1:
            workout ='Tuesday\n\n'
        case 2:
            workout ='Wednesday\n\n'
        case 3:
            workout ='Thursday\n\n'
        case 4:
            workout ='Friday\n\n'
        case 5:
            workout = 'Saturday\n\n'
        case 6:
            workout = 'Sunday\n\n'
        case _:
            raise RuntimeError('Invalid day of the week!')

    workout += f'Workout type: {PLAN[week_day]['type']:<20}\n'
    workout += f'Workout 1:    {PLAN[week_day]['workout1']:<20}\n'
    workout += f'Workout 2:    {PLAN[week_day]['workout2']:<20}\n'
    return workout


def main_func():
    workout = poll_workout()
    write_output(workout)
    show_output()


if __name__ == '__main__':
    main_func()