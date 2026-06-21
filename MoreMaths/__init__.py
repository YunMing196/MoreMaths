from MoreMaths import *
__doc__ : str
__doc__=\
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
        布尔运算RP_mode参数设置返回的是True/False还是1/0，值为False时返回布尔的，值为True时返回数字的
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
        - Population_Variance()        总体方差
        - Sample_Variance()            样本方差
        - Population_Std_Dev()         总体标准差
        - Sample_Std_Dev()             样本标准差
        - Median()                     中位数，返回数值
        - List_Product()               累乘，列表内所有元素的乘积
        - Data_Range()                 极差（最大值减最小值）
        - Mode()                       众数
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

if __name__ != "__main__":
    __all__ = [
        'Factorial', 'Fibonacci_recursive_One', 'Fibonacci_recursive_All',
        'Arrangement', 'Combination', 'Public_Max', 'Public_Min',
        'ifPrime', 'Pol', 'Rec', 'QinJiuShao', 'HaiLun',
        'Find_All', 'Find_One', 'Factorization', 'Base_Decomp',
        'Perfect_Square', 'sqrt_reduce', 'self_power_num',
        'DataStat', 'Bool_Sum', 'MathError', 'Precision', 'A', 'C',
        'Count_Power', 'GDN', 'Power',
        '__doc__'
    ]