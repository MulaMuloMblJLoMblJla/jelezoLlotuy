from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import SubMenu, Review, User

from .forms import ReviewForm, LoginForm, RegistrationForm
from django_registration.views import RegistrationView


class MyRegistration(RegistrationView):
    form = RegistrationForm
    success_url = '/'
    template_name = 'include/registration.html'

    def register(self, form):
        if form.is_valid():
            form.save()
        return redirect('/')



from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from .models import SubMenu, Review, User

from .forms import ReviewForm, LoginForm, RegistrationForm
from django_registration.views import RegistrationView


class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html', {'form': ReviewForm()})


class FormView(View):
    def get(self, request, *args, **kwargs):
        sub = SubMenu.objects.all()
        return render(request, 'forma.html', {'subs': sub, 'form1': LoginForm()})


class ListView(LoginRequiredMixin, View):
    login_url = 'form'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'list.html')
        else:
            return redirect('/')


class TableView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'table.html')


class ReviewsView(View):
    def post(self, request, *args, **kwards):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            reviews = Review.objects.all().values('name')
            for i in reviews:
                i['name'] += ', Ваша заявка отправлена'
            print(reviews)
            return JsonResponse({'reviews': list(reviews)}, safe=False)
