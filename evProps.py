#1 Aces We choose 10 card at random from a 52 card deck. Find the expected value of aces
deck = 52
randNumero = 10
def evAces(deck, randNumero):
    ev = (4 / deck) * randNumero
    return ev 
    
print(evAces(deck, randNumero))