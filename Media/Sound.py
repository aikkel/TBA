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

    def play_whoosh(self):
        self.play_sound('whoosh.wav')

    def play_hero_attack(self):
        self.play_sound('heroattack.wav')

    def play_orc_attack(self):
        self.play_sound('orcattack.wav')

    def play_lucky(self):
        self.play_sound('lucky.wav')

    def play_unlucky(self):
        self.play_sound('unlucky.wav')

# Create a SoundPlayer instance
player = SoundPlayer()

# Play the specific sound files
# player.play_lucky()
# sleep(1)
# player.play_unlucky()
# sleep(1)
# player.play_hero_attack()