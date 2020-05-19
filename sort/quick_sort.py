def quick_sort(arr):
    def partition(p, r):
        key = arr[r]
        i = p
        for j in range(p, r):
            if arr[j] <= key:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[r] = arr[r], arr[i]
        return i

    def _quick_sort(p, r):
        if p < r:
            q = partition(p, r)
            _quick_sort(p, q - 1)
            _quick_sort(q + 1, r)

    _quick_sort(0, len(arr) - 1)
