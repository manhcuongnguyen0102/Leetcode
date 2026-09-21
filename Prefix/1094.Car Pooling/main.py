class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        diff = [0]*1001
        for numPass,Pfrom,to in trips:
            diff[Pfrom]+= numPass
            diff[to]-=numPass
        current_pass = 0
        for i in diff:
            current_pass+= i
            if current_pass > capacity:
                return False
        return True