import random
import string

def password_generator(Len_pass = 8):
    ascii_options = string.ascii_letters
    number_option = string.digits
    punt_options = string.punctuation
    option = ascii_options + number_option + punt_options
    password_user = ""
    for i in range(0, Len_pass):
        digit = random.choice(option)
        password_user = password_user + digit
    return password_user

choice_user = input("Quantos digitos na senha?")
    
if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print("Entrada invalida!")
    quit()
        
response = password_generator(Len_pass = choice_user)

print(f"Senha gerada:\n{response}")
