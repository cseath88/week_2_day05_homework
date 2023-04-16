import unittest

from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):

        self.song = Song("Dijon", "Talk Down")

    def test_song_has_artist(self):
        self.assertEqual("Dijon", self.song.artist)

    def test_song_has_title(self):
        self.assertEqual("Talk Down", self.song.title)