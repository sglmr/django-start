from django.views import generic


class HomePageView(generic.TemplateView):
    template_name = "core/index.html"


class AboutPageView(generic.TemplateView):
    template_name = "core/about.html"
