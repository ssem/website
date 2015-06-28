from django.http import HttpResponse

def home(request):
    template_name = 'passwords/password_check.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context
