"""
12. linear_merge

Dada duas listas ordenadas em ordem crescente, crie e retorne uma lista
com a combinação das duas listas, também em ordem crescente. Você pode
modificar as listas recebidas.

A sua solução deve rodar em tempo linear, ou seja, deve fazer uma
única passagem em cada uma das listas.
"""


def linear_merge(list1, list2):
    # +++ SUA SOLUÇÃO +++
    """
    Primeira solução: usando o método pop(0) para remover o primeiro
    elemento de cada lista e compará-los.
    """
    """
    ❌ solução não respeita o tempor linear, pois pop(0) tem
        complexidade O(n) para listas.
    """
    # lista_merge = []
    # while list1 and list2:
    #     if list1[0] < list2[0]:
    #         lista_merge.append(list1.pop(0))
    #     else:
    #         lista_merge.append(list2.pop(0))
    # lista_merge.extend(list1)
    # lista_merge.extend(list2)
    # return lista_merge

    """
    Segunda solução: usando a função sorted para ordenar a concatenação das
    duas listas.
    """
    """
    ❌ solução não respeita o tempo linear, pois sorted tem complexidade
        O(n log n).
    """
    # return sorted(list1 + list2)

    """
    Terceira solução: usando recursão para comparar o primeiro elemento de cada
    lista e construir a lista resultante.
    """
    """
    ❌ solução não respeita o tempo linear, pois a recursão pode levar a uma
        complexidade O(n^2) no pior caso, dependendo do tamanho das listas.
    """
    # def merge(list1, list2):
    #     if not list1:
    #         return list2
    #     if not list2:
    #         return list1
    #     if list1[0] < list2[0]:
    #         return [list1[0]] + merge(list1[1:], list2)
    #     else:
    #         return [list2[0]] + merge(list1, list2[1:])
    # return merge(list1, list2)

    """
    Quarta solução: usando o pop(0) para remover o ultimo elemento de cada
    lista e compará-los, construindo a lista resultante de trás para frente.
    """
    # lista_merge = []
    # while list1 and list2:
    #     if list1[-1] > list2[-1]:
    #         lista_merge.append(list1.pop())
    #     else:
    #         lista_merge.append(list2.pop())
    # lista_merge.extend(reversed(list1))
    # lista_merge.extend(reversed(list2))
    # return list(reversed(lista_merge))

    """
    Quinta solução: usando o repr para comparar os elementos das listas e
    construir a lista resultante.
    """
    # i = j = 0
    # lista_merge = []

    # while i < len(list1) and j < len(list2):
    #     if repr(list1[i]) < repr(list2[j]):
    #         lista_merge.append(list1[i])
    #         i += 1
    #     else:
    #         lista_merge.append(list2[j])
    #         j += 1

    # lista_merge.extend(list1[i:])
    # lista_merge.extend(list2[j:])
    # return lista_merge

    """
    Sexta solução: usando tudo que o python tem de melhor para
    resolver o problema de forma eficiente respeitando o tempo linear.
    """
    import heapq
    return list(heapq.merge(list1, list2))

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---


def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = "✅"
        info = ""
    else:
        sign = "❌"
        info = f"e o correto é {expected!r}"

    print(f"{sign} {f.__name__}{in_!r} retornou {out!r} {info}")


if __name__ == "__main__":
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(
        linear_merge, (["aa", "xx", "zz"], ["bb", "cc"]), ["aa", "bb", "cc", "xx", "zz"]
    )
    test(
        linear_merge, (["aa", "xx"], ["bb", "cc", "zz"]), ["aa", "bb", "cc", "xx", "zz"]
    )
    test(
        linear_merge, (["aa", "aa"], ["aa", "bb", "bb"]), ["aa", "aa", "aa", "bb", "bb"]
    )
