import webbrowser


class Movie():
    # class Movie stores movie information.
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # initialize the instance for opening trailer video
        webbrowser.open(self.trailer_youtube_url)
