import numpy as np

def dice_roll():
    return np.random.randint(1, 7) 

def reverse_dice():
    return np.random.randint(-7, 0)

dice_rolls = [dice_roll() for _ in range(10)]
print(dice_rolls)