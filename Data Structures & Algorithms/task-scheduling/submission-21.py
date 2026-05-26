class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0

        cnt = Counter(tasks)
        heap = [(-freq, char) for char, freq in cnt.items()]
        heapq.heapify(heap)
        q = collections.deque()

        time = 0
        while heap or q:   
            

            if q and q[0][0] <= time:
                popped = q.popleft()
                freq = popped[1]
                char = popped[2]
                heapq.heappush(heap, (freq,char)) 

            if heap:
                mostFreq = heapq.heappop(heap)
                if mostFreq[0] * -1 > 1:
                    q.append((time + n + 1, mostFreq[0] + 1, mostFreq[1]))   
            time += 1            
        return time 
        