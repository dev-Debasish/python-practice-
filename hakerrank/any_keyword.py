S = input().strip()

has_alnum = any(c.isalnum() for c in S)
has_alpha = any(c.isalpha() for c in S)
has_digit = any(c.isdigit() for c in S)
has_lower = any(c.islower() for c in S)
has_upper = any(c.isupper() for c in S)

print(has_alnum)
print(has_alpha)
print(has_digit)
print(has_lower)
print(has_upper)

