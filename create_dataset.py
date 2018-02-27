# -*- coding: utf-8 -*-
import string
import glob
import numpy as np

song_list = glob.glob('songs/*')
songs = []
for song_file in song_list:
    songs.append(file(song_file).read())

song_lines = {}
for song in songs:
    #song = song.replace("—", " ") #get rid of the em dash
    #song = song.replace("…", " ") #get rid of the horizontal ellipsis
    #song = song.replace("""’""", " ") #get rid of rightquote
    #song = song.replace("""‘""", " ") #get rid of leftquote
    lowered = song.lower() #lower case all text for better normalization
    undigited = ''.join([i for i in lowered if not i.isdigit()]) #remove digits
    unpunctuated = undigited.translate(None, string.punctuation) #remove all punctuation
    lines = unpunctuated.split("\n")       #separate lines
    song_lines[song] = lines
words=[]
total_words = 0
song_words_nb = []
for song in songs:
    song_words_nb.append(0)
cpt = 0

for song_line in song_lines:
    line_words = song_line.split(' ')
    song_words_nb[cpt] = 0
    for word in line_words:
        total_words += 1
        song_words_nb[cpt] += 1
        if word not in words:
            words.append(word)
    cpt += 1

word_data = np.zeros((80,1000,len(words)+2))

for song_nb in range(len(songs)):
    word_song_nb=0
    for song_line_nb in range(len(song_lines)):
        for word in line_words:
            if word_song_nb < 1000:
                word_data[song_nb,word_song_nb,words.index(word)]=1
                word_song_nb+=1

np.save('dataset.npy',word_data)
