# %%
# needleとhaystackが与えられる。
# haystackにneedleが含まれる最初のindexを返す。
# 存在しない場合-1を返す

# %%
haystack = "sadbutsad"
needle = "sad"

haystack.find(needle)
# %%
haystack = "leatcode"
needle = "leato"

haystack.find(needle)

# %%
# もっと早くやる
for i in range(len(haystack)-len(needle)+1):
    if haystack[0:len(needle)]==needle:
        print(i)
    else :
        print(-1)

# %%
