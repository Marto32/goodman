"""
All exercise files
"""
from bin import exceptions


class Exercise(object):
    """The abstract object that defines the universal exercise interface.
    """

    def __init__(self, name, url):
        """Constructs an Exercise object with a name and url.

        Args:
            name: `string` The name of the exercise.
            url: `string` A url to a video of the exercise.
        Raises:
            MalformedArgument exception.
        """
        self._name = name
        self._url = url

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
    def url(self):
        """Getter for the url property."""
        return self._url

    @url.setter
    def url(self, url):
        """Setter for the url property."""
        if not isinstance(url, str):
            raise exceptions.MalformedArgument("url must be of type string. Got {}".format(type(url)))
        self._url = url

    def as_html(self):
        """Formats the exercise as an html link."""
        return '<a href="{url}">{name}</a>'.format(url=self.url, name=self.name)

    def __repr__(self):
        return '{_name}(name={name},url={url})'.format(
            _name=__name__,
            url=self.url,
            name=self.name
        )

    def __str__(self):
        return self.as_html()


# Exercise Definitions
BenchPress = Exercise(
    "Bench Press",
    "https://www.youtube.com/watch?v=UaOwz6DNdjw")

BarbellFloorPress = Exercise(
    "Barbell floor press",
    "https://www.youtube.com/watch?v=9vYCwtHkWgI")

InclineBarbellBenchPress = Exercise(
    "Incline barbell bench press (regular grip or close grip)",
    "https://www.youtube.com/watch?v=11gY7Q5D5wo")

WeightedChinUps = Exercise(
    "Weighted chin-ups",
    "https://www.youtube.com/watch?v=7FiR9W_gVF0")

FlatDBBenchPress = Exercise(
    "Flat DB bench press (palms in or out)",
    "https://www.youtube.com/watch?v=omGiL5h2R_I")

InclineDBBenchPress = Exercise(
    "Incline DB bench press (palms in or out)",
    "https://www.youtube.com/watch?v=0G2_XV7slIg")

DBFloorPress = Exercise(
    "DB floor press (palms in)",
    "https://www.youtube.com/watch?v=A2dfGvoykPc")

DBRows = Exercise(
    "DB rows",
    "https://www.youtube.com/watch?v=PgpQ4-jHiq4")

BarbellRows = Exercise(
    "Barbell rows",
    "https://www.youtube.com/watch?v=I-qgwlP0J90")

SeatedCableRows = Exercise(
    "Seated cable rows (various bars)",
    "https://www.youtube.com/watch?v=a8qvJ2VDd9g")

TBarRows = Exercise(
    "T-bar rows",
    "https://www.youtube.com/watch?v=KDEl3AmZbVE")

ChestSupportedRows = Exercise(
    "Chest supported rows",
    "https://www.youtube.com/watch?v=H75im9fAUMc")

RearDeltFlyes = Exercise(
    "Rear delt flyes",
    "https://www.youtube.com/watch?v=0GSu6Z-Oj7U")

Scarecrows = Exercise(
    "Scarecrows",
    "https://www.youtube.com/watch?v=YakiNOaMMAA")

FacePulls = Exercise(
    "Face pulls",
    "https://www.youtube.com/watch?v=rep-qVOkqgk")

SeatedDBPowerCleans = Exercise(
    "Seated DB 'power cleans'",
    "https://www.youtube.com/watch?v=kvVEz-tBgvg")

BandPullAparts = Exercise(
    "Band pull-aparts",
    "https://www.youtube.com/watch?v=fo3ogdhMFLo")

DBShrugs = Exercise(
    "DB shrugs",
    "https://www.youtube.com/watch?v=g6qbq4Lf1FI")

BarbellShrugs = Exercise(
    "Barbell shrugs",
    "https://www.youtube.com/watch?v=NAqCVe2mwzM")

BarbellCurls = Exercise(
    "Barbell curls (regular or thick bar)",
    "https://www.youtube.com/watch?v=kwG2ipFRgfo")

StandingDBCurls = Exercise(
    "DB curls (standing)",
    "https://www.youtube.com/watch?v=av7-8igSXTs")

SeatedInclineDBCurls = Exercise(
    "Seated incline DB curls",
    "https://www.youtube.com/watch?v=soxrZlIl35U")

HammerCurls = Exercise(
    "Hammer curls",
    "https://www.youtube.com/watch?v=TwD-YGVP4Bk")

ZottmanCurls = Exercise(
    "Zottmann curls",
    "https://www.youtube.com/watch?v=FSGDM9-dZ9w")

IsoHoldDBCurls = Exercise(
    "Iso-hold DB curls",
    "https://www.youtube.com/watch?v=ooXEcYEdyGo")
