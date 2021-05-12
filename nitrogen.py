import random, string


from colorama import Fore, Back, Style
print(Fore.RED + 'Criado por CT02')
print('https://github.com/CT0222/Nitro-Generator')
print('')
amount = int(input('Quantos códigos você deseja: '))
value = 1
while value <= amount:
    codigo = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16)) 
    f = open('Nitro.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'[CT02] {code}')
    value += 1
