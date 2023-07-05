a = "&&&&&&&&Hello &&  World&&&&&"
print(a.strip('&'))
print(a.lstrip('&'))
print(a.rstrip('&'))

str = "-"
seq = ("Arls", "Bls", "will", "be", "joined")

print(str.join(seq))

s="hello world"
print( " ".join(s))

# Ljust, rjust. These pad strings. They accept one or two arguments. The first argument is the total length of the result string. The second is the padding character.
# Tip: If you specify a number that is too small, ljust and rjust do nothing. They return the original string.

p = "Hello"
print(p.ljust(10, "."))
print(p.rjust(10, "."))
print(p.center(30, "."))