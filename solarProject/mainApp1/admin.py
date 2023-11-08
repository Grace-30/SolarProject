from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import UserInput2, UserInput , ElectronicDetail

admin.site.register(UserInput2)
admin.site.register(UserInput)
admin.site.register(ElectronicDetail)
class UserInput2Inline(admin.StackedInline):
     model = UserInput2
     can_delete = False





