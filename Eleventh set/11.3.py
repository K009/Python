def swap(L, left, right):
    """Zamiana miejscami dwóch elementów na liście."""
    # L[left], L[right] = L[right], L[left]
    item = L[left]
    L[left] = L[right]
    L[right] = item

cmp = lambda x, y: (x > y) - (x < y)


def insertsort(L, left, right, cmpfunc=cmp):
    for i in range(left+1, right+1):
        for j in range(i, left, -1):   # od prawej do lewej (bez left)
            if cmpfunc(L[j-1], L[j]) < 0:
                swap(L, j-1, j)   # zamiana sąsiadów

if __name__ == "__main__":
    example_list = [1, 2, 3, 121, -8, 64, 22, 7]
    # sortowanie w odwrotnej kolejności
    insertsort(example_list, 0, 7, cmpfunc=lambda x, y: -cmp(x, y))
    print(example_list)