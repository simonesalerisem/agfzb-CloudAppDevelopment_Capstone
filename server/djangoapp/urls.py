from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

    # path for about view

    # path for contact us view

    # path for registration

    # path for login

    # path for logout

    path(route='dealers', view=views.get_dealerships, name='index'),
    path(route='contacts', view=views.get_contacts, name='contacts'),
    path(route='about', view=views.get_aboutus, name='about'),
    path(route='register', view=views.get_registration_view, name='register'),
    path(route='new_user_success', view=views.get_new_user_success_view, name='new_user_success'),
    path('logout', views.get_logout, name='logout'),
    path('login', views.get_login, name='login'),
    path('add_new_user', views.add_new_user, name='add_new_user'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)