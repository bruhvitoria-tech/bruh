altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))

area = altura*largura

print("Sua parede tem dimensão de {}x{} e sua área é de {}m².".format(largura,altura,area))

tinta = area/2

print("Você precisará de {}L para pintas a sua parede.".format(tinta))

