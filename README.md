 LeetCode 401: Binary Watch

Bài toán yêu cầu tìm tất cả các tổ hợp thời gian (giờ:phút) hợp lệ có thể hiển thị trên đồng hồ nhị phân dựa vào số lượng đèn LED đang sáng (`turnOn`). Dưới đây là phân tích và mã nguồn cho hai phương pháp giải quyết.

---

## Phương pháp 1: Vét cạn (Brute Force) & Đếm Bit

Phương pháp này duyệt qua toàn bộ không gian thời gian thực tế: giờ chạy từ $0$ đến $11$, phút chạy từ $0$ đến $59$[cite: 2]. Tổng số bit `1` trong biểu diễn nhị phân của giờ và phút được đếm và so sánh với `turnOn`[cite: 2].

*   Hàm `countBit(n)` chuyển đổi số nguyên thành chuỗi nhị phân bằng `bin(n)[2:]` và đếm số lần xuất hiện của ký tự `'1'`[cite: 2].
*   Hàm `gen_string_time(turnOn)` sử dụng vòng lặp lồng nhau để kiểm tra và trực tiếp trả về chuỗi thời gian bằng lệnh `yield f"{h}:{m:02d}"`[cite: 2].
*   Danh sách cuối cùng được tạo bằng cách ép kiểu generator qua lệnh `return list(gen_string_time(turnOn))`[cite: 2].

### Mã nguồn (`main.py`)


Phương pháp 2: Quay lui (Backtracking) & Generator
Phương pháp này duyệt qua mảng trạng thái gồm 10 bóng đèn với các giá trị quy ước: [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]. Tại mỗi vị trí inx, thuật toán rẽ thành 2 nhánh: chọn bật (cộng giá trị) hoặc không chọn bật. 
	Mảng leds lưu trữ giá trị của 4 bóng đèn giờ và 6 bóng đèn phút. 
	Hàm đệ quy gen_time(inx, cnt, h, m) kiểm soát trạng thái hiện tại. Nhánh đệ quy sẽ bị cắt tỉa (dừng sớm) bằng lệnh return nếu h≥12, m≥60, hoặc inx >= 10. 
	Lệnh yield f"{h}:{m:02d}" được gọi trực tiếp để phát kết quả khi số đèn đã bật bằng với turnOn (cnt == turnOn). 
	Lệnh yield from được sử dụng để liên tục chuyển tiếp kết quả từ các nhánh sâu (nhánh bật đèn cập nhật giờ/phút và nhánh không bật đèn) lên thẳng hàm gọi bên ngoài. 
	Danh sách cuối cùng được tạo bằng cách ép kiểu generator qua lệnh return list(gen_time(0, 0, 0, 0)) sau khi đã loại trừ trường hợp vô lý turnOn >= 9. 


