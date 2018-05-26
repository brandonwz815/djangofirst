from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView

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