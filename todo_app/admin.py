from django.contrib import admin

# Register your models here.
from todo_app.models import Todo, Name

admin.site.register(Todo)
admin.site.register(Name)
