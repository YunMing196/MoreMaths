from MoreMaths import *
print("======数学计算======")
print(f"阶乘计算：5！ = {Factorial(5)}")
print(f"阶乘计算：7! = {Factorial(7)}")
print(f"斐波那契第 {12} 项为：{Fibonacci_recursive_One(12)}")
print(f"斐波那契前 {12} 项为：{Fibonacci_recursive_All(12)}")
print(f"排列数计算：Arrangement{(15,12)} 计算结果为：{Arrangement(15,12)}")
print(f"组合数计算：Combination{(15,12)} 计算结果为：{Combination(15,12)}")
print(f"{12,8} 的最大公因数为：{Public_Max(12,8)}")
print(f"{12,8} 的最小公倍数为：{Public_Min(12,8)}")
print(f"{15} 是质数"if ifPrime(15) else f"{15} 不是质数")
print(f"{17} 是质数"if ifPrime(17) else f"{17} 不是质数")
print(f"平面直角坐标 {3,4} -->极坐标 {Pol(3,4)}")
print(f"极坐标 {5,120} -->平面直角坐标 {Rec(5,120)}")
QinJiuShao(6,6,6,RP_mode=True)
HaiLun(3,4,5, RP_mode=True)
L1 = [15,2,6,8,2,2]
print(f"原列表：{L1}, 搜查数字 {2}")
Find_All(L1,2,RP_mode=True)
Find_One(L1,2,2,RP_mode=True)
Factorization(15,RP_mode=1)
print(f"{375} 和 {5} 的关系为： ",end="")
Base_Decomp(375,5,RP_mode=True)
print(f"{16}是完全平方数" if Perfect_Square(16) else f"{16}不是完全平方数")
print(f"{17}是完全平方数" if Perfect_Square(17) else f"{17}不是完全平方数")
sqrt_reduce(16,RP_mode=True)
sqrt_reduce(18,RP_mode=True)
sqrt_reduce(72,RP_mode=True)

print(f"{100000}以内自幂数：")
for i in range(100001):
    if self_power_num(i) :
        print(i,end="\t")

print(f"{100}以内质数：")
for i in range(101):
    if ifPrime(i) :
        print(i,end="\t")
print()
print()
print("======列表统计=====")
L2 = DataStat(120,30,90,60,60)
print(f"原列表：{L2.get()}")
print(f"第{2}项：{L2.get()[2]}")
L2.get().sort()
print(f"排序后：{L2.get()}")
print(f"算术平均值：{L2.Arithmetic_mean()}")
print(f"加权平均值：{L2.Weighted_mean()}")
print(f"平均绝对偏差：{L2.MadCalculator()}")
print(f"平均距离：{L2.Distance_Mean()}")
print(f"总体 / 样本方差： {L2.Variance(ddot=0)} / {L2.Variance(ddot=1)}")
print(f"总体 / 样本标准差： {L2.Std_Dev(ddot=0)} / {L2.Std_Dev(ddot=1)}")
print(f"中位数：{L2.Median()}")
print(f"众数：{L2.Mode()}")
print(f"极差：{L2.Data_Range()}")
print(f"累乘：{L2.List_Product()}")
print(f"异常数：{L2.Error_Num()}")
print(f"最大值 / 最小值：{max(L2.get())} / {min(L2.get())}")
print()
print("======逻辑运算======")
RP_mode = False
for i in (0, 1):
    print(f"{i} 进行非运算 {Bool_Sum.NOT(i)}")
    for j in (0,1):
        print(f"{i, j} 进行与运算 {Bool_Sum.AND(i,j,RP_mode)}")
        print(f"{i, j} 进行或运算 {Bool_Sum.OR(i,j,RP_mode)}")
        print(f"{i, j} 进行异或运算 {Bool_Sum.XOR(i,j,RP_mode)}")
        print(f"{i, j} 进行同或运算 {Bool_Sum.XNOR(i,j,RP_mode)}")
        print(f"{i, j} 进行与非运算 {Bool_Sum.NAND(i,j,RP_mode)}")
        print(f"{i, j} 进行或非运算 {Bool_Sum.NOR(i,j,RP_mode)}")
        print(f"{i, j} 进行半加运算 {Bool_Sum.OR(i,j,RP_mode)}")
for i in (0,1):
    for j in (0,1):
        for k in (0,1):
            print(f"{i,j,k} 进行全加运算: {Bool_Sum.Full_Adder(i,j,k,RP_mode)}")

for i in (0,1):
    for j in (0,1):
        for k in (0,1):
            print(f"{i,j,k}交通信号灯监视结果： {Bool_Sum.TrafficLight_Status(i,j,k,RP_mode)}")


print()
print("======试试异常======")
try:
    Factorial(-15)
except MathError as E:
    print("捕获到错误！错误信息：", E)

try:
    Factorial(3.0)
except MathError as E:
    print("捕获到错误！错误信息：", E)

try:
    A(12,15)
except MathError as E:
    print("捕获到错误！错误信息：", E)

try:
    C(12,15)
except MathError as E:
    print("捕获到错误！错误信息：", E)

try:
    A(12,7,RP_mode="123456")
except MathError as E:
    print("捕获到错误！错误信息：", E)

try:
    Public_Min(13.2,5)
except MathError as E:
    print("捕获到错误！错误信息：", E)

try:
    Public_Max(12,0)
except MathError as E:
    print("捕获到错误！错误信息：", E)
try:
    L1 = DataStat()
except MathError as E:
    print("捕获到错误！错误信息：",E)



print()
print("======之前BUG回归测试======")
print("--- 1. Distance_Mean 全等列表（之前除零崩溃）---")
L_eq = DataStat(5,5,5,5)
print(f"全等列表 [5,5,5,5] Distance_Mean = {L_eq.Distance_Mean()}")

print("--- 2. DataStat 非法字符串输入（之前 ValueError 崩溃）---")
try:
    L_bad = DataStat("12..52","abc","12525")
    print(f"输入('12..52','abc','12525') 后列表 = {L_bad.get()}")
except Exception as e:
    print(f"崩溃！{e}")

print("--- 3. Count_Power 单参数（之前 UnboundLocalError）---")
print(f"Count_Power(2, 1) = {Count_Power(2, 1)}")
print(f"Count_Power(2, 0) = {Count_Power(2, 0)}")
print(f"Count_Power(3, 2) = {Count_Power(3, 2)}")

print("--- 4. Find_One 越界（之前 IndexError）---")
L_find = [1,2,3,2,5]
print(f"列表 {L_find} 找数字2第5次出现: {Find_One(L_find, 2, 5)}")
print(f"列表 {L_find} 找数字2第0次出现: {Find_One(L_find, 2, 0)}")
print(f"列表 {L_find} 找数字9第1次出现: {Find_One(L_find, 9, 1)}")

print("--- 5. Half_Adder / Full_Adder RP_mode 一致性 ---")
print(f"Half_Adder(1,0,RP_mode=False) = {Bool_Sum.Half_Adder(1,0,RP_mode=False)}")
print(f"Half_Adder(1,0,RP_mode=True)  = {Bool_Sum.Half_Adder(1,0,RP_mode=True)}")
print(f"Half_Adder(1,1,RP_mode=False) = {Bool_Sum.Half_Adder(1,1,RP_mode=False)}")
print(f"Half_Adder(1,1,RP_mode=True)  = {Bool_Sum.Half_Adder(1,1,RP_mode=True)}")
print(f"Full_Adder(1,0,0,RP_mode=False) = {Bool_Sum.Full_Adder(1,0,0,RP_mode=False)}")
print(f"Full_Adder(1,0,0,RP_mode=True)  = {Bool_Sum.Full_Adder(1,0,0,RP_mode=True)}")
print(f"Full_Adder(1,1,1,RP_mode=False) = {Bool_Sum.Full_Adder(1,1,1,RP_mode=False)}")
print(f"Full_Adder(1,1,1,RP_mode=True)  = {Bool_Sum.Full_Adder(1,1,1,RP_mode=True)}")

print("--- 6. Error_Num 多异常值 ---")
L_mul = DataStat(10, 20, 100, 200, 500)
print(f"列表 {L_mul.get()} Error_Num = {L_mul.Error_Num()}")
L_none = DataStat(1,2,3)
print(f"列表 {L_none.get()} Error_Num = {L_none.Error_Num()}")

print("--- 7. sqrt_reduce num=0 （之前 NameError）---")
print(f"sqrt_reduce(0) = {sqrt_reduce(0)}")

print("--- 8. GDN 边界 ---")
print(f"GDN(2, 1, 5) = {GDN(2, 1, 5)}")
print(f"GDN(2, 2, 3) = {GDN(2, 2, 3)}")
try:
    GDN(2, 4, 2)
except MathError as E:
    print(f"GDN(2,4,2) 捕获异常: {E}")

print()
print("__doc__查看文档\ndir()查看可使用操作")
