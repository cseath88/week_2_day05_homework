import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room(1)
        self.guest_1 = Guest("Harry")
        self.song_1 = Song("Radiohead", "Exit Music")


    def test_room_has_num(self):
        self.assertEqual(1, self.room_1.room_num)

    
    def test_can_add_song(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual(1, self.room_1.songs_in_room())


    def test_can_add_guest(self):
        self.room_1.add_guest(self.guest_1)
        self.assertEqual(1, self.room_1.guests_in_room())


    def test_can_remove_guest(self):
        self.room_1.remove_guest(self.guest_1)
        self.assertEqual(0, self.room_1.guests_in_room())


    def test_can_remove_song(self):
        self.room_1.remove_song(self.song_1)
        self.assertEqual(0, self.room_1.songs_in_room())

