"""
09. front_x

Dada uma lista de strings, retorne a lista com as strings
ordenadas, porém agrupe todas as strings que começam com 'x' primeiro.

Exemplo: ['mix', 'banana' ,'xyz', 'apple', 'xanadu', 'aardvark']
Irá retornar: ['xanadu', 'xyz', 'aardvark', 'apple', 'banana' ,'mix']

Dica: Isso pode ser resolvido criando 2 listas e ordenando cada uma
antes de combina-las.
"""


def front_x(words):
    # +++ SUA SOLUÇÃO +++

    """
    Primeira solução: usando listas auxiliares e ordenando cada uma antes de combina-las.
    """
    # x_list = []
    # other_list = []
    # for word in words:
    #     if word.startswith("x"):
    #         x_list.append(word)
    #     else:
    #         other_list.append(word)
    # x_list.sort()
    # other_list.sort()
    # return x_list + other_list

    """
    Segunda solução: usando list comprehensions e a função sorted.
    """
    # x_list = [word for word in words if word.startswith("x")]
    # other_list = [word for word in words if not word.startswith("x")]
    # return sorted(x_list) + sorted(other_list)

    """
    Terceira solução: usando a função sorted com uma chave de ordenação personalizada.
    """
    # x_list = []
    # other_list = []
    # while words:
    #     word = words.pop()
    #     if word.startswith("x"):
    #         x_list.append(word)
    #     else:
    #         other_list.append(word)
    # x_list.sort()
    # other_list.sort()
    # return x_list + other_list

    """
    Quarta solução: usando a função sorted com uma chave de ordenação personalizada.
    """
    # def order_key(word):
    #     return (not word.startswith("x"), word)

    # return sorted(words, key=order_key)

    """
    Quinta solução: usando a função sorted com uma chave de ordenação personalizada e uma função lambda.
    """
    return sorted(words, key=lambda word: (not word.startswith("x"), word))


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---


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
    test(
        front_x,
        ["bbb", "ccc", "axx", "xzz", "xaa"],
        ["xaa", "xzz", "axx", "bbb", "ccc"],
    )
    test(
        front_x,
        ["ccc", "bbb", "aaa", "xcc", "xaa"],
        ["xaa", "xcc", "aaa", "bbb", "ccc"],
    )
    test(
        front_x,
        ["mix", "xyz", "apple", "xanadu", "aardvark"],
        ["xanadu", "xyz", "aardvark", "apple", "mix"],
    )
