from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import PhotoForm
from .models import Rubric, Photo
from django.urls import reverse_lazy


def mainpage(request):
    photos = Photo.objects.all()
    rubrics = Rubric.objects.all()
    return render(request, 'mystery/mainpage.html', {'photos': photos, 'rubrics': rubrics})


class PhotoCreateView(CreateView):
    template_name = 'mystery/create.html'
    form_class = PhotoForm
    success_url = reverse_lazy('index')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


def by_rubric(request, rubric_id):
    photos = Photo.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'photos': photos, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'mystery/by_rubric.html', context)