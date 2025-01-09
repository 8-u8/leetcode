# %%
digits = [1, 2, 3]

output = [1, 2, 4]
# 123 + 1 = 4

# %%
def plusOne(digits: List[int]) -> List[int]:
    out = 124
    return out

# %%
num = 0
for i, d in enumerate(digits):
    # print(d)
    # print(i)
    p = len(digits) - (i+1)
    a = d * (10 ** p)
    # print(a)
    num += a
num += 1


# %%
out = [int(x) for x in list(str(num))]
out
# %%
