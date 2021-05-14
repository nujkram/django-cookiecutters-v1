from faker import Faker
from django_test import TestCase


from {{ cookiecutter.app }}.models.{{ cookiecutter.module }}.models import {{ cookiecutter.model }} as Master
from {{ cookiecutter.app }}.models.{{ cookiecutter.module }}.factories import {{ cookiecutter.model }}Factory as MasterFactory

fake = Faker()


class {{ cookiecutter.model }}Test(TestCase):
    def test_create_{{ cookiecutter.module }}(self):
        obj = MasterFactory.create()

        self.assertTrue(
            isinstance(
                obj,
                Master
            ),
            f"{obj} is not of type {Master}"
        )