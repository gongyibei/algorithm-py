def heap_sort(arr):
    N = len(arr)
    heap_size = N

    def max_heapify(i):
        l = i if 2 * i + 1 >= heap_size else 2 * i
        r = i if 2 * i + 2 >= heap_size else 2 * i + 1
        M = max(i, l, r, key=lambda i: arr[i])
        if M != i:
            arr[M], arr[i] = arr[i], arr[M]
            max_heapify(M)

    def build_max_heap():
        for i in range(N // 2, -1, -1):
            max_heapify(i)

    build_max_heap()
    for i in range(N - 1, 1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size -= 1
        max_heapify(0)
