from pypro.modulos.models import Modulo


def listar_modulos_ordenados() -> list[Modulo]:
    """
    Lista módulos ordenados por títulos
    """

    return list(Modulo.objects.order_by('titulo').all())