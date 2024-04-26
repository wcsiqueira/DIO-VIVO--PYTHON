# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano

    # Método fazer_chamada para permitir que um usuário faça uma chamada telefônica:
    def fazer_chamada(self, destinatario, duracao):
        custo = self.__plano.custo_chamada(duracao)
        if self.__plano.verificar_saldo() >= custo:
            self.__plano.deduzir_saldo(custo)
            saldo_restante = self.__plano.verificar_saldo()
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${saldo_restante:.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."


# Classe Plano, ela representa o plano de um usuário de telefone:
class Plano:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    # Método para verificar_saldo e retorne o saldo atual:
    def verificar_saldo(self):
        return self.__saldo

    # Método custo_chamada para calcular o custo de uma chamada supondo o custo de $0.10 por minuto:
    def custo_chamada(self, duracao):
        return duracao * 0.10

    # Método deduzir_saldo para deduzir o valor do saldo do plano:
    def deduzir_saldo(self, valor):
        self.__saldo -= valor


# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário:
nome = input(" ")
numero = input(" ")
saldo_inicial = float(input(" "))

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input(" ")
duracao = int(input(" "))

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
