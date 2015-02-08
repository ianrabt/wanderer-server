from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from django.conf import settings

from rest_framework import routers, serializers, viewsets
from wanderer.models import Location, Rating, Perspective

###

# Serializers define the API representation.

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'address','latitude', 'longitude', 'perspective_set', 'rating_set')
        depth = 1

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating

class PerspectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perspective

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class PerspectiveViewSet(viewsets.ModelViewSet):
    queryset = Perspective.objects.all()
    serializer_class = PerspectiveSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'perspectives', PerspectiveViewSet)

###

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'coresite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^w/', include('wanderer.urls')),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
