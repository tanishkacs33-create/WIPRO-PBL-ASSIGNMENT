# Initial values
a = 10
b = 20
c = 30

print(f"Before shift: a = {a}, b = {b}, c = {c}")

# Python allows simultaneous assignment without a manual temporary variable
a, b, c = c, a, b

print(f"After shift:  a = {a}, b = {b}, c = {c}")