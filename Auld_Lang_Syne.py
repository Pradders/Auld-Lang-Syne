#Import key packages
import musicalbeeps
import numpy as np

#Key notes of intro
music_notes = ['D4','G','G','G','B','A','G','A','B','G','G','B','D5','E5','E5','D5','B','B','G','A','G','A','B','A','G','E','E','D','G']

#Scale the time for each note
bpm = 120 #beats per minute
scale_time = 60/bpm #scaled to 60s
duration = scale_time*np.array([1, 1.5, 0.5, 1, 1, 1.5, 0.5, 1, 1, 1.5, 0.5, 1, 1, 3, 1, 1.5, 0.5, 1, 1, 1.5, 0.5, 1, 1, 1, 1.5, 0.5, 1, 1, 3]) #list time for each note here

#Player, default volume scaled at 0.3 (ranges from 0 to 1), individual notes, frequency and duration output
player = musicalbeeps.Player(volume = 0.6, mute_output = False)

#Play each note for the set duration
for i in range(0, len(music_notes)):
    player.play_note(music_notes[i], duration[i])