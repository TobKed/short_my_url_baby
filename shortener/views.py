from django.shortcuts import render
from .forms import LinkModelForm


def home(request):
    link_form = LinkModelForm(initial={'url': 'http://'})
    context = {
        "form": link_form,
    }
    return render(request, 'shortener/home.html', context)
