# flip a coin 1,000,000 times. 
# how many times will you get tails?

from random import randrange


def try_once(n):
    counter = 0 
    for i in range(0, n):
        if(randrange(0, n + 1) % 2): 
            counter += 1
    print(counter + " " + abs(counter - n // 2))

def main():
    for t in range(0, 10): 
        try_once(1000000)

print(main)