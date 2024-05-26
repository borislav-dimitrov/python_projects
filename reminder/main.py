import time
from reminders import REMINDERS


def check_show_message(time_passed: int) -> None:
    for message in REMINDERS:
        if time_passed - message.last_message_shown >= message.seconds:
            message.show(time_passed)


def announce_reminders() -> None:
    txt = 'Currently set reminders are:\n\n'
    for idx, message in enumerate(REMINDERS):
        txt += f'{idx}. Message: {message.message} // Remind every: {message.seconds / 60} minutes\n\n'

    print(f'{"=" * 30}\n{txt}\n{"=" * 30}')


def main_func() -> None:
    announce_reminders()
    running = True
    time_passed = 0

    while running:
        time_passed += 1

        check_show_message(time_passed)

        time.sleep(1)


if __name__ == '__main__':
    main_func()