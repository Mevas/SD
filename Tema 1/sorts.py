import time


def timeit(f):
    def timed(*args, **kw):
        ts = time.clock()
        result = f(*args, **kw)
        te = time.clock()

        print('func:%r args:[%r, %r] took: %2.4f sec' % (f.__name__, args, kw, te - ts))
        return result

    return timed


class Sorter:
    start_time = 0

    def start_timer(self):
        self.start_time = time.time()

    def end_timer(self):
        return round(time.time() - self.start_time, 6)

    def is_sorted(self, arr, original):
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

    # Bubble sort
    def bubble_sort(self, array):
        arr = array[:]

        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr

    def count_sort(self, array):
        # Daca este gol, returnam o lista goala
        if not array:
            return []

        # Cream array-ul ce va fi sortat
        arr = []

        # Verificare necesara pentru a evita eroare de memorie in cazul numerelor mult prea mari, cu count sort
        if max(array) >= 10 ** 7:
            # print(f'Count sort nu poate sorta liste ce contin numere atat de mari. - {array}')
            return sorted(array)

        # Initializam vectorul de frecventa
        counts = [0] * (max(array) + 1)

        # Umplem vectorul de frecventa
        for nr in array:
            counts[nr] += 1

        # Cream vectorul sortat
        for nr in range(max(array) + 1):
            for _ in range(counts[nr]):
                arr.append(nr)

        return arr

    def _get_digit(self, num, digit, base):
        return (num // digit) % base

    def _radix_count(self, array, digit, base):
        counts = [0] * base
        temp = [0] * len(array)

        for num in array:
            counts[self._get_digit(num, digit, base)] += 1

        for i in range(1, base):
            counts[i] += counts[i - 1]

        for i in range(len(array) - 1, -1, -1):
            counts[self._get_digit(array[i], digit, base)] -= 1
            temp[counts[self._get_digit(array[i], digit, base)]] = array[i]

        return temp

    def radix_sort(self, array, base=10):
        if not array:
            return array

        max_el = max(array)

        i = 1
        while max_el / i > 0:
            array = self._radix_count(array, i, base)
            i *= base

        return array

    def merge_sort(self, array):
        if len(array) <= 1:
            return array

        middle = len(array) // 2
        L = array[:middle]
        R = array[middle:]

        self.merge_sort(L)
        self.merge_sort(R)

        i = j = new_index = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[new_index] = L[i]
                i += 1
            else:
                array[new_index] = R[j]
                j += 1

            new_index += 1

        while i < len(L):
            array[new_index] = L[i]
            new_index += 1
            i += 1

        while j < len(R):
            array[new_index] = R[j]
            new_index += 1
            j += 1

        return array

    def _quick_sort(self, array, left, right):
        if not array:
            return array

        pivot = array[(left + right) // 2]

        i = left
        j = right

        while i <= j:
            while array[i] < pivot:
                i += 1
            while array[j] > pivot:
                j -= 1

            if i <= j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1

        if left < j:
            self._quick_sort(array, left, j)

        if i < right:
            self._quick_sort(array, i, right)

        return array

    def quick_sort(self, arr):
        array = arr[:]

        return self._quick_sort(array, 0, len(array) - 1)

    @staticmethod
    def native_sort(arr):
        return sorted(arr)
