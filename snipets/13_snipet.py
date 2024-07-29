# %%
from typing import *

# %%
# とりあえずローマ数字とアラビア数字の対応表を考える
symbol_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
# "LXIV" = 64 because [50, 10, 1, 5]
#%% 
# 例：44を期待する
# M = 1000, CM = 900, XC = 90 and IV = 4                 
s = "XLVI"
# とりあえず分解する
s_list = list(s)
s_list

#%%
# 対応する数字に変換する
s_num = [symbol_dict[x] for x in s]
s_num

# %%
# シンプルな場合(IIIなど)：シンプルに足せば終わり
# IVとか：比較で足す
# s_ans = 0
# i = 0
# for i in range(len(s_num)-1):
#     # 前よりあとが大きければ引き算
#     if s_num[i] < s_num[i+1]:
#         s_ans -= s_num[i]
#     # そうでない場合足し算
#     else:
#         s_ans += s_num[i]
# # 最後に最終桁の数字を足す
# s_ans += s_num[len(s_num)-1]
# s_ans
# %%
s_num_2 = s_num.copy()
# %%
s_num_2
# %%
# "XLIV"->[10,50,1,5]->[5, 1, 50, 10]
# 5は1より大きいので、引き算する
# ans_2 = 5-1 = 4
# 4(ans_2)と50を比べる
# 4は50より小さいので、足し算する
# ans_2 = 4 + 50 = 54
# 50は10より大きいので、引き算する
# ans_2 = 54 - 10 = 44
i = 0
while i < len(s_num_2) - 1:
    if s_num_2[i] < s_num_2[i+1]:
        # 逆にして、次の数が今の数より小さいときに、負にする
        s_num_2[i] *= -1
        print(s_num_2[i])
    i += 1
print(s_num_2)
sum(s_num_2)
# %% 別解：無理やりシンプルな記法に変換する
# s = s.replace("IV", "IIII").replace("IX", "VIIII")
# s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
# s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
