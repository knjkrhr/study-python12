def max_[T](a: T, b: T) -> T:
    return a if a > b else b


max1 = max_(1, 2)
print(max1)

max2 = max_("a", "b")
print(max2)

