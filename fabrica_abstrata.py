from __future__ import annotations
from abc import ABC, abstractmethod


class FabricaAbstrata(ABC):

    @abstractmethod
    def criar_produto_a(self) -> ProdutoAbstratoA:
        pass

    @abstractmethod
    def criar_produto_b(self) -> ProdutoAbstratoB:
        pass


class FabricaConcreta1(FabricaAbstrata):

    def criar_produto_a(self) -> ProdutoAbstratoA:
        return ProdutoConcretoA1()

    def criar_produto_b(self) -> ProdutoAbstratoB:
        return ProdutoConcretoB1()


class FabricaConcreta2(FabricaAbstrata):

    def criar_produto_a(self) -> ProdutoAbstratoA:
        return ProdutoConcretoA2()

    def criar_produto_b(self) -> ProdutoAbstratoB:
        return ProdutoConcretoB2()


class ProdutoAbstratoA(ABC):

    @abstractmethod
    def funcao_util_a(self) -> str:
        pass


class ProdutoConcretoA1(ProdutoAbstratoA):
    def funcao_util_a(self) -> str:
        return "Resultado do Produto A1."


class ProdutoConcretoA2(ProdutoAbstratoA):
    def funcao_util_a(self) -> str:
        return "Resultado do Produto A2."


class ProdutoAbstratoB(ABC):

    @abstractmethod
    def funcao_util_b(self) -> str:

        pass

    @abstractmethod
    def outra_funcao_util_b(self, colaborador: ProdutoAbstratoA) -> str:

        pass


class ProdutoConcretoB1(ProdutoAbstratoB):
    def funcao_util_b(self) -> str:
        return "Resultado do Produto B1."

    def outra_funcao_util_b(self, colaborador: ProdutoAbstratoA) -> str:
        resultado = colaborador.funcao_util_a()
        return f"Resultado do B1 colaborando com ({resultado})"


class ProdutoConcretoB2(ProdutoAbstratoB):
    def funcao_util_b(self) -> str:
        return "Resultado do Produto B2."

    def outra_funcao_util_b(self, colaborador: ProdutoAbstratoA) -> str:
        resultado = colaborador.funcao_util_a()
        return f"Resultado do B2 colaborando com ({resultado})"


def codigo_cliente(fabrica: FabricaAbstrata) -> None:

    produto_a = fabrica.criar_produto_a()
    produto_b = fabrica.criar_produto_b()

    print(produto_b.funcao_util_b())
    print(produto_b.outra_funcao_util_b(produto_a))


if __name__ == "__main__":

    print("Cliente: Testando com a primeira fábrica:")
    codigo_cliente(FabricaConcreta1())

    print("\n")

    print("Cliente: Testando com a segunda fábrica:")
    codigo_cliente(FabricaConcreta2())