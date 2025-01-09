'''
Given a sorted array of distinct integers and a target value, 
互いに異なる昇順ソートされた整数値の配列targetと与えられている。
return the index if the target is found. 
ターゲットが見つかったらそのインデックスを返す
If not, return the index where it would be if it were inserted in order.
見つからなければ、インデックスの代わりに、本来どこにあるべきかを示す
You must write an algorithm with O(log n) runtime complexity.
O(log n)で抑えられるように実装してね。
'''
# %%
nums = [1, 3, 5, 6]
idx  = [0, 1, 2, 3]
target = 5
expectedIndex = 2

# %%
nums = [1, 3, 5, 6]
idx  = [0, 1, 2, 3]
target = 2
expectedIndex = 1 # 1と3の間に入るべきなので

# %%
nums = [1, 3, 5, 6]
idx  = [0, 1, 2, 3]
target = 7
expectedIndex = 4 # 6の次に入るべきなので

# %%