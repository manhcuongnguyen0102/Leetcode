class Solution:
    def readBinaryWatch(self,turnOn:int):
        def countBit(n):
            cnt = 0
            bitS = bin(n)[2:]
            for _ in  bitS:
                if(_=='1'):
                    cnt+=1
            return cnt

        def gen_string_time(turnOn):
            for h in range(0,12):
                for m in range(0,60):
                    if(turnOn == countBit(h) + countBit(m)):
                        yield f"{h}:{m:02d}"
        return list(gen_string_time(turnOn))

    
    
