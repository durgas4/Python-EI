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



while True:
    num = int(input("Enter an integer number: "))
    if num == secret_number:
        break
    print("Ha ha! You're stuck in my loop!")

print("Well done, muggle! You are free now.")
