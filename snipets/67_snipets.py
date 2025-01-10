# %% binary


output = "110"
# 二進法で11+1=110

# %%


def plusOne(digits: List[int]) -> List[int]:
    out = 124
    return out


# %% 入力は2進数めいて文字列
a, b = "1010", "1011"
# %% 10進数換算
a_bin = int(a, 2)
b_bin = int(b, 2)
a_bin, b_bin

# %% 10進数で計算
res = a_bin + b_bin
res
# %% 2進数に変換
bin(res)[2:]
# %%
