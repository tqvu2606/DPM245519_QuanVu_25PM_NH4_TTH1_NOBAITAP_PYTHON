"""
Dựa trên list lst và giá trị x, chúng ta có các kết quả sau:

(a) lst[0] là phần tử đầu tiên của list lst, tức là 3.

(b) lst[3] là phần tử thứ 3 của list lst, tức là 5.

(c) lst[x], với x = 2, là lst[2], là phần tử thứ 2 của list lst, tức là 1.

(d) lst[-x], với x = 2, là lst[-2], là phần tử thứ 2 từ cuối của list lst, tức là 5.

(e) lst[x + 1], với x = 2, là lst[3], là phần tử thứ 3 của list lst, tức là 5.

(f) lst[x] + 1, với x = 2, là lst[2] + 1, tức là 1 + 1 = 2.

(g) lst[lst[x]], với x = 2, là lst[lst[2]], là lst[1], là phần tử thứ 1 của list lst, tức là 0.

(h) lst[lst[lst[x]]], với x = 2, là lst[lst[1]], là lst[0], là phần tử đầu tiên của list lst, tức là 3.

Vậy, các kết quả là:

(a) 3
(b) 5
(c) 1
(d) 5
(e) 5
(f) 2
(g) 0
(h) 3


"""
