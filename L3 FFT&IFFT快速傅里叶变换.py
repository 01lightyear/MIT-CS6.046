import cmath
def fft(a):
    """
    快速傅里叶变换（FFT）
    a: 输入多项式的系数表示（长度为 n 的列表，其中 n 必须为 2 的幂）
    返回：a 的频域表示（采样点形式）
    """
    n = len(a)
    if n == 1:
        return a
    # 将多项式分为偶数项和奇数项
    a_even = fft(a[0::2])  # 偶数项
    a_odd = fft(a[1::2])   # 奇数项
    # 计算单位根
    w_n = cmath.exp(2j * cmath.pi / n)  # e^(2*pi*i / n)
    w = 1
    # 合并
    y = [0] * n
    for k in range(n // 2):
        y[k] = a_even[k] + w * a_odd[k]
        y[k + n // 2] = a_even[k] - w * a_odd[k]
        w *= w_n  # 更新单位根
    return y
def ifft(a):
    """
    逆快速傅里叶变换（IFFT）
    a: 输入的频域表示（采样点形式）
    返回：a 的时域表示（系数表示）
    """
    n = len(a)
    if n == 1:
        return a
    # 将多项式分为偶数项和奇数项
    a_even = ifft(a[0::2])
    a_odd = ifft(a[1::2])
    # 计算单位根的共轭
    w_n = cmath.exp(-2j * cmath.pi / n)  # e^(-2*pi*i / n)
    w = 1
    # 合并
    y = [0] * n
    for k in range(n // 2):
        y[k] = a_even[k] + w * a_odd[k]
        y[k + n // 2] = a_even[k] - w * a_odd[k]
        w *= w_n
    return y
def polynomial_multiply(p1, p2):
    """
    使用FFT和IFFT进行多项式乘法
    p1: 第一个多项式的系数列表
    p2: 第二个多项式的系数列表
    返回：两个多项式乘积的系数列表
    """
    # 确保长度是2的幂
    n = 1
    while n < len(p1) + len(p2) - 1:
        n *= 2
    
    # 将多项式系数填充到长度为n
    p1_padded = p1 + [0] * (n - len(p1))  # 使用新变量避免修改原始输入
    p2_padded = p2 + [0] * (n - len(p2))
    
    # FFT
    fft_p1 = fft(p1_padded)
    fft_p2 = fft(p2_padded)
    
    # 逐点相乘
    fft_product = [fft_p1[i] * fft_p2[i] for i in range(n)]
    
    # IFFT
    product = ifft(fft_product)
    product = [y_i / n for y_i in product]  # 乘以n来抵消ifft中的除法
    # 取实部，并返回去掉浮点误差的整数部分
    # 使用更严格的取整方式，并只保留有效位数
    result = [round(c.real, 10) for c in product]
    return result[:len(p1) + len(p2) - 1]  # 只返回有效系数
# 定义多项式 A 和 B 的系数表示
A = [1, 2, 3]
B = [4, 5, 6]

# 使用FFT进行多项式乘法
result = polynomial_multiply(A, B)

print("A(x) * B(x) 的系数表示为:", result)
