from django.contrib import admin
from .models import UserTable
#from .models import Profile
# Register your models here.

#admin.site.register()
class UserTableAdmin(admin.ModelAdmin):
    # Customize the admin view for UserTable, if needed
    list_display= ['username', 'neutral','happy', 'sad','angry','disgusted','surprised', 'fearful']

admin.site.register(UserTable, UserTableAdmin)