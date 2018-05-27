from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import RestrauntLocation

def restraunt_listview(request):
    template_name = 'restraunts/restraunts_list.html'
    queryset = RestrauntLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)

class RestrauntListView(ListView):

    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestrauntLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else: 
            queryset = RestrauntLocation.objects.all()
        return queryset

class RestrauntDetailView(DetailView):
    queryset = RestrauntLocation.objects.all()

    def get_context_data(self, *args, **kwargs):
        print(self.kwargs)
        context = super(RestrauntDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        rest_id = self.kwargs.get('rest_id')
        obj = get_object_or_404(RestrauntLocation, id=rest_id)
        return obj

class SearchRestrauntListView(ListView):
    template_name = 'restraunts/restraunts_list.html'

    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestrauntLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else: 
            queryset = RestrauntLocation.objects.none()
        return queryset

# class AsianFusionRestrauntListView(ListView):
#     queryset = RestrauntLocation.objects.filter(category__iexact='asian fusion')
#     template_name = 'restraunts/restraunts_list.html'