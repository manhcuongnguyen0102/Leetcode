class Solution:
    def readBinaryWatch(self,turnOn: int):
        leds = [8,4,2,1,32,16,8,4,2,1]
        
        def gen_time(inx,cnt,h,m):
            if h>=12 or m>=60:
                return
            if cnt == turnOn:
                yield f"{h}:{m:02d}"
                return
            if inx >= 10:
                return
            if inx<4:
                yield from gen_time(inx+1,cnt+1,h+leds[inx],m)
            else:
                yield from gen_time(inx+1,cnt+1,h,m+leds[inx])
                
            yield from gen_time(inx+1,cnt,h,m)
        if turnOn >=9:
            return[]
        
        return list(gen_time(0,0,0,0))