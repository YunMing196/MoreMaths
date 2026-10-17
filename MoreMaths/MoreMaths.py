'''
本模块为自建模块，为一个数学模块（文档完善版）
本模块包含：
    阶乘计算、斐波那契数列计算、排列数/组合数计算、极坐标/平面直角坐标互转、最大公因数/最小公倍数计算、质数检测、分解质因数计算、底数分解计算、自幂数判断、二次根式化简等基本数学功能，
    计算三角形面积的海伦公式、秦久韶公式等
    列表统计： 算术平均数、加权平均数、总体/样本方差、总体/样本标准差、异常数（三个样本标准差为界）、极差、中位数、众数等 的计算，
    布尔、逻辑运算 ：与、或、非、或非、与非、异或、同或、半加运算、全加运算、交通监视信号灯的原理等
一些算法采用最基本最经典的算法 ,如辗转相除法、递归算法等
输入及计算须符合数学原理及规范
Python内置模块math没有的你或许可以在这里找到～

【本文档版说明】
- 本文件为 MoreMaths 的「文档完善版」：函数体代码与源文件完全一致，只补全了说明文档。
- 每个函数/方法的第一行 docstring 均为「中文名/作用」，PyCharm 鼠标悬浮即可看到提示。
- 不改任何 bug，逻辑与源文件 100% 相同。

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

    别名（快捷写法）：
        A = Arrangement                           排列数（别名）
        C = Combination                           组合数（别名）
        Fib_One = Fibonacci_recursive_One         斐波那契第n项（别名）
        Fib_All = Fibonacci_recursive_All         斐波那契前n项（别名）

    常量 / 异常：
        Precision = 15             全局精度控制（round 保留的小数位数）
        MathError                  自定义异常类（所有非法输入 / 无效 RP_mode 时抛出）

    DataStat(List)                     创建数据列表
        - get()                        外部接口访问
        - Classify()                   内部：列表特殊分类（空/单元素/全0/全1/全同/普通）
        - All_Zero()                   全零判断（文档遗留：当前代码未实现）
        - No_Repetitive()              列表去重
        - Arithmetic_mean()            算术平均数
        - Weighted_mean()              加权平均数（权 = 数值在总和中的占比）
        - MadCalculator()              平均绝对偏差
        - Distance_Mean()              平均差
        - Variance(ddot=0)             总体方差,ddot=1时为样本方差
        - Std_Dev(ddot=0)              总体标准差,ddot=1时为样本标准差
        - Median()                     中位数，返回数值
        - List_Product()               累乘，列表内所有元素的乘积
        - Data_Range()                 极差（最大值减最小值）
        - Mode()                       众数
        - CV(ddot=0)                   变异系数，计算方式为Std_Dev / Arithmetic_mean
        - Error_Num()                  异常数（超过3倍样本标准差）
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
CherryStudio：添加文档注释
我最爱的数学：为我提供如此多的灵感
'''


import sys
from functools import lru_cache
from contextlib import contextmanager
from importlib.metadata import *
from math import sqrt, hypot, atan2, radians, degrees, cos, sin, floor, isqrt
from random import *
import time
import re
from unittest import result

sys.setrecursionlimit(10000)
if sys.version_info>=(3,10,0):
    exec ("sys.set_int_max_str_digits(0)")
Precision = 15  # 整体控制精度


class MathError(Exception):
    """自定义异常类
    作用：模块内所有非法输入 / 无效 RP_mode 时抛出的异常类型
    参数：无
    原理/输出：作为异常类使用，用 raise MathError("提示信息") 触发
    """
    pass

title_order = 1
@contextmanager
def Time(title=None, RP_mode=1):
    global title_order
    if title is None:
        current_title = f"测试代码_{title_order}"
        title_order += 1
    else:
        current_title = title
    start = time.perf_counter()
    if RP_mode:
        print(f"{current_title}开始计时")
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        if RP_mode:
            print(f"{current_title}计时结束！，运行用时{elapsed:.6f}s")

@lru_cache(maxsize=None)  # 保留递归结果，节省计算时间
def Factorial(num: int, RP_mode=False):  # 阶乘计算
    """
    阶乘计算
    作用：计算非负整数 num 的阶乘（num!）
    参数：
        num : int - 非负整数（必须 >= 0）
        RP_mode : bool - 返回模式，False/0 返回数值，True/1 打印结果
    原理/输出：返回 num 的阶乘值；如 Factorial(5) -> 120；RP_mode=True 时打印"5的阶乘计算结果为：120"
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

def Catalan(n: int, RP_mode=False):  # 卡特兰数
    LIST = [1,1,2,5,14,42,132,429]
    if not(n>=0 and isinstance(n,int)):
        raise MathError("请输入正确的数！")
    elif 0 <= n <= 7:
        result = LIST[n]
    else:
        result = Combination(2 * n, n) / (n + 1)
    if not RP_mode :
        return result
    elif RP_mode:
        print(f"卡特兰数列第{n}项为：{result}")
    else:
        raise MathError("无效的输出模式")

def Fibonacci_recursive_One(n: int, RP_mode=False):  # 斐波那契-第n项
    """
    斐波那契数列第 n 项
    作用：计算斐波那契数列的第 n 项（1,1,2,3,5,8,...）
    参数：
        n : int - 非负整数，表示第几项
        RP_mode : bool - 返回模式，False/0 返回数值，True/1 打印结果
    原理/输出：返回斐波那契第 n 项值；如 Fibonacci_recursive_One(12) -> 144
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
    斐波那契数列前 n 项
    作用：计算斐波那契数列的前 n 项
    参数：
        n : int - 非负整数，表示要生成的项数
        RP_mode : bool - 返回模式，False/0 返回列表，True/1 打印列表
    原理/输出：返回前 n 项的列表；如 Fibonacci_recursive_All(5) -> [1, 1, 2, 3, 5]
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
    排列数（n 选 m 的排列）
    作用：计算从 n 个不同元素中取出 m 个的排列数 P(n,m) = n!/(n-m)!
    参数：
        n : int - 总数（非负整数）
        m : int - 取出的个数（非负整数，且 m <= n）
        RP_mode : bool - 返回模式，False/0 返回数值，True/1 打印结果
    原理/输出：返回排列数；如 Arrangement(5,2) = 5!/(5-2)! = 20
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
    组合数（n 选 m 的组合）
    作用：计算从 n 个不同元素中取出 m 个的组合数 C(n,m) = n!/(m!·(n-m)!)
    参数：
        n : int - 总数（非负整数）
        m : int - 取出的个数（非负整数，且 m <= n）
        RP_mode : bool - 返回模式，False/0 返回数值，True/1 打印结果
    原理/输出：返回组合数；如 Combination(5,2) = 5!/(2!·3!) = 10
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
    最大公因数（辗转相除法）
    作用：计算两个正整数的最大公因数 GCD
    参数：
        m : int - 正整数
        n : int - 正整数
        RP_mode : bool - 返回模式，False/0 返回数值，True/1 打印结果
    原理/输出：采用辗转相除法（欧几里得算法）返回最大公因数；如 Public_Max(12,8) -> 4
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
    最小公倍数
    作用：计算两个正整数的最小公倍数 LCM
    参数：
        m : int - 正整数
        n : int - 正整数
        RP_mode : bool - 返回模式，False/0 返回数值，True/1 打印结果
    原理/输出：利用公式 LCM = m·n / GCD(m,n)；如 Public_Min(12,8) -> 24
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
    质数检测
    作用：判断一个整数是否为质数（素数）
    参数：
        num : int - 待判断的整数
    原理/输出：返回布尔值 True/False；不支持 RP_mode；如 ifPrime(17) -> True，ifPrime(15) -> False
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
    平面直角坐标转极坐标
    作用：把平面直角坐标 (x, y) 转换为极坐标 (r, θ)
    参数：
        x : 数值 - 横坐标
        y : 数值 - 纵坐标
        RP_mode : bool - 返回模式，False/0 返回元组，True/1 打印结果
    原理/输出：返回 (r, θ°)，r = √(x²+y²)，θ = atan2(y,x) 换算成角度；如 Pol(3,4) 的 r = 5
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
    极坐标转平面直角坐标
    作用：把极坐标 (r, α) 转换为平面直角坐标 (x, y)
    参数：
        r : 数值 - 到原点的距离
        Alpha : 数值 - 角度（角度制，内部会转弧度）
        RP_mode : bool - 返回模式，False/0 返回元组，True/1 打印结果
    原理/输出：返回 (x, y)，x = r·cos(α)，y = r·sin(α)
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
    秦九韶公式求三角形面积
    作用：用秦九韶（三斜求积）公式计算三角形的面积
    参数：
        a, b, c : 数值 - 三角形三条边长（须满足两边之和大于第三边）
        RP_mode : bool - 返回模式，False/0 返回数值，True/1 打印结果
    原理/输出：返回三角形面积；如 QinJiuShao(3,4,5) -> 6
    """
    List = [a, b, c]
    List.sort()
    if not (List[0] + List[1] > List[2] and List[2] - List[1] < List[0]):
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
    海伦公式求三角形面积
    作用：用海伦公式计算三角形的面积
    参数：
        a, b, c : 数值 - 三角形三条边长（须满足两边之和大于第三边）
        RP_mode : bool - 返回模式，False/0 返回数值，True/1 打印结果
    原理/输出：海伦公式 S = √(p(p-a)(p-b)(p-c))，其中 p = (a+b+c)/2；如 HaiLun(3,4,5) -> 6
    """
    List = [a, b, c]
    List.sort()
    if not (List[0] + List[1] > List[2] and List[2] - List[1] < List[0]):
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


def Find_All(List: list, Value: int, RP_mode=False):   # 寻找-所有
    """
    查找元素在列表中的所有位置
    作用：找出指定值在列表中出现的所有下标
    参数：
        List : list - 待查找的列表
        Value : 任意 - 要查找的值
        RP_mode : bool - 返回模式，False/0 返回列表，True/1 打印结果
    原理/输出：返回所有出现位置的索引列表；如 Find_All([1,2,1], 1) -> [0, 2]
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
    查找元素第 count 次出现的位置
    作用：找出指定值在列表中第 count 次出现的下标
    参数：
        List : list - 待查找的列表
        Value : 任意 - 要查找的值
        count : int - 第几次出现（从 1 开始计数）
        RP_mode : bool - 返回模式，False/0 返回数值，True/1 打印结果
    原理/输出：返回第 count 次出现的索引；不存在时返回 None
    """
    Index = Find_All(List, Value)
    if not(len(Index) > 0 and 0 < count <=len(Index)):
        result = None
    else:
        result = Index[count-1]
    if not RP_mode:
        return result
    elif RP_mode:
        print(f"元素在列表中第{count}次出现的索引位置：{result}" if not result == None else f"列表中没有这个元素")
    else:
        raise MathError("无效的输出模式")


def Factorization(num: int, RP_mode=False):  # 分解质因数
    """
    分解质因数
    作用：把一个大于 1 的整数分解为质因数的乘积
    参数：
        num : int - 待分解的正整数（必须 > 1）
        RP_mode : bool - 返回模式，False/0 返回列表，True/1 打印结果
    原理/输出：返回质因数列表；如 Factorization(15) -> [3, 5]
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
    底数分解
    作用：把一个数 num 表示成 a 的幂的形式：a^Mi × Cheng + Jia == num
    参数：
        num : 数值 - 被分解的数
        a : 数值 - 底数（注意：a = 0 或 1 时本函数会死循环，使用前请自行保证 a >= 2）
        RP_mode : bool - 返回模式，False/0 返回元组，True/1 打印结果
    原理/输出：返回 (Mi, Cheng, Jia)，满足 a^Mi × Cheng + Jia == num
    """
    if not (type(num) in [int, float,complex] and type(a) in [int, float,complex]):
        raise MathError("只允许输入数字类型!")
    Mi = 0
    if a <= 1:
        raise MathError("请输入>=1的底数！")
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
    完全平方数判断
    作用：判断一个数是否为完全平方数
    参数：
        num : int - 待判断的正整数
    原理/输出：返回布尔值；如 Perfect_Square(16) -> True，Perfect_Square(17) -> False
    """
    return True if (pow(isqrt(num), 2) == num) else False


def sqrt_reduce(num: int, RP_mode:int=False):  # 二次根式分解
    """
    二次根式化简
    作用：把 √num 化简为 k√a 的形式（k 为根号外的整数系数）
    参数：
        num : int - 非负整数，根号下的数
        RP_mode : bool - 返回模式，False/0 返回元组，True/1 打印结果
    原理/输出：若 num 是完全平方数返回 (√num, 1)；否则返回 (k, a) 使 k²×a == num；如 sqrt_reduce(18) -> (3, 2) 表示 √18 = 3√2
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
    自幂数判断（阿姆斯特朗数）
    作用：判断一个数是否为自幂数（各数位数字的位数次方之和等于该数本身）
    参数：
        num : int - 非负整数
    原理/输出：返回布尔值；如 self_power_num(153) -> True（1³+5³+3³=153）
    """
    if not (isinstance(num, int) and num >= 0):
        raise MathError("请输入非负整数！")
    else:
        List = list(map(int, list(str(num))))
        result = [d ** len(List) for d in List]
        return True if sum(result) == num else False

def Power(m, n, RP_mode=False):   #幂运算
    """
    幂运算
    作用：计算 m 的 n 次幂
    参数：
        m : 数值 - 底数
        n : 数值 - 指数
        RP_mode : bool - 返回模式，False/0 返回数值，True/1 打印结果
    原理/输出：返回 m^n；如 Power(2, 10) -> 1024
    """
    result = m ** n
    if not RP_mode:
        return result
    elif RP_mode:
        print(f"{m} ^ {n} = {result}")
    else:
        raise MathError("无效的输出模式")

def Count_Power(a, b, RP_mode=False):   #重幂
    """
    重幂（迭代幂 / 幂塔）
    作用：计算 a 的 b 重幂（a 连续自幂 b 次，即 a↑↑b = a^(a^(...^a))）
    参数：
        a : 数值 - 底数
        b : 整数 - 重数（b = 0 时 a 不能为 0）
        RP_mode : bool - 返回模式，False/0 返回数值，True/1 打印结果
    原理/输出：返回重幂结果；如 Count_Power(2,3) = 2^(2^2) = 16
    """
    if b == 1 :
        result = a
    elif b < 0:
        raise MathError("b<0时无意义")
    elif b == 0 :
        if a == 0:
            raise MathError("规定，b==0时，a不得为零！")
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
    高德纳箭头运算
    作用：实现高德纳向上箭头记号的运算（大数运算）
    参数：
        a : 数值 - 底数
        n : 整数 - 箭号级别：n=0 乘法，n=1 幂，n=2 重幂，n=3 更高层
        b : 整数 - 运算次数
    原理/输出：n=0 返回 a×b；n=1 返回 a^b；n=2 返回 a 的 b 重幂；n=3 返回 a↑↑↑b；n>3 抛出异常（数值极大）
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
    """
    数据统计类（继承 list）
    作用：创建一个数据列表对象，自动清洗非数字数据，并提供各种统计方法
    参数：
        List : 可省略 - 可以是列表，也可以是单个数字（配合 *args 展开成列表）
        *args : 可变参数 - 当 List 是单个数字时，其余数字填在这里
    原理/输出：创建对象后可通过 .get() 获取清洗后的列表；非法字符串会被自动剔除
    示范：DataStat(1,2,3) 或 DataStat([1,2,3])
    """
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
            except (ValueError,TypeError):
                del self.List[i]
                No_Num.append(j)
            i -= 1

        if len(No_Num) > 0:
            print(f"{No_Num}中的元素为非数字数据，已排除")
        if self.List == []:
            raise MathError("请传入有效列表！空列表所有统计指标均无数学意义，无法进行计算")

        self.Cateorize = self.Classify()  # 调用方法给列表分类
        self.p_list = self.Prob()


    def Classify(self):    # 特殊列表判断
        """
        列表特殊分类（内部方法）
        作用：判断列表属于哪种特殊情况，供其他统计方法快速短路
        参数：
            无
        原理/输出：返回分类编号：0=空列表，1=单元素，2=全0，3=全1，4=其他全同值，5=普通列表
        """
        if self.List == []:
            return 0              # 空列表：0
        elif len(self.List) == 1:
            return 1              # 单元素列表：1
        else:

            for i in self.List:  # 遍历每个元素
                if i != self.get()[0]:
                    return 5  # 其他 正常列表
            return 2 if self.get()[0] == 0 else (3 if self.get()[0] == 1 else 4)
            # 全0列表：2、全1列表：3，其他数字全同：4


    def get(self):
        """
        获取数据列表（对外接口）
        作用：返回内部存储的列表，可直接对其使用列表的内置方法
        参数：
            无
        原理/输出：返回 self.List；例如 max(List.get())、List.get().sort()
        """
        return self.List

    def Arithmetic_mean(self):  # 算数平均值
        """
        算术平均数
        作用：计算列表数据的算术平均值
        参数：
            无
        原理/输出：返回平均值（保留 4 位小数）；特殊情况按分类短路（空列表 None、单元素/全同返回该值、全0返回0、全1返回1）
        """
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

    def Prob(self):
        result = []
        L = self.get()
        Sum = sum(L)
        for i in range(0,len(L)):
            result.append(L[i]/Sum)
        return result


    def Weighted_mean(self,Wighted:list=None):  # 加权平均值
        """
        加权平均数
        作用：计算加权平均值，权重 = 各数值在整组数据总和中的占比
        参数：
            Wighted 权重列表，即每个数对应的权重
        原理/输出：对每个数 x 取占比 &=x/总和，计算 x×& 后对所有结果求算术平均：Σ(x·x/Σx)/n
        """
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
            Sum = Wighted if Wighted else sum(self.p_list)
            L = []
            for i,j in zip(self.get(),self.p_list):
                L.append(i*j)
            result = sum(L) / Sum
        return round(result, 4)

    def MadCalculator(self):  # 平均绝对偏差
        """
        平均绝对偏差（MAD）
        作用：计算各数据点与均值之差的绝对值的平均
        参数：
            无
        原理/输出：MAD = Σ|x - 均值| / n；返回计算结果
        """
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
        """
        平均差
        作用：计算排序后相邻两个数据之差的绝对值的平均
        参数：
            无
        原理/输出：先对列表排序，再对相邻差取绝对值的平均（注意：本方法会改变内部列表的顺序）
        """
        self.List = sorted(self.List)
        result = []
        for i in range(1, len(self.List)):
            result.append(abs(self.List[i] - self.List[i - 1]))
        try:
            return round(sum(result) / len(result) , Precision)
        except ZeroDivisionError:
            return 0

    def __Var(self):
        """
        偏差平方和（内部方法）
        作用：计算各数据点与均值之差的平方和，供方差/标准差使用
        参数：
            无
        原理/输出：返回 Σ(x - 均值)²
        """
        r1 = []
        for i in self.List:
            r1.append(pow(i - self.Arithmetic_mean(), 2))
        return sum(r1)

    def Variance(self,ddot=0):  # 方差，ddot=0时为总体，ddot=1时为样本
        """
        总体方差 / 样本方差（ddot 控制总体或样本）
        作用：计算数据列表的方差
        参数：
            ddot : int - 0=总体方差（除以 n，代表全体数据）；1=样本方差（除以 n-1，代表抽样数据）
        原理/输出：返回方差（保留 4 位小数）
        记忆口诀：ddot=0 总体=全体(/n)；ddot=1 样本=抽样(/(n-1))
        """
        if self.Cateorize==5:
            result = self.__Var() / len(self.List) if ddot == 0 else self.__Var() / (len(self.List) - 1)
            return round(result, 4)
        else:
            return 0

    def Std_Dev(self,ddot=0):  # 标准差，ddot=0时为总体，ddot=1时为样本
        """
        总体标准差 / 样本标准差（ddot 控制总体或样本）
        作用：计算数据列表的标准差（方差的平方根）
        参数：
            ddot : int - 0=总体标准差（除以 n）；1=样本标准差（除以 n-1）
        原理/输出：返回标准差（保留 4 位小数）
        记忆口诀：ddot=0 总体=全体(/n)；ddot=1 样本=抽样(/(n-1))
        """
        if self.Cateorize==5:
            return round(sqrt(self.Variance(ddot)), 4) if self.Variance(ddot) is not None else None
        else:
            return 0

    def Median(self):  # 中位数
        """
        中位数
        作用：计算列表数据的中位数
        参数：
            无
        原理/输出：返回中位数；元素个数为偶数时取中间两个的平均值，奇数时取中间那个
        """
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
        """
        累乘
        作用：计算列表内所有元素的乘积
        参数：
            无
        原理/输出：返回乘积；空列表返回 1，全0返回 0，全同值返回 该值^元素个数
        """
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
        """
        极差
        作用：计算最大值与最小值的差
        参数：
            无
        原理/输出：返回 最大值 - 最小值
        """
        if self.Cateorize==0:
            return None
        elif self.Cateorize==5:
            return max(self.List) - min(self.List)
        else:
            return 0

    def Mode(self):  # 众数
        """
        众数
        作用：找出出现次数最多的数值（众数）
        参数：
            无
        原理/输出：唯一最多返回该值；多峰（部分并列）返回并列值列表；全峰（所有值并列）返回 None
        """
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
        """
        异常数（3σ 法则）
        作用：找出偏离均值超过 3 倍样本标准差的数据点
        参数：
            无
        原理/输出：返回异常值（单个值或列表）；无异常时打印提示并返回 None
        """
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
        """
        列表去重
        作用：去掉列表中重复的元素，保持原有顺序
        参数：
            无
        原理/输出：直接修改内部列表 self.List（无返回值）
        """
        seen = set()
        result_list = []

        for item in self.List:
            if item not in seen:
                seen.add(item)
                result_list.append(item)

        self.List = result_list

    def CV(self,ddot=0):  # 变异系数
        """
        变异系数（CV）
        作用：计算标准差与均值之比，衡量数据的相对离散程度
        参数：
            ddot : int - 0=基于总体标准差；1=基于样本标准差
        原理/输出：返回 标准差 / 均值；注意：均值=0 时返回0
        """
        if self.Cateorize==5:
            return self.Std_Dev(ddot) / self.Arithmetic_mean() if self.Arithmetic_mean() else 0
        elif self.Cateorize in (0,2):
            return None
        else:
            return 0

class Bool_Sum:
    """
    布尔与逻辑运算类
    作用：提供各种布尔逻辑运算、半加器/全加器、交通信号灯逻辑综合
    统一说明：RP_mode 为 False 时返回 0/1，为 True 时返回 False/True
    """
    @staticmethod
    def AND(A, B, RP_mode=False):  # 与运算
        """
        逻辑与运算（AND）
        作用：对两个输入做逻辑与
        参数：
            A, B : 任意 - 输入值（自动转 bool）
            RP_mode : bool - False 返回 0/1，True 返回 False/True
        原理/输出：A 和 B 都为真才为真
        """
        A = bool(A)
        B = bool(B)
        result = A if A == False else B
        return result if RP_mode else int(result)

    @staticmethod
    def AND_More(*args, RP_mode=False):
        """
        多参数逻辑与（AND_More）
        作用：对任意多个输入做逻辑与
        参数：
            *args : 任意 - 多个输入值
            RP_mode : bool - False 返回 0/1，True 返回 False/True
        原理/输出：全部为真才为真
        """
        result = all(tuple(map(bool, args)))
        return result if RP_mode else int(result)

    @staticmethod
    def OR(A, B, RP_mode=False):  # 或运算
        """
        逻辑或运算（OR）
        作用：对两个输入做逻辑或
        参数：
            A, B : 任意 - 输入值（自动转 bool）
            RP_mode : bool - False 返回 0/1，True 返回 False/True
        原理/输出：有一个为真即为真
        """
        A = bool(A)
        B = bool(B)
        result = A if A == True else B
        return result if RP_mode else int(result)

    @staticmethod
    def OR_More(*args, RP_mode=False):
        """
        多参数逻辑或（OR_More）
        作用：对任意多个输入做逻辑或
        参数：
            *args : 任意 - 多个输入值
            RP_mode : bool - False 返回 0/1，True 返回 False/True
        原理/输出：有一个为真即为真
        """
        result = any(tuple(map(bool, args)))
        return result if RP_mode else int(result)

    @staticmethod
    def NOT(A, RP_mode=False):  # 非运算
        """
        逻辑非运算（NOT）
        作用：对输入取反
        参数：
            A : 任意 - 输入值
            RP_mode : bool - False 返回 0/1，True 返回 False/True
        原理/输出：真变假，假变真
        """
        A = bool(A)
        result = not A
        return result if RP_mode else int(result)

    @staticmethod
    def NAND(A, B, RP_mode=False):  # 与非运算
        """
        逻辑与非（NAND）
        作用：先做逻辑与，再取反
        参数：
            A, B : 任意 - 输入值
            RP_mode : bool - False 返回 0/1，True 返回 False/True
        原理/输出：A、B 都为真时返回假，否则返回真
        """
        A = bool(A)
        B = bool(B)
        result = not (A and B)
        return result if RP_mode else int(result)

    @staticmethod
    def NOR(A, B, RP_mode=False):  # 或非运算
        """
        逻辑或非（NOR）
        作用：先做逻辑或，再取反
        参数：
            A, B : 任意 - 输入值
            RP_mode : bool - False 返回 0/1，True 返回 False/True
        原理/输出：A、B 都为假时返回真，否则返回假
        """
        A = bool(A)
        B = bool(B)
        result = not (A or B)
        return result if RP_mode else int(result)

    @staticmethod
    def XOR(A, B, RP_mode=False):  # 异或运算
        """
        逻辑异或（XOR）
        作用：两个输入相异才为真
        参数：
            A, B : 任意 - 输入值
            RP_mode : bool - False 返回 0/1，True 返回 False/True
        原理/输出：A ≠ B 时为真
        """
        A = bool(A)
        B = bool(B)
        result = (A and (not (B))) or (B and (not (A)))
        return result if RP_mode else int(result)

    @staticmethod
    def XNOR(A, B, RP_mode=False):  # 同或运算
        """
        逻辑同或（XNOR）
        作用：两个输入相同才为真
        参数：
            A, B : 任意 - 输入值
            RP_mode : bool - False 返回 0/1，True 返回 False/True
        原理/输出：A == B 时为真
        """
        A = bool(A)
        B = bool(B)
        result = (A and B) or ((not A) and (not B))
        return result if RP_mode else int(result)

    @staticmethod
    def Half_Adder(A, B, RP_mode=False):  # 半加运算
        """
        半加器运算（Half Adder）
        作用：两个二进制位相加，输出本位和与进位
        参数：
            A, B : 任意 - 两个加数位
            RP_mode : bool - False 返回 (0/1, 0/1)，True 返回 (False/True, False/True)
        原理/输出：返回 (进位 C, 本位和 S)；S = A XOR B，C = A AND B
        """
        A = bool(A)
        B = bool(B)
        S = Bool_Sum.XOR(A, B,RP_mode=True)
        C = A and B
        return (C, S) if RP_mode else tuple(map(int, (C, S)))

    @staticmethod
    def Full_Adder(A, B, C_in, RP_mode=False):  # 全加运算
        """
        全加器运算（Full Adder）
        作用：两个二进制位加一个低位进位，输出本位和与进位
        参数：
            A, B : 任意 - 两个加数位
            C_in : 任意 - 低位进位输入
            RP_mode : bool - False 返回 (0/1, 0/1)，True 返回 (False/True, False/True)
        原理/输出：返回 (进位 C_out, 本位和 S)；S = A XOR B XOR C_in，C_out = (A·B)+(B·C_in)+(A·C_in)
        """
        A = bool(A)
        B = bool(B)
        C_in = bool(C_in)
        S = Bool_Sum.XOR(Bool_Sum.XOR(A, B,RP_mode=True), C_in, RP_mode=True)
        C_out = (A and B) or (B and C_in) or (A and C_in)
        return (C_out, S) if RP_mode else tuple(map(int, (C_out, S)))

    @staticmethod
    def TrafficLight_Status(R, A, G, RP_mode=False):
        """
        交通信号灯逻辑综合运算
        作用：对红黄绿三灯状态做组合逻辑判断
        参数：
            R, A, G : 任意 - 红灯/黄灯/绿灯状态（0 或 1）
            RP_mode : bool - False 返回 0/1，True 返回 False/True
        原理/输出：返回组合逻辑的综合结果（0/1 或 False/True）
        """
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
    L1 = DataStat("1.25.9",7,".8", "9.9.9.9",9, 5, 9, 6,"abc", 5, 23, 15,"12..52")
    print(L1.get())
    with Time("16的阶乘计算"):
        Factorial(16,RP_mode=True)
    with Time():
        Fibonacci_recursive_One(8,RP_mode=True)
    with Time():
        Find_All([7,3,3,2,4,6,9,3],Value=3,RP_mode=True)
    L2 = DataStat([15,None,6,79,5,656,23])
    print(L2.get())

if __name__ != "__main__":
    # 当作为模块导入时，导出所有公共函数
    __all__ = [
        'Factorial', 'Fibonacci_recursive_One', 'Fibonacci_recursive_All',
        'Arrangement', 'Combination', 'Public_Max', 'Public_Min',
        'ifPrime', 'Pol', 'Rec', 'QinJiuShao', 'HaiLun',
        'Find_All', 'Find_One', 'Factorization', 'Base_Decomp',
        'Perfect_Square', 'sqrt_reduce', 'self_power_num',
        'DataStat', 'Bool_Sum', 'MathError', 'Precision',
        'A', 'C', 'Fib_One', 'Fib_All',
        'Count_Power', 'GDN', 'Power','Time'
    ]
