from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return "Category: {}".format(self.name)


class Object(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=75)
    categories = models.ManyToManyField(Category)

    def set_categories(self):
        self._set_pair_category()
        self._set_divisible_by_categories()

    def _set_pair_category(self):
        if self.id % 2 == 0:
            category, created = Category.objects.get_or_create(name="Even")
        else:
            category, created = Category.objects.get_or_create(name="Odd")

        self.categories.add(category)

    def _set_divisible_by_categories(self):
        divisible = False

        for num in range(2, self.id):
            if self.id % num == 0:
                divisible = True
                self.categories.add(Category.objects.get_or_create(name="Divisible By {}".format(num))[0])

        if divisible is False:
            self.categories.add(Category.objects.get_or_create(name="Prime")[0])

    def __str__(self):
        return "Object: {} with Categories: {}".format(self.name, self.categories.all())
