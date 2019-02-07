import routine

from bin import exceptions


class Workout(object):
    """An interface for a full workout. Typically this would be a full set of routines to do on a given day."""

    def __init__(self, name, routines):
        self._name = name
        self._routines = routines

    @property
    def name(self):
        """Getter for the name property."""
        return self._name

    @name.setter
    def name(self, name):
        """Setter for the name property."""
        if not isinstance(name, str):
            raise exceptions.MalformedArgument("name must be of type string. Got {}".format(type(name)))
        self._name = name

    @property
    def routines(self):
        """Getter for the routines property."""
        return self._routines

    @routines.setter
    def routines(self, routines):
        """Setter for the routines property."""
        if not isinstance(routines, list):
            raise exceptions.MalformedArgument("routines must be of type list. Got {}".format(type(routines)))
        self._routines = routines

    def as_html(self):
        """Helper method to format the routine as HTML.

        Returns:
            A `string` of HTML formatted workout routines."""
        html = """
            <p><b>{name}</b></p>
            <p>Don't forget to <a href="https://www.youtube.com/watch?v=qQ96oXp5RTU">warm up</a>!</p>
            <ul>
                {routines}
            </ul>
        """.format(
            name=self.name,
            routines=''.join([routine.as_html() for routine in self.routines]))

        return html

    def __str__(self):
        return self.as_html()


# WS4SB Workouts
MaxEffortUpperBody = Workout(
    name="Max-Effort Upper Body",
    routines=[
        routine.MaxEffortExercise,
        routine.SupplementalExercise,
        routine.RearDeltSuperset,
        routine.Traps,
        routine.ElbowFlexorExercise,
    ])

DynamicEffortLowerBody = Workout(
    name="Dynamic-Effort Lower Body",
    routines=[
        routine.JumpTraining,
        routine.UnilateralExercise,
        routine.HipExtensionExercise,
        routine.WeightedAbdominals,
    ])

RepetitionUpperBody = Workout(
    name="Repetition Upper Body",
    routines=[
        routine.RepetitionExercise,
        routine.VerticalPullingDeltSuperset,
        routine.MedialDelts,
        routine.TrapsArmsSuperset,
    ])

MaxEffortLowerBody = Workout(
    name="Max-Effort Lower Body",
    routines=[
        routine.MaxEffortLift,
        routine.UnilateralMovement,
        routine.HamstringMovement,
        routine.GroundBasedAbCricuit,
    ])
