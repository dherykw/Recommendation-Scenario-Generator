import random

from objects.models import Object
from users.models import SceneUser, GENDER_CHOICES


class ModelGenerator:
    def __init__(self, number_of_users=1, ):
        super().__init__()
        self.number_of_user = number_of_users
        self.user = None

    def add_user(self, name, gender, age):
        self.user = SceneUser.objects.create(name=name, gender=gender, age=age)
        return self.user

    def generate_random_user(self):
        random_gender = GENDER_CHOICES.Male if random.randrange(2) % 2 == 0 else GENDER_CHOICES.Female
        random_age = random.randrange(18, 60)

        return SceneUser.objects.create(
            name='Random User',
            gender=random_gender,
            age=random_age
        )

    def generate_objects(self, qty, min_value=10000):
        max_value = min_value + qty
        Object.objects.all().delete()

        for object_id in range(min_value, max_value):
            print("Generated Object {}".format(object_id))
            object = Object.objects.create(id=object_id, name="Object {}".format(object_id))
            object.set_categories()
