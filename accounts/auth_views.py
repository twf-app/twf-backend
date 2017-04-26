from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView, RedirectView


class LoginView(FormView):
    template_name = 'site.html'
    success_url = 'https://www.google.com'
    form_access = AuthenticationForm
    redirect_field_name = '/'


class LogoutView(RedirectView):
    template_name = 'site.html'
    redirect_field_name = '/'


class RegisterView(FormView):
    template_name = 'site.html'
    success_url = 'site.html'
