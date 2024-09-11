import random

lower = "abcdefghijklmnñopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%&/()_-+=?><[]{.}*"

all_chars = lower + upper + numbers + symbols
lenght = int(input("Enter a legnth: "))

password = ''.join(random.sample(all_chars, lenght))
print("Generar password: ", password)