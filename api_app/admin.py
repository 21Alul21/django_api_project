from django.contrib import admin

# # Register your models here.
from .models import User



from django.contrib.auth.admin import UserAdmin

class CustomAdmin(UserAdmin):

    model = User
    ordering = ('email',)  
    
    
    list_display = ('email', 'firstName', 'lastName', 'is_staff', 'is_active')

    search_fields = ('email', 'firstName', 'lastName')
    list_filter = ('is_staff', 'is_active')


admin.site.register(User, CustomAdmin)