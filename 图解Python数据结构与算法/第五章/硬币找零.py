def min_coins_change(amount, coins):  
    # 初始化一个无限大的数组来保存每个金额所需的最少硬币数  
    dp = [float('inf')] * (amount + 1)  
    dp[0] = 0  # 金额为0时不需要任何硬币  
  
    # 动态规划填充dp数组  
    for coin in coins:  
        for i in range(coin, amount + 1):  
            dp[i] = min(dp[i], dp[i - coin] + 1)  
  
    # 如果dp[amount]仍然是初始值，说明无法凑齐金额  
    if dp[amount] == float('inf'):  
        return None  
    else:  
        return dp[amount]  
  
def find_min_change(total_payment, item_price, coins):  
    # 计算需要找零的金额  
    change_amount = total_payment - item_price  
      
    # 调用min_coins_change函数计算最少硬币数  
    min_coins = min_coins_change(change_amount, coins)  
      
    # 如果无法凑齐找零金额，返回错误信息  
    if min_coins is None:  
        return "无法找零"  
      
    # 构造找零方案  
    change = []  
    remaining = change_amount  
    for coin in sorted(coins, reverse=True):  
        while remaining >= coin:  
            change.append(coin)  
            remaining -= coin  
      
    return change  
  
# 定义店里有的纸币和硬币面值  
coins = [50, 20, 10, 5, 1]  
  
# 顾客支付的金额和商品的价格  
total_payment = 150  
item_price = 93  
  
# 找出最少找零的纸币和硬币组合  
min_change = find_min_change(total_payment, item_price, coins)  
  
# 输出结果  
if isinstance(min_change, list):  
    print(f"找零方案：{min_change}，共需要{len(min_change)}张纸币或硬币。")  
else:  
    print(min_change)