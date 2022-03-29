import random


def gen_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Set random counts
    nr_letters = random.randint(6, 12)
    nr_numbers = random.randint(4, 6)
    nr_symbols = random.randint(4, 6)

    # Get random values
    rand_letters = [random.choice(letters) for _ in range(nr_letters)]
    rand_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    rand_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    random_password = rand_letters + rand_numbers + rand_symbols

    # Randomize array and export as string
    random.shuffle(random_password)
    final_password = "".join(random_password)

    return final_password
