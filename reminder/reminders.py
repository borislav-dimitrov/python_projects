from messages import Reminder


REMINDERS: list[Reminder] = [
    Reminder(message='Pose Check!', seconds= 60 * 10),
    Reminder(message='Do Sports!', seconds= 60 * 30),
]