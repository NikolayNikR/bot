import matplotlib.pyplot as plt


def safeBar(valuos, names, path):
    print('Agg')
    plt.bar(names, valuos)
    plt.savefig(path)


def graph(begin: int, end: int, step: int, func: str, path: str):
    lst_x = [x for x in range(begin, end + 1, step)]
    lst_y = [eval(func) for x in lst_x]

    plt.figure(figsize=(8, 6))
    plt.plot(lst_x, lst_y, label=f"y = {func}")
    plt.title(f"y = {func}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(-1 * end, end)
    plt.ylim(-1 * end, end)
    plt.grid()
    plt.legend()
    plt.savefig(path)


print(graph(1, 10, 1, 'x + 1', 'graf'))
