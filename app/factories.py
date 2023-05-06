import factory
from factory.fuzzy import FuzzyText, FuzzyChoice
from factory.faker import Faker

from app.models import GenderEnum


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'app.Student'

    """ Static data """
    name = "Zomor"
    gender = GenderEnum.MALE.value

    """ Sequence text """
    # name = factory.Sequence(lambda n: "student{}".format(n))

    """ Fuzzy text """
    # name = FuzzyText(length=10).fuzz()

    """ Faker """
    # name = Faker._get_faker().name()

    """ CHOICES """
    """ FUZZY CHOICE """
    # gender = FuzzyChoice(choices=GenderEnum.choices(), getter=lambda c: c[1]).fuzz()


"""
    Contains Foreign key relationship
"""
class MobileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'app.Mobile'

    student = factory.SubFactory(StudentFactory)
    mobile = Faker._get_faker().msisdn()


"""
    Contains Many to Many relationship
"""
class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'app.Course'

    name = Faker._get_faker().name()

    @factory.post_generation
    def students(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing.
            return

        # Add the iterable of groups using bulk addition
        self.students.add(*extracted)
