from django.shortcuts import render
#importing the models that we are going to use to access data in the views. 
from .models import Book, Author, BookInstance, Genre


# a view is a function that processes an HTTP request, fetches the data from the
# database and renders it in an HTML template, returning the generated HTML in a HTTP
# response. 

#we are calling it the index page because it is the indexing page that leads to all 
#the sub-pages. 

def index(request):
    """View function for the homepage of the site."""

    #generating counts of the main obejects 
    num_books = Book.objects.all().count() 
    num_instances = BookInstance.objects.all().count() 

    num_instances_available = BookInstance.objects.filter(status_exact='a').count() 

    num_authors = Author.objects.count() 


    #context dict which provides the html template with placeholders for the data
    #that is includede in the HTML request. 
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)




