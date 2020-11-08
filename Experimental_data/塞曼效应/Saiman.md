## 实验数据记录
### 不加磁场时
$$
D_{k-1}=\frac{7.792-0.272}{\sqrt{2}}\\
D_k=\frac{5.618-2.322}{\sqrt{2}}
$$
### 加入磁场时
$$
D_b=\frac{6.092-2.440}{\sqrt{2}}\\
D_a=\frac{5.350-3.134}{\sqrt{2}}
$$


```python
dic={}
dic['D_k_1']=(7.792-0.272)/2**0.5/1000
dic['D_k']=(5.618-2.322)/2**0.5/1000
dic['D_b']=(6.092-2.440)/2**0.5/1000
dic['D_a']=(5.350-3.134)/2**0.5/1000
for i in dic:
    print(i,'=','%.4e'%dic[i],'m')
```

    D_k_1 = 5.3174e-03 m
    D_k = 2.3306e-03 m
    D_b = 2.5824e-03 m
    D_a = 1.5669e-03 m


$$
标准具间隔圈厚度d=2mm\\
当U=30V时,B=920mT
$$
根据公式
$$
\frac{e}{m}=\frac{2\pi c(D_b^2-D_a^2)}{(M_2g_2-M_1g_1)dB(D_{k-1}^2-D_{k}^2)}
$$


```python
from scipy.constants import pi,c
d=2/1000
B=920/1000
print('d','=','%.4g'%d,'m')
print('B','=','%.4g'%B,'T')
em=2*pi*c*(dic['D_b']**2-dic['D_a']**2)/\
(d*B*(dic['D_k_1']**2-dic['D_k']**2))
print('e/m','=','%.4g'%em,'C/kg')
```

    d = 0.002 m
    B = 0.92 T
    e/m = 1.888e+11 C/kg


### 计算得出
$$
\frac{e}{m}=1.888\times10^{11}\ C/kg
$$


```python

```
