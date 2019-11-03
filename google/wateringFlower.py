#[2,4,5,1,2]
#4

def wateringFlower(cap, flower):
    path = 0
    count = 0
    tank = 0
    for i in range(len(flower)):
        if cap < flower[i]:
            return -1
        if tank < flower[i]:
            count += (path * 2)
            tank = cap
        tank -= flower[i]
        path += 1
    count += path
    return count
# 2+2+4+4+5
arr = [2,4,5,1,2]
res = wateringFlower(6,arr)
print (res)