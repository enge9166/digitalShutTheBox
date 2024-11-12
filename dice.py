import random

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def valid_combinations(numbers, target):
    if target == 0:
        return [[]]
    if not numbers:
        return []
    result = []
    for i, num in enumerate(numbers):
        if num <= target:
            for combo in valid_combinations(numbers[i+1:], target - num):
                result.append([num] + combo)
    return result
