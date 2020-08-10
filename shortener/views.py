from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from .forms import LinkInfoForm, LinkModelForm
from .models import Link


class HomeView(View):
    form_class = LinkModelForm
    initial = {"url": "http://"}
    template_name = "shortener/home.html"

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect("link-details-view", link_id=instance.link_id)
        return render(request, self.template_name, {"form": form})


def link_details(request, link_id):
    instance = get_object_or_404(Link, link_id=link_id)
    link = reverse("link-redirect-view", kwargs={"link_id": link_id})
    host = request.get_host()
    form = LinkInfoForm(initial={"url": host + link})
    messages.info(request, instance.url)
    context = {"form": form}
    return render(request, "shortener/link_details.html", context)


def link_redirect(request, link_id):
    instance = get_object_or_404(Link, link_id=link_id)
    return HttpResponseRedirect(instance.url)


def handler404(request):
    messages.error(request, "Error 404")
    return render(request, "shortener/base.html", status=404)


def handler500(request):
    messages.error(request, "Error 500")
    return render(request, "shortener/base.html", status=500)
