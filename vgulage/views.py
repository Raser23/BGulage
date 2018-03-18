from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .forms import RegForm
from .models import User
from django.views import View


class IndexView(View):

    template_name = 'index.html'

    linames = [
        ('Моя Страница', 'ho_icon.png'),
        ('Новости', 'ne_icon.png'),
        ('Сообщения', 'mes_icon.png'),
        ('Друзья', 'fr_icon.png'),
        ('Группы', 'gr_icon.png'),
        ('Фотографии', 'ph_icon.png'),
        ('Аудиозаписи', 'au_icon.png'),
        ('Видеозаписи', 'vi_icon.png')
    ]

    def name_path(self, name, path):
        return {'name': name, 'path': '{% static\'vgulage/images/icons/' + path + ' \'%}'}

    def get(self, request, *args, **kwargs):
        context = {'linames': [self.name_path(n, p) for n, p in self.linames]}
        context['path_to_icons'] = 'vgulage/images/icons/'
        return render(request, self.template_name, context)


@method_decorator(csrf_exempt, name='dispatch')
class SignupView(View):

    template_name = 'signup.html'
    form_class = RegForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = User(name=form.cleaned_data['username'], pswd=form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect('/signed/')
        return render(request, self.template_name, {'form': form})


class SignedView(View):

    template_name = 'signed.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
