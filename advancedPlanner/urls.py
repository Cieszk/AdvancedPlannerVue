from django.contrib import admin
from django.urls import path, include
from django_registration.backends.one_step.views import RegistrationView
# from django_registration.backends.activation.views import RegistrationView
from users.forms import CustomRegisterForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.api.urls')),

    path('accounts/reigster/', RegistrationView.as_view(
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

]
