from pygame import mixer

# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("Popular Gaming Sound Effects (HD).mp3")

# Setting the volume
mixer.music.set_volume(0.7)

# Start playing the song
mixer.music.play()
