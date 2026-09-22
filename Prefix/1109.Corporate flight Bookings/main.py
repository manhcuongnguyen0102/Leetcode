class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        diff = [0]*(n+1)
        for first,last,seats in bookings:
            diff[first-1]+=seats
            diff[last]-=seats
        for i in range(1,n):
            diff[i]+=diff[i-1]
        return diff[:n]
    #muốn cộng 1 dãy từ khoảng[a->b] 1 số V thì dùng mảng hiệu sẽ thấy số ngoài đầu sẽ +v và ngoài số cuối -V