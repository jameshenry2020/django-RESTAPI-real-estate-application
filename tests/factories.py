
from unicodedata import category
import factory
from apps.profiles.models import HostAgent, Profile
from django.db.models.signals import post_save
from faker import Factory as FakerFactory
from real_estate.settings import AUTH_USER_MODEL


faker = FakerFactory.create()


@factory.django.mute_signals(post_save)
class ProfileFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory("tests.factories.UserFactory")
    about_me = factory.LazyAttribute(lambda x: faker.sentence)
    profile_img = factory.LazyAttribute(lambda x: faker.file_extension(category="image"))
    gender = factory.LazyAttribute(lambda x: f"Male")
    country = factory.LazyAttribute(lambda x: faker.country_code())
    city = factory.LazyAttribute(lambda x: faker.city())
    is_agent = False


    class Meta:
        model = Profile




User = AUTH_USER_MODEL

@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.LazyAttribute(lambda x: faker.first_name())
    last_name = factory.LazyAttribute(lambda x: faker.last_name())
    phone = factory.LazyAttribute(lambda x: faker.phone_number())
    email = factory.LazyAttribute(lambda x: f"henry@realestate.com")
    password = factory.LazyAttribute(lambda x: faker.password())
    is_active = True
    is_staff = False
    

    class Meta:
        model = User

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        if "is_superuser" in kwargs:
            return manager.create_superuser(*args, **kwargs)
        else:
            return manager.create_user(*args, **kwargs)



class HostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = HostAgent

    brand_name = factory.Sequence(lambda n: faker.name())
    profile = factory.SubFactory(ProfileFactory)
    license = factory.LazyAttribute(lambda n: faker.text(max_nb_chars=8))
    office_address = factory.LazyAttribute(lambda n: faker.address())
    num_of_reviews = factory.LazyAttribute(lambda n: faker.random_int(min=1, max=25))
