from rest_framework import viewsets, status
from rest_framework.permissions import BasePermission
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Movie, Rating, Tag
from .serializers import MovieSerializer, RatingSerializer, SubmitRatingSerializer, TagSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class MoviePagination(PageNumberPagination):
    page_size = 10  # Set the number of movies per page


class IsAuthenticatedOrReadOnly(BasePermission):
    """
    Custom permission class to allow read-only access for anonymous users.
    """

    def has_permission(self, request, view):
        return (
            request.method in ["GET", "HEAD", "OPTIONS"]
            or request.user
            and request.user.is_authenticated
        )


class MovieViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = "movieId"
    pagination_class = MoviePagination

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="genre",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Filter movies by genre",
            ),
            openapi.Parameter(
                name="tag",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Filter movies by tag",
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        genre = self.request.query_params.get("genre", None)

        if genre:
            # Filter movies based on the provided genre
            queryset = queryset.filter(genres__icontains=genre)

        tag = self.request.query_params.get("tag", None)

        if tag:
            # Filter movies based on the provided tag
            queryset = queryset.filter(tags__tag__icontains=tag)

        return queryset

    @swagger_auto_schema(
        methods=['post'],
        request_body=SubmitRatingSerializer,
        responses={201: 'Rating added successfully', 400: 'Invalid rating value or already rated'},
        operation_summary='Rate a movie',
        operation_description='Allows an authenticated user to rate a movie with a value between 0.5 and 5.'
    )
    @action(detail=True, methods=["POST"])
    def rate(self, request, movieId=None):
        movie = self.get_object()
        user = request.user  # Assumes authentication is set up

        # Check if the user has already rated the movie
        existing_rating = Rating.objects.filter(movie=movie, user=user).first()

        if existing_rating:
            return Response(
                {"detail": "You have already rated this movie."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Validate the rating value
        rating_value = request.data.get("rating")
        if rating_value is None or not (0.5 <= rating_value <= 5):
            return Response(
                {"detail": "Invalid rating value. It must be between 0.5 and 5."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Create a new rating for the movie
        rating_data = {"user": user.id, "movie": movie.movieId, "rating": rating_value}
        serializer = RatingSerializer(data=rating_data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"detail": "Rating added successfully."}, status=status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    lookup_field = "movieId"
    pagination_class = MoviePagination


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "tagId"
    pagination_class = MoviePagination
