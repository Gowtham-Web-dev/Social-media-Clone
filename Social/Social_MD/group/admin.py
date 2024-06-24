from django.contrib import admin
from group.models import Group,GroupMember

# Register your models here.

class GroupMenberInline(admin.TabularInline):

    model=GroupMember

admin.site.register(GroupMember)
admin.site.register(Group)
