# %% 文字列を分解して、それらを1つのリストにする
strs = ["flower","flow","flight", "anker"]
strs_list = [list(s) for s in strs]
# [['f', 'l', 'o', 'w', 'e', 'r'],
#  ['f', 'l', 'o', 'w'],
#  ['f', 'l', 'i', 'g', 'h', 't']]
# この必要はない。文字列から文字は1つずつ取り出せる。
strs[0][0]

# %%
sorted(strs)
# %%
# *演算子を使うことで、lettersリストを展開して、
# 各リストの要素を対応するものとして組み合わせます。
# この結果、各リストの同じインデックスの文字が結合された
# タプルのペアとして返されます。
ans = ""
for i in zip(*strs):
    if (len(set(i)) == 1):
        ans += i[0]
        break
ans
# この答えは「1文字目から連続して共通する文字」ではなく
# 「すべての単語に共通して含まれる文字」を返す。

# %%
ans = ""
v = sorted(strs)
first = v[0]
last = v[-1]

for i in range(min(len(first), len(last))):
    if first[i] != last[i]:
        print("if: \n")
        print(first[i])
        print(last[i])
        break
    else:
        print("else: \n")
        print(first[i])
        print(last[i])
        ans += first[i]
    print(f"when {i}th answer: {ans}")
ans
# %%
