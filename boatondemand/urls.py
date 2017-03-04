from django.conf.urls import url
from django.contrib import admin
from boatondemandapp import views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name= 'home'),
    url(r'^manager/sign-in/$', auth_views.login,
        {'template_name': 'manager/sign_in.html'},
        name= 'manager-sign-in'),
    url(r'^manager/sign-out', auth_views.logout,
        {'next_page': '/'},
        name= 'manager-sign-out'),
    url(r'^manager/sign-up', views.manager_sign_up,
        name= 'manager-sign-up'),
    url(r'^manager/$', views.manager_home, name= 'manager-home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
