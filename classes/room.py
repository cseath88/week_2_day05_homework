class Room:

    def __init__ (self, room_num):

        self.room_num = room_num
        self.guest_list = [ ]
        self.song_list = [ ]


    def guests_in_room(self):
        return len(self.guest_list)
    
    
    def songs_in_room(self):
        return len(self.song_list)
    

    def add_guest(self, guest):
        self.guest_list.append(guest)


    def add_song(self, song):
        self.song_list.append(song)

    
    def remove_guest(self, guest):
        if guest in self.guest_list:
            self.guest_list.clear


    def remove_song(self, song):
        if song in self.song_list:
            self.song_list.clear

    
        
            







    