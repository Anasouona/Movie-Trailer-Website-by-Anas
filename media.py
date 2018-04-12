import webbrowser


class Movie(object):
    """A movie instance can be created using following attributes.

    Attributes:
        title: Name of the movie.
        storyline: A brief description of movie plot.
        poster_image_url: URL of the poster.
        youtube_trailer_url: URL of trailer video hosted on Youtube.
        """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """Initialise movie attributes."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
