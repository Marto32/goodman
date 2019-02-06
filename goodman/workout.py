import routine


class Workout(object):

    def __init__(self):
        pass

    @property
    def name(self):
        raise NotImplementedError

    @property
    def routines(self):
        raise NotImplementedError

    def instantiate_routines(self):
        return ''.join([routine().as_html() for routine in self.routines])

    def as_html(self):
        html = """
            <p>{name}</p>
            <ul>
                {routines}
            </ul>
        """.format(
            name=self.name,
            routines=self.instantiate_routines())

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


if __name__ == '__main__':
    print(MaxEffortUpperBody())
