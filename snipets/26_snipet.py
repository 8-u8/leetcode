# # description translated to Japanese
# 非減少順numsにソートされた整数配列 が与えられた場合、各一意の要素が
# 1 回だけ出現するように重複をその場で削除します。
# 要素の相対的な順序は同じに保たれる必要があります。
# 次に、内の一意の要素の数を返します。numsの一意の要素の数を考慮して、
# numsがk受け入れられるためには、次のことを行う必要があります。
# - numsの最初のk要素が、最初のnumsに存在していた順序で一意の要素を含まれるように変更する。
#   numsの残りの要素は、_で返す。
# - kを返す
# Custom Judge:
# 審査員は次のコードを使用してソリューションをテストします。
'''
int[] nums = [...]; // 入力配列
int[] expectedNums = [...]; // 正しい長さの期待される答え

int k = removeDuplicates(nums); // 実装を呼び出す

assert k == expectedNums.length; 
for (int i = 0; i < k; i++) {
     assert nums[i] == expectedNums[i];
}
'''
# すべてのアサーションに合格すると、ソリューションは受け入れられます。
# 例1:
# 入力: nums = [1,1,2]
# 出力: 2、nums = [1,2,_]
# 説明:
# 関数は k = 2 を返す必要があり、nums の最初の 2 つの要素はそれぞれ 1 と 2 になります。
# 返された k の後に何を残すかは問題ではありません (したがって、それらはアンダースコアです)。

# %%
nums = [1,1,2]


# 例2:
# 入力: nums = [0,0,1,1,1,2,2,3,3,4]
# 出力: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# 説明:関数は k = 5 を返す必要があり、
# nums の最初の 5 つの要素はそれぞれ 0、1、2、3、4 になります。
# 返された k の後に何を残すかは問題ではありません (したがって、それらはアンダースコアです)。
# %%
nums = [0,0,1,1,1,2,2,3,3,4]
nums_set = set(nums)
nums_set

out = ["_"] * len(nums)
for i, num in enumerate(nums_set):
    out[i] = num
k = len(nums_set)
print(f"k: {k}, nums:{out}")


# 制約:
# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums非降順でソートされます。
# %%
def removeDuplicates(nums: list) -> int:
    # init
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j+=1

    return j

# %% assertion check
nums = [0,0,1,1,1,2,2,3,3,4]
print(nums)
k = removeDuplicates(nums=nums)
print(nums)

expectedNums = list(set(nums))

assert k == len(expectedNums)

for i in range(k):
     assert nums[i] == expectedNums[i]

# %%
