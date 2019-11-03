class QuickSort:

    def quicksort(self, array2, l, r):
        if l < r:
            index = self.partion(array2, l, r)
            self.quicksort(array2, l, index)
            self.quicksort(array2, index + 1, r)

    def partion(self,array, low, high):
        s = array[low]

        while low < high:

            while low < high and s <= array[high]:
                high -= 1
            if low < high:
                array[low] = array[high]
            while low < high and s > array[low]:
                low += 1
            if low < high:
                array[high] = array[low]
        array[low] = s
        return low

if __name__ == '__main__':
    array2 = [9, 3, 2, 1, 4, 6, 7, 0, 5]

    print(array2)
    QuickSort().quicksort(array2, 0, 8)
    print(array2)
