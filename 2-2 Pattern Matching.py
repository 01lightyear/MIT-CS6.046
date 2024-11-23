'''
利用快速傅里叶变换作多项式乘法，发现当匹配是乘积为0或1
'''
import numpy as np
def matching(source,pattern):
    k=0
    for i in pattern:#记录非*项数
        if i!='*':
            k+=1
    source_list=[1.0 if x=='a' else -1.0 for x in source]
    pattern_list=[1.0 if x=='a' else -1.0 if x=='b' else 0.0 for x in pattern]
    pattern_list.reverse()
    n=len(source_list)+len(pattern_list)-1
    fft=np.fft.ifft(np.fft.fft(source_list,n)*np.fft.fft(pattern_list,n)).real
    matching_list=[]
    for i in range(0,len(fft)+1-len(pattern)):
        if abs(fft[i]-k)<1e-9:
            matching_list.append(i-(len(pattern)-1))
    for j in matching_list:
        print(j)
source='abaabaaaa'
pattern='a*ba*'
matching(source,pattern)