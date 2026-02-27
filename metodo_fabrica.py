from __future__ import annotations
from abc import ABC, abstractmethod


class Criador(ABC):

    @abstractmethod
    def metodo_fabrica(self):

        pass

    def alguma_operacao(self) -> str:

        produto = self.metodo_fabrica()

        resultado = f"Criador: O mesmo código do criador trabalhou com {produto.operacao()}"

        return resultado


class CriadorConcreto1(Criador):

    def metodo_fabrica(self) -> Produto:
        return ProdutoConcreto1()


class CriadorConcreto2(Criador):
    def metodo_fabrica(self) -> Produto:
        return ProdutoConcreto2()


class Produto(ABC):

    @abstractmethod
    def operacao(self) -> str:
        pass


class ProdutoConcreto1(Produto):
    def operacao(self) -> str:
        return "{Resultado do ProdutoConcreto1}"


class ProdutoConcreto2(Produto):
    def operacao(self) -> str:
        return "{Resultado do ProdutoConcreto2}"


def codigo_cliente(criador: Criador) -> None:

    print(
        f"Cliente: Não sei qual é a classe do criador, mas ainda funciona.\n"
        f"{criador.alguma_operacao()}",
        end=""
    )


if __name__ == "__main__":
    print("Aplicação: Iniciada com CriadorConcreto1.")
    codigo_cliente(CriadorConcreto1())
    print("\n")

    print("Aplicação: Iniciada com CriadorConcreto2.")
    codigo_cliente(CriadorConcreto2())