'''


'''

class TimeMap:

    def __init__(self):
        # initialise
        self.store = {}# key=string : value =[list of [val, timestamp]]

    def set(self, key: str, value, timestamp):
        if key not in self.store:
            self.store[key] = [] # insert or defaultdict
        # append values otherwise
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp):
        # if doesnt exist return empty string
        res = ""
        values = self.store.get(key,[]) # if nomatch empty list
        #binary search
        l,r = 0, len(values) - 1
        while l <= r:
            m = (l + r)//2
            # valid <= not >
            if values[m][1] <= timestamp: #[1] as we need timestmp
                # result so far closest
                res = values[m][0]
                l = m + 1
            # invalid value
            else:
                r = m - 1
        return res

obj = TimeMap()
obj.set("foo", "bar", 1)
param_2 = obj.get("foo",1)
print(param_2)
param_3 = obj.get("foo", 3)
print(param_3) # return bar as closest
obj.set("foo", "bar2", 4)
param_4 = obj.get("foo", 4)
print(param_4)
param_5 = obj.get("foo", 5)
print(param_5)