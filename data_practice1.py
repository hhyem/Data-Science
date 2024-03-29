# -*- coding: utf-8 -*-
"""data_practice1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wIvWonS66jEWxxVqX1aSRDiWvxd-QAxq
"""

import pandas as pd
import numpy as np
import seaborn as sns

"""1. 폰트 설정"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

# %matplotlib inline

"""1-1. 파일 불러오기"""

df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/hospitalList.csv", encoding="cp949")
df.shape

df

"""2. 기본정보 확인"""

df.columns

"""3. 결측치 확인"""

df.isnull().sum()

"""4. 결측치 제거"""

nullData = df.isnull() #dropna : 결측치인 값 제거

nullData #결측치가 없기 때문에 제대로 나오지 않는다.

"""5. 일부 데이터 요약하기"""

df.info()

df.head(5)

df.tail(5)

df.describe() #NaN 값을 제외하고 데이터셋 분포의 분산과 형태를 확인한다.

df['기준일'].max()

df.max() #min, mean, median 으로 활용 가능

"""6. value_counts로 값 집계하기, 값 정렬하기 (sort_values)"""

df.value_counts() #고유값 개수

df['연번'].value_counts()

#sort_values : 값을 기준으로 레이블 정렬하는 메소드

df.sort_values(by='진료과수') #진료과수를 기준으로 오름차순 정렬

"""7. 기초 통계값 (mean, median, max, min, count, describe, unique, nunique)"""



