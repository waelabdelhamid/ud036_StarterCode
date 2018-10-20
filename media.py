class Movie():
    """ This class provides a way to store movie related information.

    Attributes:
        movie_title: A string contains the title of the movie.
        poster_image: A string contains the URL of the poster image.
        trailer_youtube: A string contains the URL of the youtube trailer.
    """

    def __init__(self, movie_title, poster_image, trailer_youtube):
        
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
