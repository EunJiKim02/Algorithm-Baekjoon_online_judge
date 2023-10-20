import sys
input = sys.stdin.readline
    
    
def less(a, b):
    if abs(a) < abs(b):
        return True
    elif abs(a) == abs(b) and ( a < b ):
        return True
    else:
        return False



class absheap:
    def __init__(self):
        self.pq = ['']
        self.length = 1
    
    def insert(self, p):
        #새로운 데이터 추가
        self.pq.append(p)
        
        # swim up
        child = self.length
        parent = child // 2
        while (parent > 0) and (less(self.pq[child], self.pq[parent])):
            self.pq[child], self.pq[parent] = self.pq[parent], self.pq[child]
            child = parent
            parent = parent // 2
        self.length += 1
    def print(self):
        print(self.pq)
        
    def delete(self):
        self.pq[1], self.pq[len(self.pq)-1] = self.pq[len(self.pq)-1], self.pq[1]
        min = self.pq.pop() # 마지막에 있는 max 값 제거
        self.length -=1
        idx = 1 # 마지막 원소 k가 있는 root에서 sink 시작
        while 2*idx <= len(self.pq)-1: # 아래에 자식이 있다면 계속 sink 시도
            idxChild = 2*idx
            if idxChild<len(self.pq)-1 and less(self.pq[idxChild+1], self.pq[idxChild]):
                idxChild = idxChild+1 # 두 자식 중 더 큰 자식 찾기
            if less(self.pq[idx], self.pq[idxChild]): break # heap order 만족하면 sink 중단
        # k와 더 큰 자식 swap함으로써 sink
            self.pq[idx], self.pq[idxChild] = self.pq[idxChild], self.pq[idx] 
            idx = idxChild
        return min
        
        
        
        
if __name__ == '__main__':
    N = int(input())
    mypq = absheap()
    for _ in range(N):
        k = int(input())
        if k == 0:
            if mypq.length == 1:
                print(0)
            else:
                print(mypq.delete())
        else:
            mypq.insert(k)
        #print(mypq.print())


