
import random
random_numbers = [random.randint(1, 20000) for _ in range(0,19999)] # generates from 10 - 99
print(random_numbers)

"""
import random

def generate_random_list_with_duplicates():
    # Generate a list of 10 random two-digit numbers
    random_numbers = [random.randint(10, 99) for _ in range(5)]
    
    # Add duplicates by copying some of the random numbers
    random_numbers += random.sample(random_numbers, 5)
    
    # Shuffle the list to mix the duplicates with the original numbers
    random.shuffle(random_numbers)
    
    return random_numbers

# Example usage
random_list = generate_random_list_with_duplicates()
print(random_list)

"""