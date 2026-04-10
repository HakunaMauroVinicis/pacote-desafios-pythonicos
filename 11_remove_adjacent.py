"""
11. remove_adjacent

Dada uma lista de números, retorne uma lista onde todos elementos
adjacentes iguais são reduzidos a um único elemento.

Exemplo: [1, 2, 2, 3]
Irá retornar: [1, 2, 3]
"""


def remove_adjacent(nums):
    # +++ SUA SOLUÇÃO +++
    """
    Primeira solução: usando uma lista auxiliar para armazenar os números sem
    adjacentes iguais.
    """
    # lista_num = []
    # for num in nums:
    #     if not lista_num or num != lista_num[-1]:
    #         lista_num.append(num)
    # return lista_num

    """
    Segunda solução: usando uma lista auxiliar para armazenar os números sem
    adjacentes iguais e modificando a lista original.
    """
    # lista_num = []
    # while nums:
    #     num = nums.pop()
    #     if not lista_num or num != lista_num[-1]:
    #         lista_num.append(num)
    # lista_num.reverse()
    # return lista_num

    """
    Terceira solução: usando uma list comprehension para criar uma nova lista
    sem adjacentes iguais.
    """
    # return [num for i, num in enumerate(nums) if i == 0 or num != nums[i - 1]]

    """
    Quarta solução: usando uma função auxiliar para remover adjacentes iguais.
    """
    # def remover_adjacent(nums):
    #     if not nums:
    #         return []
    #     result = [nums[0]]
    #     for num in nums[1:]:
    #         if num != result[-1]:
    #             result.append(num)
    #     return result
    # return remover_adjacent(nums)

    """
    Quinta solução: fazendo tudo na mão sem append, sem usar funções
    auxiliares ou list comprehensions.
    """
    # if not nums:
    #     return []
    # result = [nums[0]]
    # for num in nums[1:]:
    #     if num != result[-1]:
    #         result += [num]
    # return result

    """
    Sexta solução: sendo a mais eficiente possivel usando tudo que tem direito
    de bibliotecas do padrão Pythonico em uma única linha.
    """
    from itertools import groupby
    return [key for key, _ in groupby(nums)]


def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = "✅"
        info = ""
    else:
        sign = "❌"
        info = f"e o correto é {expected!r}"

    print(f"{sign} {f.__name__}({in_!r}) retornou {out!r} {info}")


if __name__ == "__main__":
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(remove_adjacent, [1, 2, 2, 3], [1, 2, 3])
    test(remove_adjacent, [2, 2, 3, 3, 3], [2, 3])
    test(remove_adjacent, [], [])
    test(remove_adjacent, [2, 2, 3, 3, 3, 2, 2], [2, 3, 2])
