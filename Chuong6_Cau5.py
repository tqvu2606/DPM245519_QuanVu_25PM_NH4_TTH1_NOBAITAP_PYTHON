"""
Dựa trên list lst, chúng ta có các kết quả sau:

(a) lst là list đầy đủ: [20, 1, -34, 40, -8, 60, 1, 3].

(b) lst[0:3] là một list con chứa các phần tử từ vị trí thứ 0 đến vị trí thứ 2 (không bao gồm vị trí thứ 3): [20, 1, -34].

(c) lst[4:8] là một list con chứa các phần tử từ vị trí thứ 4 đến vị trí thứ 7 (không bao gồm vị trí thứ 8): [-8, 60, 1, 3].

(d) lst[4:33] - Phạm vi này vượt quá số lượng phần tử của lst, nhưng Python vẫn sẽ trả về tất cả các phần tử từ vị trí thứ 4 đến hết: [-8, 60, 1, 3].

(e) lst[-5:-3] là một list con chứa các phần tử từ vị trí thứ 3 từ cuối (bao gồm) đến vị trí thứ 5 từ cuối (không bao gồm): [40, -8].

(f) lst[-22:3] - Phạm vi này trải rộng hơn số lượng phần tử của lst, nhưng Python vẫn sẽ trả về các phần tử từ đầu đến vị trí thứ 2: [20, 1].

(g) lst[4:] là một list con chứa các phần tử từ vị trí thứ 4 đến hết: [-8, 60, 1, 3].

(h) lst[:] là một bản sao của list lst: [20, 1, -34, 40, -8, 60, 1, 3].

(i) lst[:4] là một list con chứa các phần tử từ đầu đến vị trí thứ 3 (không bao gồm vị trí thứ 4): [20, 1, -34, 40].

(j) lst[1:5] là một list con chứa các phần tử từ vị trí thứ 1 đến vị trí thứ 4 (không bao gồm vị trí thứ 5): [1, -34, 40, -8].

(k) -34 in lst kiểm tra xem -34 có trong list lst hay không, kết quả là True.

(l) -34 not in lst kiểm tra xem -34 không có trong list lst hay không, kết quả là False.

(m) len(lst) trả về số lượng phần tử của list lst, tức là 8.


"""
