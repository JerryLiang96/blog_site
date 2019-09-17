from rest_framework import mixins, viewsets
from .serializers import BlogSerializer
from .models import Category


class BookView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    key = Category.objects.get(name='book')
    queryset = key.blog_set.all()

    def get_serializer_class(self):
        return BlogSerializer
