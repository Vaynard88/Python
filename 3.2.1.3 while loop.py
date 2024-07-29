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
guess_number = int(input("Enter a magic number: "))
while guess_number != secret_number:
  print('"Ha ha! You\'re stuck in my loop!"')
  guess_number = int(input("Take another guess: "))
print('"Well done, muggle! You are free now."')