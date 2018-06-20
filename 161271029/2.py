#2


def main():
    n = int(input())
    inputVec = input().split()
    a = []
    for i in range(n):
        a.append(int(inputVec[i]))
    queue = [[], [], []]
    queueCnt = [0] * 3
    for i in range(n):
        minIdx = queueCnt.index(min(queueCnt))
        #print(minIdx)
        queueCnt[minIdx] += 1
        queue[minIdx].append(a[i])
    cntOld = 0
    cntForEach = [0] * 3
    finishPoint = max(sum(queue[0]), sum(queue[1]), sum(queue[2]))
    for i in range(len(queue)):
        while len(queue[i]) != 0:
            q = queue[i]
            cntForEach[i] += q[0] * (len(q) - 1)
            queue[i].pop(0)
    cntOld = sum(cntForEach)
    print(cntOld, finishPoint)

    queue = [[], [], []]
    cntNew = 0

    for i in range(len(a)):
        queue[0].append(a[i])
    #print(queue)
    finishPoint = 0
    while len(queue[0]) != 0:
        # queue[0][0] in process
        finishPoint += queue[0][0]
        # moving
        if len(queue[1]) == 0 and len(queue[0]) >= 2:
            queue[1].append(queue[0][1])
            queue[0].pop(1)
        if len(queue[2]) == 0 and len(queue[0]) >= 2:
            queue[2].append(queue[0][1])
            queue[0].pop(1)
        #waiting
        cntNew += queue[0][0] * (len(queue[0]) - 1)
        #queue[0] finished
        if len(queue[1]) > 0:
            queue[1][0] -= queue[0][0]
            if queue[1][0] <= 0:
                queue[1].pop(0)
        if len(queue[2]) > 0:
            queue[2][0] -= queue[0][0]
            if queue[2][0] <= 0:
                queue[2].pop(0)
        queue[0].pop(0)
    if len(queue[1]) > 0:
        finishPoint += queue[1][0]
    if len(queue[2]) > 0:
        finishPoint += queue[2][0]
    print(cntNew, finishPoint)


if __name__ == '__main__':
    main()