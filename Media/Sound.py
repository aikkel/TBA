from playsound import playsound

class SoundPlayer:
    def __init__(self, whoosh, heroattack, orcattack):
        self.whoosh = whoosh
        self.heroattack = heroattack
        self.orcattack = orcattack

    def play_whoosh(self):
        playsound(self.whoosh)

    def play_hero_attack(self):
        playsound(self.heroattack)

    def play_orc_attack(self):
        playsound(self.orcattack)