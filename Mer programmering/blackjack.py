import kortlek


def skrivUtHand(hand):
    print("Dina kort är: ", end="")
    for kort in hand:
        print(str(kort) + ", ", end="")


def räknaPoäng(hand):
    poäng = 0
    for kort in hand:
        if kort == "J" or kort == "Q" or kort == "K":
            poäng += 10
        elif kort == "A" and poäng < 11:
            poäng += 11
        elif kort == "A" and poäng >= 11:
            poäng += 1
        else:
            poäng += kort
    return poäng


def checkaVinnare(hand, dealer):
    dealerPoäng = räknaPoäng(dealer)
    spelare1Poäng = räknaPoäng(hand)

    print(f"Dealerns kort är {dealer[0]} och {dealer[1]}")
    print(f"Dealerns totala poäng: {dealerPoäng}")
    print(f"Spelare1 totala poäng: {spelare1Poäng}")

    if spelare1Poäng == 21:
        print("Blackjack, du vinner")
    elif spelare1Poäng <= dealerPoäng or spelare1Poäng > 21:
        print("Dealern tar dina pengar")
    else:
        print("Du vinner")


# spel-loop
def spel_loop():
    while True:
        spela = input(
            "Vill du spela? (j för ja, valfri tangent för att avsluta)")

        if spela != "j":
            break
        lek = kortlek.skapaKortlek()
        # dealer tar två kort
        dealer = [lek.pop(0), lek.pop(0)]

        print(f"Dealerns första kort är {dealer[0]}")

        hand = [lek.pop(0), lek.pop(0)]

        print(f"Dina första två kort är {hand[0]} och {hand[1]}")

        fortsätt = True

        # omgång
        while fortsätt:
            # fråga om användaren vill ta ett till kort
            taKort = input("Ta nytt kort? (j för ja, annan tangent för nej)")

            if taKort == "j" and räknaPoäng(hand) <= 21:
                # dela ut kort
                hand.append(lek.pop(0))
                skrivUtHand(hand)
            else:
                fortsätt = False  # avsluta spelet

        checkaVinnare(hand, dealer)


if __name__ == "__main__":
    spel_loop()