import os
import threading
from playsound import playsound

class SoundPlayer:
    def __init__(self):
        self.folder_path = os.path.dirname(os.path.abspath(__file__))
        self.music_playing = False
        self.music_thread = None
        self.music_lock = threading.Lock()

    def play_sound(self, sound_file):
        sound_path = os.path.join(self.folder_path, sound_file)
        playsound(sound_path)

    def play_background_music(self, music_file):
        self.music_playing = True
        while self.music_playing:
            sound_path = os.path.join(self.folder_path, music_file)
            playsound(sound_path)

    def start_music_loop_thread(self, music_file='titelMusic.wav'):
        with self.music_lock:
            if not self.music_playing:
                self.music_thread = threading.Thread(
                    target=self.play_background_music,
                    args=(music_file,),
                    daemon=True
                )
                self.music_thread.start()
                self.music_playing = True

    def stop_music_loop_thread(self):
        with self.music_lock:
            self.music_playing = False
            if self.music_thread:
                self.music_thread.join()

    def play_whoosh(self):
        threading.Thread(target=self.play_sound, args=('whoosh.wav',)).start()

    def play_hero_attack(self):
        threading.Thread(target=self.play_sound, args=('heroattack.wav',)).start()

    def play_orc_attack(self):
        threading.Thread(target=self.play_sound, args=('orcattack.wav',)).start()

    def play_lucky(self):
        threading.Thread(target=self.play_sound, args=('lucky.wav',)).start()

    def play_unlucky(self):
        threading.Thread(target=self.play_sound, args=('unlucky.wav',)).start()

    def play_titel(self):
        threading.Thread(target=self.play_sound, args=('titelMusic.wav',)).start()
