def test(a):
    def add(b):
        nonlocal a
        a = a + 1
        return (a + b)
    return (add)
num = int(input())
function= test(num)
print(function(num))