class Song:

    count = 0
    genres = []
    artist = []
    genre_count = {}


    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
     

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)


    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artist:
            cls.artist.append(artist)
    
    
