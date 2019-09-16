from rest_framework import mixins, viewsets
from .serializers import NavSerializer
from .models import Nav


class NavView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Nav.objects.all()

    def get_serializer_class(self):
        return NavSerializer
