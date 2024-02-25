* I want to create a django project named movielens with application movies 
* want to create a new model Movie using the schema for Movie Lens ml-20m dataset
* want to add a django rest framework API for the Movielens ml-20m Movie model that can list, retrieve, create and updated movie. Prefer to use Django Rest Framework viewsets.
* please add pagination to the movie list results
* peach movie has genres assigned as pipe separated list of genres. I want the API to return a list of strings from the pipe separated string
* i want to add swagger documentation to my movie lens api
* need to add also the ratings model from the Movielens ml-20m dataset
* the timestamp column is a unix epoch timestamp
* also want to add tags model to my Movielens movies application for tags.csv
* want tags and movies to have foreign key relationship
* want the foreign key to preserve existing movieId column
* want to add a filter to movies list so that only movies with given genre are returned
* want to add drf_yasg annotation to list method so that the genre is shown in the Swagger
* openapi module is not imported. What is the correct import statement?
* want to add api POST /api/movies/{movieId}/rate/ so that authenticated users can rate a movie with rating from 0.5 to 5
* need to restrict actions like update, delete, rate for a movie to only authenticated users
* I still want list and retrieve to be available for anonymous users
* want to annotate the rate action so that it is known to swagger
* want that rate action accepts only rate value and not all the values from RatingSerializer
