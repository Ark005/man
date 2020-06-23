from django.views.generic import UpdateView,ListView,CreateView 
from .models import Person
from .forms import PersonForm
from django.urls import reverse_lazy



class HomePageView(ListView):
    model = Person
    template_name = 'home.html'

class CreatePostView(CreateView): 
    model = Person
    form_class = PersonForm
    template_name = 'post.html'
    success_url = reverse_lazy('home') 

