
from django.conf.urls.static import static
from django.conf import settings

app_name = 'djangoapp'
urlpatterns = [
  
from django.conf.urls.static import static
from django.conf import settings

app_name = 'djangoapp'
urlpatterns = [
        path(route='login', view=views.login_user, name='login'),
    #
    # path for login
    # path(route='login', view=views.login_user, name='login'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # path for login
    # path(route='login', view=views.login_user, name='login'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
