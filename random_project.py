import random

budget = input("Whats the budget that you have? ")
price_per_spin = 15

spins_that_can_be_bought = int(budget) // price_per_spin

print(f"You can get {spins_that_can_be_bought} spins!")
money_to_be_returned = int(budget) - (spins_that_can_be_bought * price_per_spin)
print(f"Here's your change ${money_to_be_returned}.")
print("")
decision = input("Do you want to spin the wheel now? [Y/N]  ")

if decision.lower() == "y":
    for roulette in range(1, spins_that_can_be_bought + 1):
        num1 = random.randrange(1, 10)
        num2 = random.randrange(1, 10)
        num3 = random.randrange(1, 10)
        print(f"Spin Number {roulette}: ")
        print(num1, num2, num3,)
        print("")

        if num1 == num2 == num3:
            print("JACKPOT!!!")
        elif num1 == num2 or num2 == num3 or num1 == num3:
            print("You almost caught the big price ")

        if roulette == spins_that_can_be_bought:
            print("You have reached the spin limit")
            break
        else:
            decision = input("Do you want to spin the wheel? [Y/N]  ")
        if decision.lower() == "n":
            break



