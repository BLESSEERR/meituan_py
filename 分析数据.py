import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
data=pd.read_excel('美团数据.xlsx')
data1=data.groupby(by=['店铺地址'])['店铺名称'].count().reset_index()
data1=data1.sort_values('店铺名称',ascending=True)[-10:]
print(data1)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置加载的字体名
plt.rcParams['axes.unicode_minus'] = False   # 解决保存图像是负号'-'显示为方块的问题

#店铺评分分析
fig,axes=plt.subplots(2,1,figsize=(12,12))
sns.regplot(x='人均金额',y='评分',data=data,color='r',marker='+',ax=axes[0])
sns.regplot(x='店铺评论数',y='评分',data=data,color='g',marker='*',ax=axes[1])
plt.show()

##条形图
x=data1['店铺地址']
y=data1['店铺名称']
plt.barh(x,y)
plt.xlabel('不同地区店铺数量')
plt.show()
#评论数分布
# 店铺评论数分布
data.店铺评论数.plot.hist(bins=10)
plt.title("店铺评论数分布")
plt.show()
print(data)