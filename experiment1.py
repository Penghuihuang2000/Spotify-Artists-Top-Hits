import spotipy
from spo import sporeads
from spotipy.oauth2 import SpotifyClientCredentials

from tkinter import *
from tkinter import messagebox

root = Tk()  # get a window


def main():
    # input
    root.title('Spotify Artist Top Hits')  # set the title of the window
    Label(root, text='Artist').grid(row=0, column=0)
    enter = Entry(root)  # input the artist you wanna search
    enter.grid(row=0, column=1, padx=20, pady=20)  # adjust the position
    enter.delete(0, END)
    enter.insert(0, 'Ariana Grande')  # the default artist is Ariana Grande


    running = 1

    def get_tophits() :
        artist_name = enter.get()
        res = sporeads()
        res.getreads(artist_name)
        song_dict = res.showreads()
        show_data(song_dict, artist_name)

    def show_data (song_dict, artist_name) :  # show the data we get from spotify web api
        root1 = Tk()  # sub window
        root1.geometry('1200x600')
        root1.title(artist_name + 'Top Hits')

        for idx, track in enumerate(song_dict['tracks']['items']):  # put the data of each song we got into the frame
            LANGS = [(str(idx+1), 'rank'),
                     (track['name'], 'song'),
                     (track['album']['name'], 'album'),
                     (track['album']['release_date'], 'release'),
                     (str(track['popularity']), 'popularity')]
            group = LabelFrame(root1, text='songs', padx=0, pady=0)  # frame
            group.pack(padx=11, pady=0, side=LEFT)  # place the frame
            for lang, value in LANGS:  # set data into the frame
                c = Label(group, text=value + ': ' + lang)
                c.pack(anchor=W)
        Label(root1, text='*popularity: popularity index given by Spotify',
              fg='black').place(x=40, y=20, height=40)

        Button(root1, text='quit', width=10, command=root1.quit).place(x=500, y=100, width=80, height=40)  # 退出按钮
        root1.mainloop()


    Button(root, text="confirm", width=10, command=get_tophits) \
        .grid(row=3, column=0, sticky=W, padx=10, pady=5)
    Button(root, text='quit', width=10, command=root.quit) \
        .grid(row=3, column=1, sticky=E, padx=10, pady=5)
    if running == 1:
        root.mainloop()


if __name__ == '__main__':
    main()

