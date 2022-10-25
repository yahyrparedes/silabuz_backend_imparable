from rest_framework.permissions import IsAuthenticated

from apps.artists.models import Artist


class IsArtist(IsAuthenticated):

    def has_permission(self, request, view):
        is_authenticated = super(IsArtist, self).has_permission(request, view)
        if not is_authenticated:
            return False
        try:
            return request.user.artist is not None
        except Artist.DoesNotExist:
            return False


class IsArtistAndActive(IsArtist):

    def has_permission(self, request, view):
        is_artist = super(IsArtistAndActive, self).has_permission(request, view)
        if not is_artist:
            return False
        return request.user.artist.is_active
