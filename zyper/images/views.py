from django.http import Http404

from rest_framework import viewsets, serializers, status
from rest_framework.response import Response

from zyper.images.tasks import gen_thumbnail
from zyper.images.models import ImageFile

from django.shortcuts import redirect

class ImageSerializer(serializers.ModelSerializer):
    file_thumb = serializers.FileField(read_only=True)
    file_original = serializers.FileField(required=True)
    name = serializers.CharField(
        required=True, allow_blank=False
    )

    class Meta:
        model = ImageFile
        fields = '__all__'


class ImageViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = ImageFile.objects.all()

        serializer = ImageSerializer(
            queryset, 
            many=True,
            context={'request': request}
        )

        return Response(serializer.data)

    def create(self, request):
        serializer = ImageSerializer(
            data=request.data,
            context={'request': request}
        )

        if serializer.is_valid():
            serializer.save()
            gen_thumbnail.delay(serializer.instance.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                                                    
    def instance(self, request, pk):
        try:
            image = ImageFile.objects.get(pk=pk)
        except ImageFile.DoesNotExist:
            raise Http404
        
        serializer = ImageSerializer(
            image,
            context={'request': request}
        )

        return Response(serializer.data)


image_list = ImageViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

image_instance = ImageViewSet.as_view({
    'get': 'instance'
})
