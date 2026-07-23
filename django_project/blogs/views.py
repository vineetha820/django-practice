from django.shortcuts import render
from .models import post

posts=[
    {
    'author': 'Sai Krishna',
    'title': 'Blog Post 1', 
    'content': 'This is the content of the first blog post.',
    'date': 'October 1, 2023'
},
{
    'author': 'Sai Krishna',
    'title': 'Blog Post 1', 
    'content': 'This is the content of the first blog post.',
    'date': 'October 1, 2023'
}
]

def home(request):
    context={
        'posts':post.objects.all(),
        'title':'Home Page'
    }
    return render(request,'blogs/home.html',context)

def about(request):
    return render(request,'blogs/about.html')
def contact(request):
    return render(request,'blogs/contact.html')