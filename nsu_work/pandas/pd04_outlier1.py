# ★★★ 중요 ★★★


import numpy as np
aaa = np.array([-10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 50])

def outlier(data):
    quartile_1, q2, quartile_3 = np.percentile(data, [25, 50, 75])
    print("1사분위 : ", quartile_1)
    print("q2 : ", q2)
    print("3사분위 : ", quartile_3)
    iqr = quartile_3 - quartile_1
    print('IQR : ', iqr)
    lower_bound = quartile_1 - (iqr * 1.5) #  X(곱하기) 1.5 까진 봐준다
    upper_bound = quartile_3 + (iqr * 1.5) #  X(곱하기) 1.5 까진 봐준다
    return np.where((data > upper_bound) | (data < lower_bound)) , \
        iqr, lower_bound, upper_bound

outlier_loc, iqr, low, up = outlier(aaa)
print('이상치의 위치 : ', outlier_loc)

import matplotlib.pyplot as plt
plt.boxplot(aaa)
plt.axhline(up, color='red', label = 'upper_bound')
plt.axhline(low, color='blue', label = 'lower_bound')
plt.legend()
plt.show()

# 1사분위 :  4.0
# q2 :  7.0
# 3사분위 :  10.0 
# IQR :  6.0     3사분위 - 1사분위
# 이상치의 위치 :  (array([ 0, 12]),)    # 0 = -10, 12 = 50


# 원래는 y=wx+b 가 아닌 y=xw+b