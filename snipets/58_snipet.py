# %%
def lengthOfLastWord(s: str) -> int:
    s = [s for s in s.split(' ') if s]

    s_list = list(s[-1])

    out = len(s_list)

    return out

# %%
s = "   fly me   to   the moon  "
# %%
# 空白を破壊する場合はリスト内包表記
splitted_s = [s for s in s.split(' ') if s]
splitted_s
# %%
last_words = splitted_s[-1]

# %%
last_words_2 = list(last_words)
last_words_2
# %%
len(last_words_2)
# %%
lengthOfLastWord("luffy")
# %%
