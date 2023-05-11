from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language



##admin.site.register(Book)
admin.site.register(Genre)
#admin.site.register(Author)
#admin.site.register(BookInstance)
admin.site.register(Language)

#The model admin classes allow us to change how the admin models are displayed on the
# admin site.

#configuring a listview for authors in the admin site. 
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    #how the detailed view is setup. (changing models from the admin site)
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    

admin.site.register(Author, AuthorAdmin)



#tabular inline allows the admin user to see multiple instances of the books at the same time.
class BookInstanceInline(admin.TabularInline):
    model = BookInstance 

@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')



#will allow the admin to filter based on the status or the due back date. 
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')

    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )