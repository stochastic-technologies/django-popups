from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

urlpatterns = patterns("popups.api",
    url(r"^hide/$", "hide_popup", name="popups-hide"),
)

