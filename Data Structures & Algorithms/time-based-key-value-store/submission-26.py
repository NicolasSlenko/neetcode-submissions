class TimeMap:

    def __init__(self):
        self.kmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kmap:
            self.kmap[key] = [[value, timestamp]]
        else:
            self.kmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kmap:
            return ""
        arr = self.kmap[key]
        print(arr)
        l = 0
        print(l)
        r = len(arr) - 1
        res = ""

        while l <= r:
            m = (l + r)//2
            print("m: " + str(m))
            if arr[m][1] == timestamp:
                print("found")
                return arr[m][0]
            
            if arr[m][1] < timestamp:
                res = arr[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res

