frase = str(input("Digite seu nome completo: ")).strip()

print("Seu nome em letra maiúscula é {}".format(frase.upper()))
print("Seu nome minúsculo é {}".format(frase.lower()))
print("Seu nome tem ao todo {} letras. ".format(len(frase)-frase.count(' ')))
#print("Seu primeiro nome tem {} letras.".format(frase.find(' ')))
separa = frase.split()
print("Seu primeiro nome é {} e ele tem {} letras.".format(separa[0], len(separa[0])))
