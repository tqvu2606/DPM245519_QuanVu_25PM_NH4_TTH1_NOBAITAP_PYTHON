def oscillate(start, end):
    if start < end:
        for i in range(start, end + 1):
            yield i
            if i != end:
                yield -i
    elif start > end:
        for i in range(start, end - 1, -1):
            yield i
            if i != end:
                yield -i
    else:
        yield start
        yield start

for n in oscillate(-3,5):
    print(n,end=' ')
print()
