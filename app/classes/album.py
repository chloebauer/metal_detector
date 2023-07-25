class Album:
    def __init__(self, band_name, band_url, album_name, album_url, genre, release_date):
        self.band_name = band_name
        self.band_url = band_url
        self.album_name = album_name
        self.album_url = album_url
        self.genre = genre
        self.release_date = release_date

    def formatted_output(self):
        return '{} by {}\nGenre: {}\nRelease Date: {}'.format(self.album_name, self.band_name,
                                                              self.genre, self.release_date)
