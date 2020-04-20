# 最高的年终奖,最大购物数量
N, M = 3200, 60
# 不同年终奖的最大乘积和,初始值都为0.
f = [0] * N
# 分组背包，每组有四种情况，[a.主件, b.主件+附件1 ,c.主件+附件2, d.主件+附件1+附件2]
item_prices = [[0 for i in range(4)] for j in range(M)]  # 价格
item_values = [[0 for i in range(4)] for j in range(M)]  # 四种情况下的价值与价格乘积之和
# 实际年终奖钱数,希望购买物品的个数
n, m = map(int, input().split())
n = n // 10  # 价格为10的整数倍，节省时间
# 从1 开始,购买0件无乘积
for i in range(1, m + 1):
    price, value, main_index = map(int, input().split())
    price = price // 10
    # 是主件
    if main_index == 0:
        for t in range(4):
            item_prices[i][t], item_values[i][t] = item_prices[i][t] + price, item_values[i][t] + price * value
    # 是附件1
    elif item_prices[main_index][1] == item_prices[main_index][0]:  # 如果a==b，添加附件1(如果a=b=c=d说明没有附件)
        item_prices[main_index][1], item_values[main_index][1] = item_prices[main_index][1] + price, item_values[main_index][1] + price * value
        item_prices[main_index][3], item_values[main_index][3] = item_prices[main_index][3] + price, item_values[main_index][3] + price * value
    else:  # 添加附件2
        item_prices[main_index][2], item_values[main_index][2] = item_prices[main_index][2] + price, item_values[main_index][2] + price * value
        item_prices[main_index][3], item_values[main_index][3] = item_prices[main_index][3] + price, item_values[main_index][3] + price * value
'''
dp:
从购买最后一组物品开始考虑,fn= 最后一组物品价格价值之和最大,和剩余购买组的和.
而剩余购买的组肯定也是和最大的,不然最优解不成立. 这和原来的问题是一样的,只不过购买组数量规模减少了,也就是子问题.
所以状态确定了:最优策略的最后一步,子问题.
f
然后确定转移方程: f[j]= max(f(j-第一组价格)+第一组和,.......)
'''
# 假设只购买一件开始
for i in range(1, m + 1):
    # 钱要从高往低递减,不可以从0开始,因为给定一组物品时,如果钱从1开始的话,
    # n:购物总资金上限，只能倒序遍历，因为背包的思维是可用空间从大到小，求当前每个子状态的最优，
    # 如果顺序遍历，背包容量变大，之前遍历的子状态的最优结论就被推翻了
    for j in range(n, -1, -1):

    # for j in range(n):
        # 确定购买哪一组情况乘积之和最大
        for k in range(4):
            if j >= item_prices[i][k]:
                # max中有f[j],就是在和前一组对比
                f[j] = max(f[j], f[j - item_prices[i][k]] + item_values[i][k])
print(10 * f[n])
