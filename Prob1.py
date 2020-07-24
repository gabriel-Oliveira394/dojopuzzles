"""
Um determinado ano é bissexto se:
O ano for divisível por 4, mas não divisível por 100, exceto se ele for também divisível por 400.

Escreva uma função que determina se um determinado ano informado é bissexto ou não.
"""

ano = int(input("Digite um ano: "))

print(type(ano))
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'O ano {ano} é bissexto!')

        else:
            print(f'O ano {ano} não é bissexto!')

    else:
        print(f'O ano {ano} é bissexto!')

else:
    print(f'O ano {ano} não é bissexto!')