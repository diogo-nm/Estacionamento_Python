class Estacionamento:
  def __init__(self, carro):
    self.carro = carro
    self.proximo = None

class Pilha:
  def __init__(self):
    self.topo = None
    self.tamanho = 0

  def __len__(self):
    return self.tamanho

  def carros_estacionados(self):
    fila = ''
    num = self.tamanho
    aux = self.topo
    while (aux):
      fila = fila + str(aux.carro) + f'-> vaga{num} \n'
      aux = aux.proximo
      num -= 1

    print(fila)

  def __str__(self):
    return self.__repr__()

  def estacionar(self, info):
    carro = Estacionamento(info)
    carro.proximo = self.topo
    self.topo = carro
    self.tamanho += 1

  def sair(self):
    if self.tamanho > 0:
      carro = self.topo
      self.topo = self.topo.proximo
      self.tamanho -= 1
      return carro.carro

    else:
      return None

  def pegar(self):
    if self.tamanho > 0:
      return self.topo.carro

    else:
      return None

class Fila:
  def __init__(self):
    self.primeiro = None
    self.ultimo = None
    self.tamanho = 0

  def __len__(self):
    return self.tamanho

  def carros_estacionados(self):
    if self.tamanho > 0:
      num = 1
      fila = ''
      aux_ponteiro = self.primeiro
      while(aux_ponteiro):
        fila = fila + str(aux_ponteiro.carro) + f'-> vaga {num}\n'
        aux_ponteiro = aux_ponteiro.proximo
        num += 1
      print(fila)
    else:
     return 'Fila vazia'

  def __str__(self):
    return self.__repr__()

  def estacionar(self, carro):
    carro = Estacionamento(carro)
    if self.ultimo is None:
      self.ultimo = carro
    else:
      self.ultimo.proximo = carro
      self.ultimo = carro

    if self.primeiro is None:
      self.primeiro = carro

    self.tamanho += 1

  def sair(self):
    if self.tamanho >0:
      carro = self.primeiro.carro
      self.primeiro = self.primeiro.proximo

      if self.primeiro is None:
        self.ultimo = None

      self.tamanho -= 1
      return carro
    raise IndexError('A fila está vazia')

  def pegar(self):
     if self.tamanho > 0:
      carro = self.primeiro.carro
      return carro
     raise IndexError('A fila está vazia!')
