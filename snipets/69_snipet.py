# %% 開平を求めてください。ただしビルトインの関数を使わずにね。

# %% クソでかい数字に対して厳しい
x =4
# %%
start = 1
end = x
mid = start + (end - start) / 2  # 探索範囲の半分
print(f'calc sqrt of {x}')
print(f'init of start: {start}')
print(f'init of mid: {mid}')
print(f'init of end {end}')
i = 1
while start <= end:
    mid = start + (end - start) / 2
    mid_sq = mid * mid
    if mid_sq > x:  # midの二乗がxより大きい場合：
        # 終点を中央値付近に持ってくる
        end = mid - 1
    elif mid_sq == x:
        break
    else:
        # 始点を中央値付近にもってくる
        start = mid + 1
    print(f'===== loop {i} ======')
    print(f'start in the loop: {start}')
    print(f'mid in the loop: {mid}')
    print(f'end in the loop: {end}')
    i += 1
# %%
