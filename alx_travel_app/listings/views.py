from rest_framework import viewsets, permissions
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer


class ListingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing listings.
    Only authenticated users can create listings.
    All users can view listings.
    """
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Return all listings. You can customize this to filter by location or host.
        """
        return Listing.objects.all()

    def perform_create(self, serializer):
        """
        Automatically assign the current user as the host.
        """
        serializer.save(host=self.request.user)


class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing bookings.
    Users can only view or create their own bookings.
    """
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Limit bookings to the current authenticated user.
        """
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Automatically assign the booking to the current user.
        """
        serializer.save(user=self.request.user)
