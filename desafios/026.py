frase = str(input("Escreva uma frase qualquer: ")).upper().strip()
print("A sua frase aparece a letra 'A' {} vezes." .format(frase.count('A')))
print("A letra 'A' aparece na posição a primeira vez: {}".format(frase.find('A')+1))
print("A letra 'A' aparece na posição a última vez: {}".format(frase.rfind('A')+1))