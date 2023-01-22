from pypro.modulos.models import Modulo


def listar_modulos_ordenados() -> list[Modulo]:
    """
    Lista módulos ordenados por parâmetro order
    """

    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)
