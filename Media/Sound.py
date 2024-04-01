import os
import winsound
from time import sleep

class SoundPlayer:
    def __init__(self):
        # Get the directory path of the current script
        self.folder_path = os.path.dirname(os.path.abspath(__file__))

    def play_sound(self, sound_file):
        # Construct the full path to the sound file
        sound_path = os.path.join(self.folder_path, sound_file)

        # Play the sound file using winsound
        print(sound_path)
        winsound.PlaySound(sound_path, winsound.SND_FILENAME)

# Create a SoundPlayer instance
player = SoundPlayer()

# Play the sound files
player.play_sound('whoosh.wav')
sleep(1)
player.play_sound('heroattack.wav')
sleep(1)
player.play_sound('orcattack.wav')
sleep(1)
player.play_sound('lucky.wav')
sleep(1)
player.play_sound('unlucky.wav')