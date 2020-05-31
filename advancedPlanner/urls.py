from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import settings

from django_registration.backends.one_step.views import RegistrationView
# from django_registration.backends.activation.views import RegistrationView

from users.forms import CustomRegisterForm

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/', include('users.api.urls')),
    path('api/', include('planner.api.urls')),

    path('accounts/register/', RegistrationView.as_view(
        form_class=CustomRegisterForm,
        success_url='/'),
        name='django-registration-register'
    ),
    path('accounts/', include('django.contrib.auth.urls')),

    # Login via browsable API
    path('api-auth/', include('rest_framework.urls')),
    # Login via Rest
    path('api/rest-auth/', include('rest_auth.urls')),
    # Register via Rest
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
