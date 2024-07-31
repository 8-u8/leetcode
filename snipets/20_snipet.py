# %%
# 1. Open brackets must be closed by the same type of brackets.
#    開カッコは同じ形の閉じカッコによって閉じられていなければならない
#    ex: ()<-correct; (}<-incorrect.
# 2. Open brackets must be closed in the correct order.
#    開カッコは正しい順序で閉じられていなければならない
#    ex: ({}) <- correct; {(}) <- incorrect.
# 3. Every close bracket has a corresponding open bracket of the same type.
#    すべての閉じカッコは同じ形の開カッコに対応する
#    ex: ) -> (, } -> {, ] -> [.
# s = "([)]"

# %% 開カッコと閉じカッコが同じ数あればよいのでは
# "([)]"は正しい順序で閉じられていない！
t_f = s.count("(") == s.count(")") and\
      s.count("{") == s.count("}") and\
      s.count("[") == s.count("]")
t_f
# %% 3を具体的に辞書にする
# 1を兼ねている。問題の難しさは2にありそう
bracket_dict = {
    ")": "(",
    "}": "{",
    "]": "["
}

# %% 2の判定
# 正しい順序とは？
s1 = "()[]{}" # pattern1: 独立して閉じている
s2 = "([{}])" # pattern2: ネストして閉じている
s3 = "(){[]}" # pattern3: 1と2のハイブリッド
s4 = "([)]"   # pattern4: NGケース
# stacks = []
# flag = 0
# for i, s in enumerate(s1):
#     if s in bracket_dict.values():
#         stacks.append(s)   
#     elif s in bracket_dict.keys():
#         if not stacks or bracket_dict[s] != stacks.pop():
#             flag += 1

# %%

def isValid(s: str) -> bool:
    stacks = []
    for s_ in s:
        if s_ in bracket_dict.values():
            stacks.append(s_)   
        elif s_ in bracket_dict.keys():
            # list.pop()は最後の位置を取り出す
            # stacksが空でない、またはbracket_dict[s_]がstacksの
            # 最後尾と一致しない場合
            if not stacks or bracket_dict[s_] != stacks.pop():
                return False

    return not stacks
# %%
isValid(s1)
# %%
isValid(s2)
# %%
isValid(s3)
# %%
isValid(s4)
# %%
isValid("((")

# %%
