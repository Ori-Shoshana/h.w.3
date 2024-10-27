import sys
sys.setrecursionlimit(2000)  # מגדילים את העומק המקסימלי לרקורסיה

def create_tuple_regular(n):
    if n == 0:
        return ()
    else:
        return create_tuple_regular(n - 1) + (n,)

# קריאה לפונקציה
result_regular = create_tuple_regular(1000)
print(result_regular)

def create_tuple_tail(n, acc=()):
    if n == 0:
        return acc
    else:
        return create_tuple_tail(n - 1, (n,) + acc)

# קריאה לפונקציה
result_tail = create_tuple_tail(1000)
print(result_tail)

def sum_tuple_regular(t):
    if not t:
        return 0
    else:
        return t[0] + sum_tuple_regular(t[1:])

# קריאה לפונקציה על הטופל שיצרנו
sum_regular = sum_tuple_regular(result_regular)
print(sum_regular)

def sum_tuple_tail(t, acc=0):
    if not t:
        return acc
    else:
        return sum_tuple_tail(t[1:], acc + t[0])

# קריאה לפונקציה על הטופל שיצרנו
sum_tail = sum_tuple_tail(result_tail)
print(sum_tail)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm_regular(a, b):
    return (a * b) // gcd(a, b)

# דוגמה לקריאה
lcm_result_regular = lcm_regular(6, 4)

def lcm_tail(a, b):
    return (a * b) // gcd(a, b)

# דוגמה לקריאה
lcm_result_tail = lcm_tail(6, 4)

print(lcm_result_regular,lcm_result_tail)

def is_palindrome_regular(n):
    s = str(n)
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome_regular(int(s[1:-1]))

# דוגמה לקריאה
palindrome_result_regular = is_palindrome_regular(123454321)

def is_palindrome_tail(n, s=None):
    if s is None:
        s = str(n)
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome_tail(n, s[1:-1])

# דוגמה לקריאה
palindrome_result_tail = is_palindrome_tail(123454321)

print(palindrome_result_regular,palindrome_result_tail)

def sortedzip_regular(lists):
    sorted_lists = [sorted(lst) for lst in lists]
    return list(zip(*sorted_lists))

# דוגמה לקריאה
sortedzip_result_regular = sortedzip_regular([[3, 1, 2], [5, 6, 4], ['a', 'b', 'c']])

def sortedzip_tail(lists, acc=None):
    if acc is None:
        sorted_lists = [sorted(lst) for lst in lists]
        return list(zip(*sorted_lists))

# דוגמה לקריאה
sortedzip_result_tail = sortedzip_tail([[3, 1, 2], [5, 6, 4], ['a', 'b', 'c']])

print(sortedzip_result_regular,sortedzip_result_tail)

import time
import sys

def create_array_no_lazy():
    start_time = time.time()
    arr = [i for i in range(10001)]
    end_time = time.time()
    execution_time = end_time - start_time
    memory_size = sys.getsizeof(arr)
    
    return arr, execution_time, memory_size

# קריאה לפונקציה
array_no_lazy, time_no_lazy, size_no_lazy = create_array_no_lazy()
print(f"time : {time_no_lazy}, size : {size_no_lazy} bytes")

def create_array_lazy():
    start_time = time.time()
    arr = (i for i in range(10001))  # Generator expression
    end_time = time.time()
    execution_time = end_time - start_time
    memory_size = sys.getsizeof(arr)
    
    return arr, execution_time, memory_size

# קריאה לפונקציה
array_lazy, time_lazy, size_lazy = create_array_lazy()
print(f"time : {time_lazy}, size : {size_lazy} bytes")


def first_5000_no_lazy():
    start_time = time.time()
    arr, _, _ = create_array_no_lazy()
    first_5000 = arr[:5000]
    end_time = time.time()
    execution_time = end_time - start_time
    memory_size = sys.getsizeof(first_5000)
    
    return first_5000, execution_time, memory_size, type(first_5000)

# קריאה לפונקציה
first_5000_array_no_lazy, time_5000_no_lazy, size_5000_no_lazy, type_5000_no_lazy = first_5000_no_lazy()
print(f"time : {time_5000_no_lazy}, size : {size_5000_no_lazy} bytes, type : {type_5000_no_lazy}")


def first_5000_lazy():
    start_time = time.time()
    arr, _, _ = create_array_lazy()
    first_5000 = (next(arr) for _ in range(5000))  # Lazy Evaluation
    end_time = time.time()
    execution_time = end_time - start_time
    memory_size = sys.getsizeof(first_5000)
    
    return first_5000, execution_time, memory_size, type(first_5000)

# קריאה לפונקציה
first_5000_array_lazy, time_5000_lazy, size_5000_lazy, type_5000_lazy = first_5000_lazy()
print(f"time: {time_5000_lazy}, size: {size_5000_lazy} bytes, type : {type_5000_lazy}")

def prime_generator():
    num = 2
    while True:
        is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
        if is_prime:
            yield num
        num += 1

# דוגמה לשימוש
gen = prime_generator()
print(next(gen))  # מחזיר את המספר הראשוני הראשון
print(next(gen))  # מחזיר את המספר הראשוני הבא

import math

def taylor_series_generator(x):
    n = 0
    sum_series = 0
    while True:
        term = (x ** n) / math.factorial(n)
        sum_series += term
        yield sum_series
        n += 1

# דוגמה לשימוש
gen = taylor_series_generator(2)
for _ in range(8):
    print(next(gen))  # מחזיר את הסכום של הטור לאחר הוספת האיבר הבא

