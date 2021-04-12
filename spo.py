# create a class for getting those top hits and showing them
class sporeads:
    def getreads(self, artist):
        import spotipy
        from spotipy.oauth2 import SpotifyClientCredentials
        self.artist = artist
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="0822a31cd9d04068ba59343d6b3e1a80",
                                                                   client_secret="df0c7bbb087844179ff7264f1d715e5d"))
        self.results = sp.search(q=artist, limit=5)

    def showreads(self):
        re = self.results
        return(re)