  
import random as rnd


def skapaKortlek():
    kortnummer = [i for i in range(2, 11)]
    klädkort = ["J", "Q", "K", "A"]
    kortnummer += klädkort
    lek = kortnummer*4  # färg spelar ingen roll i blackjack

    blandaKortlek(lek)
    return lek


def blandaKortlek(lek):
    return rnd.shuffle(lek)