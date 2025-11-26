class Carro(object):
    def Falecomigo(self):
        print('Sou um carro')
class Fusca(Carro):
    def FaleComUmFusca(self):
        print('Sou um Fusca')
x = Carro()
y = Fusca()

x.Falecomigo()
y.Falecomigo()
    
