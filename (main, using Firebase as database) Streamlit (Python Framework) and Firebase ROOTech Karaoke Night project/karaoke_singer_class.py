class KaraokeSinger:
    def __init__(self, name, song_choice, song_artist):
        self.name = name
        self.song_choice = song_choice
        self.song_artist = song_artist

    #Just want to be able to see the 'KaraokeSinger' object's attribute in the terminal when it is printed rather than
    #a 'KaraokeSinger' object
    def __repr__(self):
        return "KaraokeSinger('{}', '{}', '{}')".format(self.name, self.song_choice, self.song_artist)
    
    #Allows the 'KaraokeSinger' object to be recreated as a dictionary so it can be used to be reuploaded into the csv 
    #database in 'karaoke_singer_registration_streamlit.py' file
    def as_dict(self):
        return {'name': self.name, 'song_choice': self.song_choice, 'song_artist': self.song_artist}
