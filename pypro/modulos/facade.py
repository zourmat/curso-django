from pypro.modulos.models import Modulo, Aula


def listar_modulos_ordenados() -> list[Modulo]:
    """
    Lista módulos ordenados por parâmetro order
    """

    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)


def listar_aulas_modulo_ordenadas(modulo: Modulo):
    return list(modulo.aula_set.order_by('order').all())


def encontrar_aula(slug):
    return Aula.objects.select_related('modulo').get(slug=slug)
