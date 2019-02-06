import routine


class Workout(object):
    """An interface for a full workout. Typically this would be a full set of routines to do on a given day."""

    def __init__(self):
        pass

    @property
    def name(self):
        """The name of the workout."""
        raise NotImplementedError

    @property
    def routines(self):
        """A list of routines that comprise the workout."""
        raise NotImplementedError

    def as_html(self):
        """Helper method to format the routine as HTML.

        Returns:
            A `string` of HTML formatted workout routines."""
        html = """
            <p>{name}</p>
            <ul>
                {routines}
            </ul>
        """.format(
            name=self.name,
            routines=''.join([routine().as_html() for routine in self.routines]))

        return html

    def __str__(self):
        return self.as_html()


class MaxEffortUpperBody(Workout):
    name = "Max-Effort Upper Body"
    routines = [
        routine.MaxEffortExercise,
        routine.SupplementalExercise,
        routine.RearDeltSuperset,
        routine.Traps,
        routine.ElbowFlexorExercise,
    ]


class DynamicEffortLowerBody(Workout):
    name = "Dynamic-Effort Lower Body"
    routines = [
        routine.JumpTraining,
        routine.UnilateralExercise,
        routine.HipExtensionExercise,
        routine.WeightedAbdominals,
    ]


if __name__ == '__main__':
    print(DynamicEffortLowerBody())
