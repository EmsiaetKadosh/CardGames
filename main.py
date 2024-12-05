n = int(input())
data = []
for i in range(n):
    x, y, t = map(float, input().split())
    data.append((x, y, t))


def v(n, data_):
    V = sum(((data_[i][0] - data_[i + 1][0]) ** 2 + (data_[i][1] - data_[i + 1][1]) ** 2) ** 0.5 for i in range(len(data_) - 1))
    t = data_[n - 1][2] - data_[0][2]
    u = V / t
    return f'{u:.3f}'


m = int(input())
start_end = []
for i in range(m):
    start, end = map(int, input().split())
    start_end.append((start, end))
print(v(n, data))
for m in start_end:
    new_data = data[m[0]:m[1] + 1]
    print(v(m[1] - m[0] + 1, new_data))
