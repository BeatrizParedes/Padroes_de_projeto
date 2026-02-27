# Implementação dos Padrões Criacionais  
## Factory Method e Abstract Factory  

### Disciplina: Requisitos de Software  

---

##  1. Objetivo do Projeto

Este projeto tem como objetivo demonstrar a aplicação prática de dois padrões criacionais de projeto:

- Factory Method (Método Fábrica)
- Abstract Factory (Fábrica Abstrata)

A implementação foi realizada em Python com foco na compreensão da separação de responsabilidades, baixo acoplamento e flexibilidade arquitetural — conceitos fundamentais na Engenharia de Requisitos e na modelagem de sistemas.

---

##  2. Contextualização na Engenharia de Requisitos

Na disciplina de Requisitos, aprendemos que:

- Sistemas devem ser flexíveis a mudanças.
- Requisitos evoluem ao longo do tempo.
- O projeto deve permitir extensibilidade sem modificar código existente.

Os padrões criacionais ajudam a:

✔ Reduzir acoplamento  
✔ Facilitar manutenção  
✔ Permitir extensão sem alterar código cliente  
✔ Atender requisitos de escalabilidade  

Esses padrões são aplicáveis principalmente quando existem requisitos variáveis ou famílias de objetos relacionadas.

---

#  3. Factory Method (Método Fábrica)

Arquivo: `metodo_fabrica.py`

##  Definição

O Factory Method define uma interface para criar um objeto, mas permite que subclasses decidam qual classe instanciar.

Ele delega a criação para subclasses.

##  Estrutura Implementada

- Criador (classe abstrata)
- CriadorConcreto1
- CriadorConcreto2
- Produto (interface)
- ProdutoConcreto1
- ProdutoConcreto2

##  Características

- Baixo acoplamento
- Extensibilidade
- Princípio Aberto/Fechado (Open/Closed Principle)

##  Quando Usar

- Quando não se sabe antecipadamente qual classe será instanciada
- Quando subclasses devem decidir o tipo de objeto criado
- Quando se deseja desacoplar criação de uso

---

#  4. Abstract Factory (Fábrica Abstrata)

Arquivo: `fabrica_abstrata.py`

##  Definição

O Abstract Factory fornece uma interface para criar famílias de objetos relacionados ou dependentes sem especificar suas classes concretas.

Ele garante compatibilidade entre objetos da mesma família.

##  Estrutura Implementada

- FabricaAbstrata
- FabricaConcreta1
- FabricaConcreta2
- ProdutoAbstratoA / ProdutoAbstratoB
- ProdutoConcretoA1 / ProdutoConcretoB1
- ProdutoConcretoA2 / ProdutoConcretoB2

##  Características

- Criação de famílias de objetos
- Garantia de compatibilidade
- Alto nível de abstração
- Facilita troca de variantes

##  Quando Usar

- Quando o sistema precisa trabalhar com múltiplas famílias de objetos
- Quando produtos devem ser compatíveis entre si
- Quando o sistema precisa ser independente da forma como os objetos são criados

---

#  5. Comparação entre os Padrões

| Critério | Factory Method | Abstract Factory |
|-----------|----------------|------------------|
| Foco | Criação de um produto | Criação de famílias de produtos |
| Nível de complexidade | Médio | Alto |
| Estrutura | Uma hierarquia principal | Múltiplas hierarquias |
| Uso comum | Frameworks, plugins | Sistemas multiplataforma |

---

# ▶ 6. Como Executar

## Requisitos

- Python 3 instalado
