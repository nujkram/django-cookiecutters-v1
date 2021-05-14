import factory
from faker import Faker

from .models import {{ cookiecutter.model }} as Master

fake = Faker()


class {{ cookiecutter.model }}Factory(factory.DjangoModelFactory):
    class Meta:
        model = Master
    
    # Fields:
    name = factory.LazyAttribute(lambda x: fake.name())
