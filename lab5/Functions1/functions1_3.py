def solve(numhead, numlegs):
    chicken_legs = numhead * 2
    rabbit_legs = numlegs - chicken_legs
    rabbits = rabbit_legs/2
    chickens = numhead - rabbits
    return rabbits, chickens

numhead, numlegs = int(input()), int(input())
print(solve(numhead, numlegs))