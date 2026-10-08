class TimeMap:

    def __init__(self):
        self.time_map = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key]=[]
        self.time_map[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        time_name = self.time_map.get(key,[])
        res = ""
        l,h = 0,len(time_name)-1
        while l<=h:
            mid = (h-l)//2 + l
            time = time_name[mid][0]
            if timestamp>=time:
                res = time_name[mid][1]
                l = mid+1
            else:
                h = mid-1
        return res
