from django.contrib import admin
from to_do_list_App.models import *

class custom_user_display(admin.ModelAdmin):
    list_display=['username','city','user_type']

    search_fields=['username','city','user_type']

    fieldsets=[
        (
            'Users list',
            {
                'fields':['username','email','password']
            }

        ),

        (
            'Advanced Option',
            {
                'classes':['collapse'],
                'fields':['first_name','last_name','city','profile_picture','user_type']
            }
        ),
    ]


    
admin.site.register(custom_user,custom_user_display)
admin.site.register(category_model)
admin.site.register(task_model)
    



