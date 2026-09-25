class Pedido:
    def __init__(self, cliente: str, valor_base: float):
        self.cliente = cliente
        self.valor_base = valor_base
        self.itens: list[str] = []
        self._desconto: float = 0.0  # Atributo protegido

    @property
    def desconto(self) -> float:
        return self._desconto

    @desconto.setter
    def desconto(self, valor: float):
        # Validação do invariante de negócio
        if valor < 0:
            raise ValueError("O desconto não pode ser negativo.")
        if valor > 0.50:
            raise ValueError("O desconto máximo permitido é de 50%.")
        self._desconto = valor

    # Método 1: Adicionar item ao pedido
    def adicionar_item(self, item: str) -> None:
        if not item.strip():
            raise ValueError("Nome do item não pode ser vazio.")
        self.itens.append(item)

    # Método 2: Calcular total com desconto aplicado
    def calcular_total(self) -> float:
        return self.valor_base * (1 - self._desconto)





    import pytest
from pedido import Pedido

def test_criar_pedido_e_adicionar_itens():
    pedido = Pedido(cliente="Ana", valor_base=100.0)
    pedido.adicionar_item("Caderno")
    
    assert pedido.cliente == "Ana"
    assert "Caderno" in pedido.itens

def test_calcular_total_com_desconto_valido():
    pedido = Pedido(cliente="Carlos", valor_base=200.0)
    pedido.desconto = 0.10  # 10% de desconto
    
    assert pedido.calcular_total() == 180.0

def test_invariante_desconto_invalido():
    pedido = Pedido(cliente="Beatriz", valor_base=100.0)
    
    # Testa a proteção contra desconto negativo
    with pytest.raises(ValueError, match="O desconto não pode ser negativo."):
        pedido.desconto = -0.05

    # Testa a proteção contra desconto acima do limite
    with pytest.raises(ValueError, match="O desconto máximo permitido é de 50%."):
        pedido.desconto = 0.60



pytest -v
