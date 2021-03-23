secret_number = 777

print(
    """
    +================================+
    | Welcome to my game, muggle!    |
    | Enter an integer number        |
    | and guess what number I've     |
    | picked for you.                |
    | So, what is the secret number? |
    +================================+
    """)


num = int(input("Enter an integer number: "))
if num != secret_number:
    print("Ha ha! You're stuck in my loop!")
    while True:
        input("")
else:
    print("Well done, muggle! You are free now.")
