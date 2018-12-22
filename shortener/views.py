from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.http import HttpResponseRedirect
from .models import Link
from .forms import LinkModelForm, LinkInfoForm


class HomeView(View):
    form_class = LinkModelForm
    initial = {'url': 'http://'}
    template_name = 'shortener/home.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        context = {
            "form": form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect('link-details-view', link_id=instance.link_id)


def link_details(request, link_id):
    link = reverse('link-redirect-view', kwargs={"link_id": link_id})
    host = request.get_host()
    form = LinkInfoForm(initial={"url": host+link})
    context = {
        "form": form,
    }
    return render(request, "shortener/link_details.html", context)


def link_redirect(request, link_id):
    instance = get_object_or_404(Link, link_id=link_id)
    return HttpResponseRedirect(instance.url)
