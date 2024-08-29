class KaraokeSinger:
    def __init__(self, name, song_choice):
        self.name = name
        self.song_choice = song_choice

    #Just want to be able to see the 'KaraokeSinger' object's attribute in the terminal when it is printed rather than
    #a 'KaraokeSinger' object
    def __repr__(self):
        return "KaraokeSinger('{}', '{}')".format(self.name, self.song_choice)
    
    #Allows the 'KaraokeSinger' object to be recreated as a dictionary so it can be used to be reuploaded into the csv 
    #database in '(main)_karaoke_singer_registration_streamlit_csv.py' file
    def as_dict(self):
        return {'name': self.name, 'song_choice': self.song_choice}