from django.contrib import admin
from .models import Post,Contact
# Register your models here.

admin.site.register(Post)
admin.site.register(Contact)



admin.site.site_header = 'BLOGSPOT | ADMIN PANEL'
admin.site.site_title = 'BLOGSPOT | BLOGGING WEBSITE'
admin.site.index_title= 'BlogSpot Site Administration'
