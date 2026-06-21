'''
本模块为自建模块，为一个数学模块
本模块包含：
    阶乘计算、斐波那契数列计算、排列数/组合数计算、极坐标/平面直角坐标互转、最大公因数/最小公倍数计算、质数检测、分解质因数计算、底数分解计算、自幂数判断、二次根式化简等基本数学功能，
    计算三角形面积的海伦公式、秦久韶公式等
    列表统计： 算术平均数、加权平均数、总体/样本方差、总体/样本标准差、异常数（三个样本标准差为界）、极差、中位数、众数等 的计算，
    布尔、逻辑运算 ：与、或、非、或非、与非、异或、同或、半加运算、全加运算、交通监视信号灯的原理等
一些算法采用最基本最经典的算法 ,如辗转相除法、递归算法等
输入及计算须符合数学原理及规范
Python内置模块math没有的你或许可以在这里找到～
提示：
    ①除了质数判断之外，在每个数学函数除标准的所需参数之外还定义了一个RP_mode参数，用于定义返回方式，
        值为 0 ，则将结果作为值返回，方便用于计算（默认）；
        值为 1 ，则将结果（带文字的，字符串）直接输出到控制台
        数据列表统计没有RP_mode参数
        布尔运算RP_mode参数设置返回的是True/False还是1/0，值为False时返回数字的，值为True时返回布尔的
    ②最大递归深度10000，悠着点玩，报错我不管

同时提供对外接口List.get()，通过这个你可以对数据列表使用内置列表的方法、函数，如：
max(List.get())  求最大值
List.get()[3]  从索引访问元素
List.get().sort()  对列表进行排序
List.get.remove(obj) 删除元素  等等操作
!!!创建数据表方法：可以直接在括号中传入数字内容，不带方括号 ； 也可以直接传入一个列表
示范1: List1 = DataStat(1,2,3)
示范2: List1 = DataStat([1,2,3])

所有内容：
    Factorial(num, RP_mode=False)               阶乘计算，限制非负整数，RP_mode=0返回数值，=1打印结果
    Fibonacci_recursive_One(n, RP_mode=False)   斐波那契数列第n项计算，RP_mode控制是否打印
    Fibonacci_recursive_All(n, RP_mode=False)   斐波那契数列前n项计算，RP_mode控制是否打印
    Arrangement(n, m, RP_mode=False)            排列数计算（n选m），要求m、n为整数且m≥n，RP_mode控制输出
    Combination(n, m, RP_mode=False)            组合数计算（n选m），要求m、n为整数且m≥n，RP_mode控制输出
    Public_Max(m, n, RP_mode=False)             最大公因数（辗转相除法），RP_mode控制是否打印结果
    Public_Min(m, n, RP_mode=False)             最小公倍数，RP_mode控制是否打印结果
    ifPrime(num)                                质数检测，返回True/False，无RP_mode
    Pol(x, y, RP_mode=False)                    平面直角坐标转极坐标，返回(r, θ°)，RP_mode控制是否打印
    Rec(r, Alpha, RP_mode=False)                极坐标转平面直角坐标，返回(x, y)，RP_mode控制是否打印
    QinJiuShao(a, b, c, RP_mode=False)          秦九韶公式求三角形面积，带边长合法性检查，RP_mode控制输出
    HaiLun(a, b, c, RP_mode=False)              海伦公式求三角形面积，带边长合法性检查，RP_mode控制输出
    Find_All(List, Value, RP_mode=False)        查找元素在列表中所有出现的位置索引，RP_mode控制输出
    Find_One(List, Value, count, RP_mode=False) 查找元素在列表中第count次出现的位置，RP_mode控制输出
    Factorization(num, RP_mode=False)           分解质因数，输入需大于1的整数，RP_mode控制输出
    Base_Decomp(num, a, RP_mode=False)          数论关系表达式分解，返回指数、商和余数，RP_mode控制输出
    Perfect_Square(num)                         判断一个数是否为完全平方数，返回 True/False，无 RP_mode
    sqrt_reduce(num, RP_mode=False)             二次根式化简，如 √18 = 3√2，返回(k,a)或打印，RP_mode控制输出
    self_power_num(num)                         判断一个数是否为自幂数（如153=1^3+5^3+3^3），返回 True/False，无 RP_mode
    Power(m, n, RP_mode=False)                  返回m的n次幂，RP_mode控制输出
    Count_Power(a, b, RP_mode=False)            返回a的b重幂，RP_mode控制输出
    GDN(a, n, b)                                高德纳箭头计算函数，不支持RP_mode=False
    DataStat(List)                     创建数据列表
        - get()                        外部接口访问
        - No_Repetitive()              列表去重
        - All_Zero()                   全零判断
        - Arithmetic_mean()            算术平均数
        - Weighted_mean()              加权平均数
        - MadCalculator()              平均绝对偏差
        - Distance_Mean()              平均距离
        - Variance(ddot=0)             总体方差,ddot=1时为样本方差
        - Std_Dev(ddot=0)              总体标准差,ddot=1时为样本标准差
        - Median()                     中位数，返回数值
        - List_Product()               累乘，列表内所有元素的乘积
        - Data_Range()                 极差（最大值减最小值）
        - Mode()                       众数
        - CV(ddot=0)                   异常系数，计算方式为Std_Dev / Arithmetic_mean
        - Error_Num()                  异常数（超过3倍总体标准差）
    Bool_Sum 类（布尔与逻辑运算类）
        - AND(A, B, RP_mode=False)      逻辑与运算，支持RP_mode返回int或bool
        - AND_More(*args, RP_mode=False) 多参数逻辑与，RP_mode控制返回类型
        - OR(A, B, RP_mode=False)       逻辑或运算，RP_mode控制返回类型
        - OR_More(*args, RP_mode=False)  多参数逻辑或，RP_mode控制返回类型
        - NOT(A, RP_mode=False)         逻辑非运算，RP_mode控制返回类型
        - NAND(A, B, RP_mode=False)     逻辑与非运算，RP_mode控制返回类型
        - NOR(A, B, RP_mode=False)      逻辑或非运算，RP_mode控制返回类型
        - XOR(A, B, RP_mode=False)      逻辑异或运算，RP_mode控制返回类型
        - XNOR(A, B, RP_mode=False)     逻辑同或运算，RP_mode控制返回类型
        - Half_Adder(A, B, RP_mode=False)  半加器运算，返回进位和当前位，RP_mode控制返回类型
        - Full_Adder(A, B, C_in, RP_mode=False) 全加器运算，返回进位和当前位，RP_mode控制返回极差
        - TrafficLight_Status(R, A, G, RP_mode=False) 交通信号灯逻辑综合运算，返回布尔或int

鸣谢：
腾讯元宝：提供函数名、变量名的英文名命名
我最爱的数学：为我提供如此多的灵感
'''


import sys
from functools import lru_cache
from math import sqrt, hypot, atan2, radians, degrees, cos, sin, floor, isqrt
from random import *
import time
import re


sys.setrecursionlimit(10000)
sys.set_int_max_str_digits(0)
Precision = 15  # 整体控制精度


class MathError(Exception):
    pass


@lru_cache(maxsize=None)  # 保留递归结果，节省计算时间
def Factorial(num: int, RP_mode=False):  # 阶乘计算
    """
    要求传入非负整数num
    返回一个数值为这个数的阶乘
    支持输出模式控制，False / 0 返回值，True / 1输出文字
    """
    if not (isinstance(num, int) and num >= 0):
        raise MathError("计算阶乘时输入的数字必须大于零且为整数")
    else:
        if (num == 0) or (num == 1):
            result = 1
        else:
            result = 1
            for i in range(2, num + 1):
                result *= i
        if not RP_mode:
            return result
        elif RP_mode:
            print(f"{num}的阶乘计算结果为：{result}")
        else:
            raise MathError("无效的输出模式")


def Fibonacci_recursive_One(n: int, RP_mode=False):  # 斐波那契-第n项
    """
    要求传入非负整数n
    返回一个数值，为斐波那契第n项值
    支持输出模式控制，False / 0 返回值，True / 1输出文字
    """
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        result = b
    if not RP_mode:
        return result
    elif RP_mode:
        print(f"斐波那契数列第{n}项为：{result}")
    else:
        raise MathError("无效的输出模式")


def Fibonacci_recursive_All(n: int, RP_mode=False):  # 斐波那契-前n项
    """
    要求传入非负整数n
    返回一个数列表，为斐波那契前n个数
    支持输出模式控制，False / 0 返回值，True / 1输出文字
    """
    List = [None] * n
    for i in range(0, n):
        List[i] = Fibonacci_recursive_One(i + 1)
    result = List
    if not RP_mode:
        return result
    elif RP_mode:
        print(f"斐波那契数列前{n}项为：{result}")
    else:
        raise MathError("无效的输出模式")


def Arrangement(n: int, m: int, RP_mode=False):  # 排列数
    """
    要求按顺序传入非负整数n、m
    要求n > m
    返回一个数值，为 从n项中选取m项排列
    支持输出模式控制，False / 0 返回值，True / 1输出文字
    """
    if not (isinstance(n, int) and isinstance(m, int) and 0 <= m <= n):
        raise MathError("计算排列数时m、n须均为正整数且m不大于n ！")
    else:
        result = Factorial(n) / Factorial(n - m)
        if not RP_mode:
            return result
        elif RP_mode:
            print(f"({m}, {n}) 的排列数计算结果为：{result}")
        else:
            raise MathError("无效的输出模式")


def Combination(n: int, m: int, RP_mode=False):  # 组合数
    """
    要求按顺序传入非负整数n、m
    要求n > m
    返回一个数值，为 从n项中选取m项组合
    支持输出模式控制，False / 0 返回值，True / 1输出文字
    """
    if not (isinstance(n, int) and isinstance(m, int) and 0 <= m <= n):
        raise MathError("计算组合数时m、n须均为非负整数且m不大于n ！")
    else:
        if n == 0 or n == m:
            result = 1
        else:
            result = Factorial(n) / (Factorial(m) * Factorial(n - m))
        if not RP_mode:
            return result
        elif RP_mode:
            print(f"({m}, {n}) 的组合数计算结果为：{result}")
        else:
            raise MathError("无效的输出模式")

def Public_Max(m: int, n: int, RP_mode=False):  # 最大公因数（辗转相除法）
    """
    要求传入非负整数n、m
    返回一个数值，为从m和n的最大公因数
    支持输出模式控制，False / 0 返回值，True / 1输出文字
    """
    if not (isinstance(m, int) and isinstance(n, int) and m > 0 and n > 0):
        raise MathError("错误！计算最大公因数时m、n须均为正整数 ！")
    r = max(m, n) % min(m, n)
    if r == 0:
        result = min(m, n)
    else:
        result = Public_Max(n, r, RP_mode=False)
    if not RP_mode:
        return result
    elif RP_mode:
        print(f"{m}, {n}的最大公因数为：{result}")
    else:
        raise MathError("无效的输出模式")


def Public_Min(m: int, n: int, RP_mode=False):  # 最小公倍数
    """
    要求传入正整数n、m
    要求n > m
    返回一个数值，为 从m和n的最小公倍数
    支持输出模式控制，False / 0 返回值，True / 1输出文字
    """
    if not (isinstance(m, int) and isinstance(n, int) and m >= 0 and n >= 0):
        raise MathError("计算最小公倍数时m、n须均为正整数 ！")
    if m == 0 or n == 0:
        raise MathError("计算最小公倍数时m、n不能为零 ！")
    result = int((m * n) / Public_Max(m, n))
    if not RP_mode:
        return result
    elif RP_mode:
        print(f"{m}, {n}的最小公倍数为： {result}")
    else:
        raise MathError("无效的输出模式")


def ifPrime(num: int):  # 质数检测
    """
    要求传入整数num
    返回布尔类型，判断这个数是不是质数
    不支持模式控制
    """
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def Pol(x, y, RP_mode=False):  # 平面直角坐标 转  极坐标
    """
    要求按顺序传入横坐标x、纵坐标y
    返回两个数值，第一个为与原点O的距离r，第二个为r与x的夹角Alpha
    支持输出模式控制，False / 0 返回值，True / 1输出文字
    """
    result = round(hypot(x, y), Precision), round(degrees(atan2(y, x)), Precision)
    if not RP_mode:
        return result
    elif RP_mode:
        print(f"平面直角坐标 {x, y} 转极坐标结果为： {result}")
    else:
        raise MathError("无效的输出模式")


def Rec(r, Alpha, RP_mode=False):  # 极坐标转平面直角坐标
    """
    要求按顺序传入与原点距离r、角度alpha
    返回两个数值，第一个数为横坐标x，第二个数为纵坐标y
    支持输出模式控制，False / 0 返回值，True / 1输出文字
    """
    AlphaR = radians(Alpha)  # 角度制转弧度制
    result = round(r * cos(AlphaR), Precision), round(r * sin(AlphaR), Precision)
    if not RP_mode:
        return result
    elif RP_mode:
        print(f"极坐标 {r, Alpha} 转换为直角坐标结果为：{result}")
    else:
        raise MathError("无效的输出模式")


def QinJiuShao(a, b, c, RP_mode=False):  # 秦久韶公式
    """
    要求传入三角形三边长
    要求符合三角形三边长定理
    返回一个数值，为这个三角形的面积
    支持输出模式控制，False / 0 返回值，True / 1输出文字
    """
    List = [a, b, c]
    List.sort()
    if not (List[0] + List[1] > List[2] or List[2] - List[1] < List[0]):
        raise MathError("不符合三角形三条边的大小关系！")
    else:
        a2 = pow(a, 2)
        b2 = pow(b, 2)
        c2 = pow(c, 2)
        result = round(sqrt((a2 * b2 - (pow((a2 + b2 - c2) / 2, 2))) / 4), Precision)
        if not RP_mode:
            return result
        elif RP_mode:
            print(f"边长为{a}, {b}, {c} 的三角形面积为：{result}\t<秦久韶公式>")
        else:
            raise MathError("无效的输出模式")


def HaiLun(a, b, c, RP_mode=False):  # 海伦公式
    """
    要求传入三角形三边长
    要求符合三角形三边长定理
    返回一个数值，为这个三角形的面积
    支持输出模式控制，False / 0 返回值，True / 1输出文字
    """
    List = [a, b, c]
    List.sort()
    if not (List[0] + List[1] > List[2] or List[2] - List[1] < List[0]):
        raise MathError("不符合三角形三条边的大小关系！")
    else:
        p = (a + b + c) / 2
        S = round(sqrt(p * (p - a) * (p - b) * (p - c)), Precision)
        if not RP_mode:
            return S
        elif RP_mode:
            print(f"边长为{a}, {b}, {c} 的三角形面积为：{S}\t<海伦公式>")
        else:
            raise MathError("无效的输出模式")


def Find_All(List: list, Value: int, RP_mode=False):
    """
    要求传入一个列表List和一个值Value
    返回一个列表，为这个值在这个列表中的所有位置
    支持输出模式控制，False / 0 返回值，True / 1输出文字
    """
    Index = []
    for i, j in enumerate(List):
        if j == Value:
            Index.append(i)
    result = Index
    if not RP_mode:
        return result
    elif RP_mode:
        print(f"元素在列表中出现的索引位置：{result}" if not len(result) == 0 else f"列表中没有这个元素")
    else:
        raise MathError("无效的输出模式")


def Find_One(List: list, Value: int, count: int, RP_mode=False):
    """
    要求传入一个列表List，两个单值value、count
    返回一个数值，为第value在列表中第count次出现的位置
    支持输出模式控制，False / 0 返回值，True / 1输出文字
    """
    Index = Find_All(List, Value)
    if len(Index) == 0 or count < 0 or count >= len(Index):
        result = None
    else:
        result = Index[count]
    if not RP_mode:
        return result
    elif RP_mode:
        print(f"元素在列表中第{count}次出现的索引位置：{result}" if not result == None else f"列表中没有这个元素")
    else:
        raise MathError("无效的输出模式")


def Factorization(num: int, RP_mode=False):  # 分解质因数
    """
    要求传入一个正整数num
    返回一个列表，为这个数分解质因数对结果
    支持输出模式控制，False / 0 返回值，True / 1输出文字
    """
    if not (isinstance(num, int) and (num > 1)):
        raise MathError("分解质因数时输入的数字必须大于1且为整数")
    else:
        result = []
        temp = num
        i = 2
        while i <= temp:
            if temp % i == 0:
                result.append(i)
                temp = temp // i
            else:
                i += 1

        if not RP_mode:
            return result
        elif RP_mode:
            print(f"{num}的质因数分解结果为：{result}")
        else:
            raise MathError("无效的输出模式")


def Base_Decomp(num, a, RP_mode=False):  # 底数分解
    """
    传入两个数num和a
    返回三个值，使a的第一个数 次幂 乘以 第二个数 加上第三个是数 可得到num
    """
    Mi = 0
    while True:
        if (a ** (Mi + 1)) > num:
            break
        else:
            Mi += 1
    r2 = a ** Mi
    Cheng = num // r2
    r4 = r2 * Cheng
    Jia = num - r4
    result = Mi, Cheng, Jia
    if not RP_mode:
        return result
    elif RP_mode:
        print(f"{a} ^ {result[0]} * {result[1]} + {result[2]} == {num}")
    else:
        raise MathError("无效的输出模式")


def Perfect_Square(num: int):  # 完全平方数判断
    """
    传入一个正整数num
    返回一个布尔值，说明这个数是不是完全平方数
    """
    return True if (pow(isqrt(num), 2) == num) else False


def sqrt_reduce(num: int, RP_mode=False):  # 二次根式分解
    """
    要求传入一个正整数num
    如果是完全平方数，返回一个数，是这个数的算术平方根
    如果不是，返回两个数值k、a，使k倍的根号a等于根号num
    支持输出模式控制，False / 0 返回值，True / 1输出文字
    """
    if not (isinstance(num, int) and num >= 0):
        raise MathError("请输入非负整数！")
    else:
        k = isqrt(num)
        if Perfect_Square(num):
            result = (k, 1)
        else:
            for i in range(k, 0, -1):
                if num % i ** 2 == 0:
                    break
            a = num // i ** 2
            result = (i, a)
        if not RP_mode:
            return result
        elif RP_mode:
            print(f"√{num} = {result[0]}√{result[1]}" if result[1] != 1 else f"√{num} = {result[0]}")
        else:
            raise MathError("无效的输出模式")

def self_power_num(num: int):  # 自幂数判断
    """
    传入一个正整数
    输出一个布尔值，判断这个数是不是自幂数
    不支持模式控制
    """
    if not (isinstance(num, int) and num >= 0):
        raise MathError("请输入非负整数！")
    else:
        List = list(map(int, list(str(num))))
        result = [d ** len(List) for d in List]
        return True if sum(result) == num else False

def Power(m, n, RP_mode=False):   #幂运算
    result = m ** n
    if not RP_mode:
        return result
    elif RP_mode:
        print(f"{m} ^ {n} = {result}")
    else:
        raise MathError("无效的输出模式")

def Count_Power(a, b, RP_mode=False):   #重幂
    if b == 1 :
        result = a
    elif b == 0 :
        if a == 0:
            raise MathError("规定，b=0时，a不得为零！")
        else:
            result = 1
    else:
        count = [a] * b
        for i in range(len(count)-2, -1, -1):
            if i == len(count)-2:
                result = Power(count[i],count[i+1])
            else:
                result = Power(count[i], result)
    if not RP_mode:
        return result
    elif RP_mode:
        print(f"{a} 的 {b}  重幂 = {result}")
    else:
        raise MathError("无效的输出模式")


def GDN(a, n, b):  #高德纳箭头
    """
    高德纳箭号运算函数
    参数说明：
    a - 底数
    n - 箭号级别（正整数）
    b - 运算次数
    规定 n==1：记作a↑b      返回 a^b
        n==2：记作a↑↑b     返回a^^b（a的b重幂）
        n==3：记作a↑↑↑b    返回a↑↑(a↑↑(…………↑↑(a↑↑a))    a的个数为b
        n>=4：庞大的天文数字，会耗尽计算机资源，不支持计算
    本函数不支持输出模式控制
    """
    def N1(a1,b1):
        return Power(a1,b1)
    def N2(a2,b2):
        return Count_Power(a2,b2)
    def N3(a3,b3):
        count = [a3] * b3
        for i in range(len(count) - 2, -1, -1):
            if i == len(count) - 2:
                result = N2(count[i], count[i + 1])
            else:
                result = N2(count[i], result)
        return result
    if b == 1:
        return a
    if n == 0:
        return a*b
    elif n == 1:
        return N1(a,b)
    elif n == 2:
        return N2(a,b)
    elif n == 3:
        return N3(a,b)
    else:
        if not (isinstance(n,int) and n >=0 ):
            raise MathError("请输入有效的级数！")
        if n > 3 :
            raise MathError("数据极其庞大，终止运算！")

class DataStat(list):
    def __init__(self, List=None, *args):
        super().__init__()
        if List == None and not args:
            raise MathError("请勿传入空列表!")
        else:
            if isinstance(List, list):
                self.List = List
            else:
                self.List = [List] + list(args)


        No_Num =[]
        i = len(self.List)-1
        while i >= 0:
            j = self.List[i]
            try:
                self.List[i] = float(j)
            except ValueError:
                del self.List[i]
                No_Num.append(j)
            i -= 1

        if len(No_Num) > 0:
            print(f"{No_Num}中的元素为非数字数据，已排除")
        if self.List == []:
            raise MathError("请传入有效列表！空列表所有统计指标均无数学意义，无法进行计算")

        self.Cateorize = self.Classify()


    def Classify(self):    # 特殊列表判断
        if self.List == []:
            return 0              # 空列表：0
        elif len(self.List) == 1:
            return 1              # 单元素列表：1
        else:
            
            for i in self.List:  # 遍历每个元素
                if i != self.get()[0]:
                    return 5  # 其他 正常列表
            return 2 if self.get()[0] == 0 else (3 if self.get()[0] == 1 else 4)   # 全0列表：2、全1列表：3，其他数字全同：4


    def get(self):
        return self.List
    
    def Arithmetic_mean(self):  # 算数平均值
        if self.Cateorize==0:
            return None
        elif self.Cateorize==1:
            return self.get()[0]
        elif self.Cateorize==2:
            return 0
        elif self.Cateorize==3:
            return 1
        elif self.Cateorize==4:
            return self.get()[0]
        else:
            result = sum(self.List) / len(self.List)
            return round(result, 4)

    def Weighted_mean(self):  # 加权平均值
        if self.Cateorize==0:
            return None
        elif self.Cateorize==1:
            return self.get()[0]
        elif self.Cateorize==2:
            return 0
        elif self.Cateorize==3:
            return 1
        elif self.Cateorize==4:
            return self.get()[0]
        else:
            r1 = []
            for i in self.List:
                r1.append(i * (i / sum(self.List)))
            result = sum(r1) / len(self.List)
        return round(result, 4)

    def MadCalculator(self):  # 平均绝对偏差
        if self.Cateorize==0:
            return None
        elif self.Cateorize==1:
            return 0
        elif self.Cateorize==2:
            return 0
        elif self.Cateorize==3:
            return 0
        elif self.Cateorize==4:
            return 0
        else:
            abs_deviations = []
            for i in self.List:
                abs_deviations.append(abs(i - self.Arithmetic_mean()))
            return round(sum(abs_deviations) / len(abs_deviations), Precision)

    def Distance_Mean(self):  # 平均差
        self.List = sorted(self.List)
        result = []
        for i in range(1, len(self.List)):
            result.append(abs(self.List[i] - self.List[i - 1]))
        try:
            return round(sum(result) / len(result) , Precision)
        except ZeroDivisionError:
            return 0

    def __Var(self):
        r1 = []
        for i in self.List:
            r1.append(pow(i - self.Arithmetic_mean(), 2))
        return sum(r1)

    def Variance(self,ddot=0):  # 方差，ddot=0时为总体，ddot=1时为样本
        if self.Cateorize==5:
            result = self.__Var() / len(self.List) if ddot == 0 else self.__Var() / (len(self.List) - 1)
            return round(result, 4)
        else:
            return 0

    def Std_Dev(self,ddot=0):  # 标准差，ddot=0时为总体，ddot=1时为样本
        if self.Cateorize==5:
            return round(sqrt(self.Variance(ddot)), 4) if self.Variance(ddot) is not None else None
        else:
            return 0

    def Median(self):  # 中位数
        if self.Cateorize==5:
            r1 = len(self.List)
            self.List.sort()
            if r1 % 2 == 0:
                return (self.List[int(r1 / 2)] + self.List[int(r1 / 2 - 1)]) / 2
            else:
                return self.List[int(r1 // 2)]
        elif self.Cateorize==0:
            return None
        elif self.Cateorize==1:
            return self.get()[0]
        elif self.Cateorize==2:
            return 0
        elif self.Cateorize==3:
            return 1
        else:
            return self.get()[0]

    def List_Product(self):  # 累乘
        if self.Cateorize==5:
            result = 1
            for num in self.List:
                result *= num
            return result
        elif self.Cateorize==0:
            return 1
        elif self.Cateorize==1:
            return self.get()[0]
        elif self.Cateorize==2:
            return 0
        elif self.Cateorize==3:
            return 1
        else:
            return self.get()[0]**len(self.List)

    def Data_Range(self):  # 极差
        if self.Cateorize==0:
            return None
        elif self.Cateorize==5:
            return max(self.List) - min(self.List)
        else:
            return 0

    def Mode(self):  # 众数
        if self.Cateorize==5:
            Dicts = dict()
            for i in self.List:
                Dicts[i] = self.List.count(i)
            LK = list(Dicts.keys())
            LV = list(Dicts.values())
            result_List = []
            Index = Find_All(LV, max(LV))
            if len(Index) == len(set(self.List)):
                return None
            else:
                for j in Index:
                    result_List.append(LK[j])
                if len(result_List) == 1:
                    return result_List[0]
                else:
                    return result_List
        elif self.Cateorize==4:
            return self.get()[0]
        elif self.Cateorize==3:
            return 1
        elif self.Cateorize==2:
            return 0
        elif self.Cateorize==1:
            return self.get()[0]
        else:
            return None

    def Error_Num(self):  # 异常数，判断标准为偏离均值大于三个样本标准差
        if self.Cateorize==5:
            result_List = []
            mean = self.Arithmetic_mean()
            for i in self.List:
                if abs(i - mean) >= 3 * self.Std_Dev(ddot=1):
                    result_List.append(i)
            if len(result_List) == 1:
                return result_List[0]
            elif len(result_List) == 0:
                print(f"列表 {self.List} 无异常值")
                return None
            else:
                return result_List
        else:
            return None

    def No_Repetitive(self):  # 列表去重
        seen = set()
        result_list = []

        for item in self.List:
            if item not in seen:
                seen.add(item)
                result_list.append(item)

        self.List = result_list

    def CV(self,ddot=0):  # 变异系数
        if self.Cateorize==5:
            return self.Std_Dev(ddot) / self.Arithmetic_mean()
        elif self.Cateorize in (0,2):
            return None
        else:
            return 0

class Bool_Sum:
    @staticmethod
    def AND(A, B, RP_mode=False):  # 与运算
        A = bool(A)
        B = bool(B)
        result = A if A == False else B
        return result if RP_mode else int(result)

    @staticmethod
    def AND_More(*args, RP_mode=False):
        result = all(tuple(map(bool, args)))
        return result if RP_mode else int(result)

    @staticmethod
    def OR(A, B, RP_mode=False):  # 或运算
        A = bool(A)
        B = bool(B)
        result = A if A == True else B
        return result if RP_mode else int(result)

    @staticmethod
    def OR_More(*args, RP_mode=False):
        result = any(tuple(map(bool, args)))
        return result if RP_mode else int(result)

    @staticmethod
    def NOT(A, RP_mode=False):  # 非运算
        A = bool(A)
        result = not A
        return result if RP_mode else int(result)

    @staticmethod
    def NAND(A, B, RP_mode=False):  # 与非运算
        A = bool(A)
        B = bool(B)
        result = not (A and B)
        return result if RP_mode else int(result)

    @staticmethod
    def NOR(A, B, RP_mode=False):  # 或非运算
        A = bool(A)
        B = bool(B)
        result = not (A or B)
        return result if RP_mode else int(result)

    @staticmethod
    def XOR(A, B, RP_mode=False):  # 异或运算
        A = bool(A)
        B = bool(B)
        result = (A and (not (B))) or (B and (not (A)))
        return result if RP_mode else int(result)

    @staticmethod
    def XNOR(A, B, RP_mode=False):  # 同或运算
        A = bool(A)
        B = bool(B)
        result = (A and B) or ((not A) and (not B))
        return result if RP_mode else int(result)

    @staticmethod
    def Half_Adder(A, B, RP_mode=False):  # 半加运算
        A = bool(A)
        B = bool(B)
        S = Bool_Sum.XOR(A, B,RP_mode=True)
        C = A and B
        return (C, S) if RP_mode else tuple(map(int, (C, S)))

    @staticmethod
    def Full_Adder(A, B, C_in, RP_mode=False):  # 全加运算
        A = bool(A)
        B = bool(B)
        C_in = bool(C_in)
        S = Bool_Sum.XOR(Bool_Sum.XOR(A, B,RP_mode=True), C_in, RP_mode=True)
        C_out = (A and B) or (B and C_in) or (A and C_in)
        return (C_out, S) if RP_mode else tuple(map(int, (C_out, S)))

    @staticmethod
    def TrafficLight_Status(R, A, G, RP_mode=False):
        R = bool(R)
        A = bool(A)
        G = bool(G)
        Z = Bool_Sum.OR_More(Bool_Sum.AND_More(Bool_Sum.NOT(R), Bool_Sum.NOT(A), Bool_Sum.NOT(G)),
                             Bool_Sum.AND_More(Bool_Sum.NOT(R), A, G),
                             Bool_Sum.AND_More(R, Bool_Sum.NOT(A), G),
                             Bool_Sum.AND_More(R, A, Bool_Sum.NOT(G)),
                             Bool_Sum.AND_More(R, A, G))
        return Z if RP_mode else int(Z)

A = Arrangement
C = Combination
Fib_One = Fibonacci_recursive_One
Fib_All = Fibonacci_recursive_All
if __name__ == "__main__":
    L1 = DataStat(7, 9, 5, 9, 6, 5, 23, 15,"12..52")
    print(L1.Variance(ddot=0))
    print(L1.Variance(ddot=1))
    print(L1.Std_Dev(ddot=0))
    print(L1.Std_Dev(ddot=1))
    print(L1.CV(ddot=0))
    print(L1.CV(ddot=1))
    print(type(L1))
    print(Bool_Sum.AND_More(1, 1, 1, 1))
    sqrt_reduce(18, 1)
    A(15, 6)
    Count_Power(2,5,RP_mode=True)
    print(L1.get())
    print(L1.get())
    L2=DataStat("12..2","abc","12525")
    print(L2.get())
    L3 =DataStat(1,2,3,2)
    L3.No_Repetitive()
    print(L3.get())    
if __name__ != "__main__":
    # 当作为模块导入时，导出所有公共函数
    __all__ = [
        'Factorial', 'Fibonacci_recursive_One', 'Fibonacci_recursive_All',
        'Arrangement', 'Combination', 'Public_Max', 'Public_Min',
        'ifPrime', 'Pol', 'Rec', 'QinJiuShao', 'HaiLun',
        'Find_All', 'Find_One', 'Factorization', 'Base_Decomp',
        'Perfect_Square', 'sqrt_reduce', 'self_power_num',
        'DataStat', 'Bool_Sum', 'MathError', 'Precision', 'A', 'C',
        'Count_Power','GDN','Power'
    ]
