class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserirSemPrioridade(self, nodo):
        if not self.head:
            self.head = nodo
        else:
            current = self.head
            while current.proximo:
                current = current.proximo
            current.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if not self.head:
            self.head = nodo
        else:
            current = self.head
            prev = None
            while current and current.cor == "A":
                prev = current
                current = current.proximo
            if prev:
                nodo.proximo = prev.proximo
                prev.proximo = nodo
            else:
                nodo.proximo = self.head
                self.head = nodo

    def inserir(self):
        cor = input("Digite a cor do cartão (A ou V): ").upper()
        numero = int(input("Digite o número do cartão: "))
        novo_nodo = Nodo(numero, cor)
        if not self.head:
            self.head = novo_nodo
        elif cor == "V":
            self.inserirSemPrioridade(novo_nodo)
        elif cor == "A":
            self.inserirComPrioridade(novo_nodo)

    def imprimirListaEspera(self):
        current = self.head
        while current:
            print(f"[Cartão {current.numero} - Cor {current.cor}]")
            current = current.proximo

    def atenderPaciente(self):
        if not self.head:
            print("Nenhum paciente na fila.")
        else:
            print(f"Chamando paciente com cartão {self.head.numero} para atendimento.")
            self.head = self.head.proximo


def menu():
    lista_espera = ListaEncadeada()
    while True:
        print("\nMenu:")
        print("1 – Adicionar paciente à fila")
        print("2 – Mostrar pacientes na fila")
        print("3 – Chamar paciente")
        print("4 – Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            lista_espera.inserir()
        elif opcao == '2':
            lista_espera.imprimirListaEspera()
        elif opcao == '3':
            lista_espera.atenderPaciente()
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
