
class bubbleSort (object):
    def bSort(self, lst):
        for i in range(len(lst)-1):
            for j in range(len(lst) - 1 - i):
                if lst[j] > lst[j + 1]:
                    lst[j],lst[j+1] = lst[j+1], lst[j]
        return lst

print (bubbleSort().bSort([3,2,1,0]))
