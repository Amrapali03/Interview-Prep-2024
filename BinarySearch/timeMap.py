'''
981. Time Based Key-Value Store
Solved
Medium
Topics
Companies
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"

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