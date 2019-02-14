import argparse
import datetime

import workout
import yagmail

parser = argparse.ArgumentParser(description="CLI for the goodman workout application.")
parser.add_argument('--gmail_username', type=str, help="The senders gmail username.", required=True)
parser.add_argument('--gmail_password', type=str, help="The senders gmail password.", required=True)
parser.add_argument('--recipient', type=str, help="The recipients email address.", required=True)

SCHEDULE = {
    # Weekday index : Workout
    # Monday
    0: workout.MaxEffortUpperBody,

    # Tuesday
    1: workout.DynamicEffortLowerBody,

    # Thursday
    3: workout.RepetitionUpperBody,

    # Friday
    4: workout.MaxEffortLowerBody,
}


def should_workout(weekday_index):
    """Determines if there is a workout scheduled for the given day.

    Args:
        weekday_index: 'int' An index representing the weekday. See docs:
        https://docs.python.org/3/library/datetime.html#datetime.date.weekday
    Returns:
        True or False.
    """
    return weekday_index in SCHEDULE.keys()


def get_workout_for_day(weekday_index):
    """Obtains a workout for the given day.

    Args:
        weekday_index: 'int' An index representing the weekday. See docs:
        https://docs.python.org/3/library/datetime.html#datetime.date.weekday
    Returns:
        The `Workout` object for the given day.
    """
    return SCHEDULE[weekday_index]


if __name__ == '__main__':
    args = parser.parse_args()
    today = datetime.datetime.today().weekday()
    if should_workout(today):
        workout = get_workout_for_day(today)
        subject = "WORKOUT: {}".format(workout.name)

        yag = yagmail.SMTP(user=args.gmail_username, password=args.gmail_password)
        yag.send(args.recipient, subject, workout.as_html())


