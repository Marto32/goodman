import random

import exercise
from bin import exceptions


class ExerciseRoutine(object):
    """An interface to define exercise routines.

    Routines are descriptions / notes combined with a set of exercises. Typically,
    they will represent one group or part of a full workout.
    """
    def __init__(self):
        pass

    @property
    def name(self):
        raise NotImplementedError

    @property
    def description(self):
        raise NotImplementedError

    @property
    def exercises(self):
        raise NotImplementedError

    @property
    def n_exercises(self):
        return 1

    def get_exercises(self):
        """Randomly chooses and returns n exercises for the routine where n is self.n_exercises.

        Returns:
            A `list` of exercise objects.
        """
        exercises_for_routine = []
        for _ in range(self.n_exercises):
            exercises_for_routine.append(random.choice(self.exercises))

        return exercises_for_routine

    def as_html(self):
        """Formats the routine as a list element with a nested list of exercises."""
        exercises_formatted = ['<li>{exercise}</li>'.format(exercise=e) for e in self.get_exercises()]
        return """
            <li>{description}:
                <ul>
                    {exercises_formatted}
                </ul>
            </li>
            """.format(description=self.description.rstrip('.'),
                       exercises_formatted=''.join(exercises_formatted))

    def __str__(self):
        return self.as_html()


class SupersetRoutine(ExerciseRoutine):

    @property
    def exercises(self):
        raise exceptions.DeadProperty("exercises is not used in SupersetRoutine. Use exercise_groups instead.")

    @property
    def exercise_groups(self):
        """A list of lists containing exercises.

        Example: [[BenchPress, BarbellFloorPress], [FacePulls, Scarecrows]]"""
        raise NotImplementedError

    def get_exercises(self):
        """Randomly chooses exercises from the nested groups."""
        exercises_for_routine = []
        for exercise_group in self.exercise_groups:
            for _ in range(self.n_exercises):
                exercises_for_routine.append(random.choice(exercise_group))

        return exercises_for_routine


# Monday routines
class MaxEffortExercise(ExerciseRoutine):
    name = "Max-Effort Exercise"
    description = "Work up to a max set of 3-5 reps."
    exercises = [
        exercise.BenchPress,
        exercise.BarbellFloorPress,
        exercise.InclineBarbellBenchPress,
        exercise.WeightedChinUps,
    ]


class SupplementalExercise(ExerciseRoutine):
    name = "Supplemental Exercise"
    description = ("Perform 2 sets of max reps. Choose a weight you can perform 15-20 reps on the 1st set. "
                   "Use the same weight for both sets and rest 3-4 minutes in between.")
    exercises = [
        exercise.FlatDBBenchPress,
        exercise.InclineDBBenchPress,
        exercise.DBFloorPress,
    ]


class RearDeltSuperset(SupersetRoutine):
    name = "Horizontal pulling / Rear delt superset"
    description = "Superset! Perform 3-4 supersets of 8-12 reps of each exercise."
    exercise_groups = [
        [
            exercise.DBRows,
            exercise.BarbellRows,
            exercise.SeatedCableRows,
            exercise.TBarRows,
            exercise.ChestSupportedRows,
        ],
        [
            exercise.RearDeltFlyes,
            exercise.Scarecrows,
            exercise.FacePulls,
            exercise.SeatedDBPowerCleans,
            exercise.BandPullAparts,
        ]
    ]


class Traps(ExerciseRoutine):
    name = "Traps"
    description = "Perform 3-4 sets of 8-15 reps."
    exercises = [
        exercise.DBShrugs,
        exercise.BarbellShrugs,
    ]


class ElbowFlexorExercise(ExerciseRoutine):
    name = "Elbow flexor exercise"
    description = "Perform 3-4 sets of 8-15 reps."
    exercises = [
        exercise.BarbellCurls,
        exercise.StandingDBCurls,
        exercise.SeatedInclineDBCurls,
        exercise.HammerCurls,
        exercise.ZottmanCurls,
        exercise.IsoHoldDBCurls,
    ]
