from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from rest_framework import viewsets, permissions, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from profileapp.models import Profile
from profileapp.permissions import SpecialPermission
from profileapp.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [SpecialPermission]

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except Exception as e:
            raise ValidationError(e)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = '../'
    template_name = 'signup.html'