from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from rest_framework import viewsets, permissions

from profileapp.models import Profile
from profileapp.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = '../'
    template_name = 'signup.html'