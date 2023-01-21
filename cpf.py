  
cpf = ('41159993068')

nove_digitos = cpf[:9]
contador_regres_1 = 10
resul_digito_1  = 0

for digito in nove_digitos:
    resul_digito_1 += int(digito) * contador_regres_1
    contador_regres_1 -= 1

primeiro_digi = (resul_digito_1 * 10) % 11 
digi_1 = primeiro_digi if primeiro_digi <= 9 else 0


dez_digitos = nove_digitos + str(digi_1)
contador_regressivo_2 = 11
resultado_digito_2 = 0

for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
digi_1 = str(digi_1)
digito_2 = str(digito_2)

digitos = (nove_digitos + digi_1 + digito_2)
print(digitos)

if cpf == digitos:
    print('O cpf é valido!')
else:
    print('O cpf é inválido!')







   






