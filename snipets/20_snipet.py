# %%
# 1. Open brackets must be closed by the same type of brackets.
#    開カッコは同じ形の閉じカッコによって閉じられていなければならない
# 2. Open brackets must be closed in the correct order.
#    開カッコは正しい順序で閉じられていなければならない
# 3. Every close bracket has a corresponding open bracket of the same type.
#    すべての閉じカッコは同じ形の開カッコに対応する
s = "([)]"

# %%
# ()の対応関係のチェックをする
t_f = ("(" in s and ")" in s) or\
      ("{" in s and "}" in s) or\
      ("[" in s and "]" in s)
t_f # これだけだと "()[]{}{}{"でもTrue。
# %%
bracket_dict = {
    ")":"(",
    "}":"{",
    "]":"["
}

# %% 開カッコと閉じカッコが同じ数あればよいのでは
# 正しい順序で閉じられていない！
t_f_2 = s.count("(") == s.count(")") and\
        s.count("{") == s.count("}") and\
        s.count("[") == s.count("]")
t_f_2
# %%
