from django.db import models


class Name(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=20)
    text = models.TextField()

    def __str__(self):
        return f'This is {self.name}'


class Todo(models.Model):
    title = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f'This is  {self.title} todo'
