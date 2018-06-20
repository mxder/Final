# 3

class M:
    def __init__(self, t, a, d):
        self.t = t
        self.a = a
        self.d = d

class N:
    def __init__(self, t, v):
        self.t = t
        self.v = v

def main():
    m = int(input())
    mVec = []
    for i in range(m):
        inputVec = input().split()
        mVec.append(M(int(inputVec[0]), int(inputVec[1]), int(inputVec[2])))
    n = int(input())
    nVec = []
    for i in range(n):
        inputVec = input().split()
        nVec.append(N(int(inputVec[0]), int(inputVec[1])))
    cnt = 0
    for m in mVec:
        price = 0
        for n in nVec:
            if m.t < n.t:
                break
            price = n.v
        if m.d == 1:
            totalStock = m.a * 100
            guohu = totalStock // 1000
            tongxun = 1
            jiaoyie =  totalStock * price
            yongjin = totalStock * 0.002
            if yongjin < 5:
                yongjin = 5
            cnt -= jiaoyie + tongxun + yongjin + guohu
        if m.d == 2:
            totalStock = m.a * 100
            guohu = totalStock // 1000
            tongxun = 1
            jiaoyie = totalStock * price
            yongjin = totalStock * 0.002
            yinhua = jiaoyie * 0.001
            if yongjin < 5:
                yongjin = 5
            cnt += jiaoyie - tongxun - yongjin - guohu - yinhua
    print("%.2f" % cnt)


if __name__ == '__main__':
    main()