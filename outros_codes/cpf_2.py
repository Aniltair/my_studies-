import re

cpf = ('3629276504-0')
cpf = re.sub(r'[^0-9]', '', cpf)
nove_dig = cpf[:9]
print(cpf)
def Digito_um(nove_dig):
    contador_regres = 10
    resultado = 0
    for digitos in nove_dig:
        resultado += int(digitos) * contador_regres
        contador_regres -= 1 
    Digito_um = (resultado * 10) % 11
    Digito_um = Digito_um if Digito_um <= 9 else 0
    Digito_um = str(Digito_um)
    return Digito_um

dez_digitos = nove_dig + Digito_um(nove_dig)


def Digito_dois(dez_digitos):
    contador_regres = 11 
    resultado = 0
    for digitos in dez_digitos:
        resultado += int(digitos) * contador_regres
        contador_regres -= 1
    Digito_dois = (resultado * 10) % 11
    Digito_dois = Digito_dois if Digito_dois <= 9 else 0
    Digito_dois = str(Digito_dois)
    return Digito_dois

cpf_val = nove_dig + Digito_um(nove_dig) + Digito_dois(dez_digitos)

if cpf == cpf_val:
    print('O cpf é válido')
else:
    print('cpf inválido')



