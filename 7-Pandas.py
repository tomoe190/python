#!/usr/bin/env python
# coding: utf-8

# # pandas--Python Data Analysis Library
# 官网：https://pandas.pydata.org/
# 
# Pandas中文网：https://www.pypandas.cn/
# 
# Pandas 精选资源：https://www.pypandas.cn/
# 
# Pandas 生态圈：https://www.pypandas.cn/
# 
# Pandas教程：http://www.ysir308.com/archives/category/tutorial/pandas-tutorial
# 
# 附录：
# - pandas中的index对象详解.ipynb
# - joyful-pandas-master文件夹

# In[1]:


#忽略级别 3 及以下的消息（级别 1 是提示，级别 2 是警告，级别 3 是错误）
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'


# In[97]:


from pandas import Series    #联系下一句，思考这样写的用意
import pandas as pd
import numpy as np


# ##  Pandas 中的数据类型 ####
# 
# Pandas的名称来自于面板数据（panel data）和python数据分析（data analysis）。panel data是经济学中关于多维数据集的一个术语，在Pandas中也提供了panel的数据类型。
# 
# Pandas 基于两种数据类型，series 和 dataframe。
# 
# - series 是一种一维的数据类型，其中的每个元素都有各自的索引，可以把它当作一个由带索引的元素组成的 numpy 一维数组。索引(index)可以是**数字或者字符**。
# 
# - dataframe 是一个二维的、表格型的数据结构。dataframe 可以储存许多**不同类型的数据**，并且**每个轴都有索引。**

# ### Series构建和引用

# In[98]:


s = Series([4, 7, -5, 3])    #可以用list构建
s


# In[99]:


s = Series((4, 7, -5, 3))    #可以用tuple构建
s


# In[100]:


s.index     #默认的index


# In[101]:


type(s.index)


# In[102]:


s.index = ['Bob', 'Steve', 'Jeff', 'Ryan']    #重新设置index
s


# In[103]:


s.index 


# In[104]:


s2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'a'])    #index的值可以相同
s2


# In[105]:


s2['a']   #index值索引


# In[106]:


sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
s3 = Series(sdata)      #用字典创建Series
s3


# In[107]:


states = ['California', 'Ohio', 'Oregon', 'Texas']
s4 = Series(sdata, index=states)    #用字典创建Series，另外给出index（可能与字典中的key值不完全符合）
s4


# In[108]:


s = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
s


# In[109]:


s['b']   #index值索引


# In[110]:


s[1]    #行号索引


# In[111]:


s[2:4]   #行号索引--切片不包括末尾


# In[112]:


s[['b', 'a', 'd']]  #index值索引


# In[113]:


s[[1, 3]]   #行号索引


# In[114]:


s


# In[115]:


s[s < 2]     #找出值<2的


# In[116]:


s < 2


# In[117]:


s


# In[118]:


s['a':'c']   #Series索引的切片运算和普通的切片运算不同--包含末端


# In[119]:


s['b':'c'] = 5    #切片赋值
s


# ### DataFrame构建与引用

# #### 构建一个空的DataFrame

# In[120]:


import pandas as pd
import numpy as np
df = pd.DataFrame()    
df


# In[121]:


type(df)


# In[122]:


pd.DataFrame(columns=['b','a', 'c', 'd', 'e'])    #指定列名


# #### 构建一个字符串DataFrame

# In[123]:


pd.DataFrame(np.array(list('abcdefgh')).reshape((4,2)))   #默认，按行排列


# #### 读取文件构建DataFrame

# In[124]:


DATA=pd.read_csv(r'd:\foo.csv')   #假定foo.csv文件放置在d:\
DATA


# In[125]:


DATA.index


# #### 创建日期索引的DataFrame

# In[126]:


dates = pd.date_range('20000226',periods=6)       #2000年是闰年
df_d = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
df_d


# In[127]:


df_d.index


# #### 用字典创建DataFrame，注意各项的value值个数要相同

# In[128]:


dic = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
DF = pd.DataFrame(dic)  
DF


# In[129]:


DF.index


# In[130]:


pd.DataFrame(dic, columns=['year', 'state', 'pop'])  #改变字段的顺序


# In[131]:


pd.DataFrame(dic, columns=['year', 'state', 'pp'])  #如果columns的值与data的key值不符


# In[132]:


DF1 = pd.DataFrame(dic, columns=['year', 'state', 'pop', 'debt'],
                   index=['one', 'two', 'three', 'four', 'five'])   #指定列名和index
DF1


# In[133]:


DF1.columns     #注意，columns也是Index


# In[134]:


a=DF1.year     #也可以用“.”的方式引用列
a


# In[135]:


type(a)


# In[136]:


DF1['year']    #也可以[ ]引用列


# In[137]:


DF1[['year','pop']]    #引用多列--使用list


# ### 快速查看整体信息

# In[2]:


import numpy as np
import pandas as pd


# .info()是DataFrame才可用的API，快捷查看多种信息：总行数和列数、每列元素类型和non-NaN的个数，总内存。
# 
#     DataFrame.info(verbose=None, memory_usage=True, null_counts=True)
# - verbose：True or False，字面意思是冗长的，也就说如果DataFrame有很多列，是否显示所有列的信息，如果为否，那么会省略一部分；
# - memory_usage：True or False，默认为True，是否查看DataFrame的内存使用情况；
# - null_counts：True or False，默认为True，是否统计NaN值的个数。

# In[6]:


df = pd.read_csv('golf.csv',sep=";")
df


# In[7]:


df.info()  # 直接默认设置即可


# In[8]:


df.shape  # (行数，列数)


# In[9]:


df.size   # 元素个数，rows×cols


# In[10]:


df.describe()  # 默认只对数值列进行统计 


# In[ ]:





# #### DataFrame 数据索引与选取，从这三个层次考虑：行列、区域、单元格。
# 其对应使用的方法如下：
# ##### 一. 行，列 --> df[ ]
# ##### 二. 区域   --> df.loc[ ], df.iloc[ ]
# ##### 三. 单元格 --> df.at[ ], df.iat[ ]

# In[ ]:





# In[ ]:





# In[ ]:





# ### index的用途总结：
# 
# 更方便的数据查询；
# - 使用index可以获得性能提升；
# - 自动的数据对齐功能；
# - 更多更强大的数据结构支持；
# 
# 使用index会提升查询性能
# - 如果index是唯一的，Pandas会使用哈希表优化，查询性能为O(1);
# - 如果index不是唯一的，但是有序，Pandas会使用二分查找算法，查询性能为O(logN);
# - 如果index是完全随机的，那么每次查询都要扫描全表，查询性能为O(N);

# In[67]:


df.index


# ### 一. df[ ]:一维,只能单独地针对行或列，不能合起来使用
# #####         行维度： 数字索引切片、索引切片、布尔列表、布尔Series
# -  即：如果 df[ ]中是切片、布尔，pandas认为是针对“行”---有整体感的
# -  简记为：[ ]--切片、布尔（有整体感的）针对“行”，字符、列表（没有整体感的）针对“列”

# In[144]:


import numpy as np
import pandas as pd
rng = np.random.RandomState(10)   # 设置随机局部种子
df = pd.DataFrame(rng.randn(6,4), index=list('abcdef'), columns=list('ABCD'))
df


# In[145]:


df.index


# In[ ]:





# In[146]:


df[:3]    #行号切片不包括尾


# In[147]:


df[2:3]   #行号切片不包括尾--单独一行


# In[148]:


df['a':'c']    #index切片包括尾


# In[149]:


df['a':'a']    #index切片包括尾--单独一行


# In[150]:


df[['a','c']]       #×   不能用行索引list


# In[151]:


df[[True,True,True,False,False,False]] # 前三行（布尔数组长度等于行数）


# In[152]:


df[df['A']>0] # A列值大于0的行


# In[153]:


df['A']>0


# In[154]:


type(df['A']>0)


# In[155]:


df[(df['A']>0) | (df['B']>0)] # A列值大于0，或者B列大于0的行,注意“df”外边的“()”


# In[156]:


df[(df['A']>0) & (df['B']>0)] # A列值大于0，并且B列大于0的行,注意“df”外边的“()”


# ##### 列维度：索引索引、索引列表
# #####  即：如果 df[ ]中是索引索引或索引列表，pandas识别为针对“列”
# -  简记为：[ ]--切片、布尔（有整体感的）针对“行”，字符、列表（没有整体感的）针对“列”

# In[157]:


df['A']    


# In[158]:


df['A':'C']     #×  列维度不能用切片,行维度可以


# In[159]:


df[['A','B']]     #列维度用索引列表


# In[160]:


df['A','B']       #里面要写成列表--加上[ ]


# In[161]:


df[['A','B']]   


# In[162]:


import numpy as np
import pandas as pd
rng = np.random.RandomState(10)   # 设置随机局部种子
df = pd.DataFrame(rng.randn(6,4), index=list('abcdef'), columns=list('ABCD'))
df


# ### 二. df.loc[ ] ：引用区域，二维，先行后列
# - 行维度：单个索引及切片、索引list、布尔list、布尔Series
# - 列维度：单个索引及切片、索引list、布尔list、布尔Series
# - 简记为：loc--索引所有及布尔

# In[186]:


import numpy as np
import pandas as pd
rng = np.random.RandomState(10)   # 设置随机局部种子
df = pd.DataFrame(rng.randn(6,4), index=list('abcdef'), columns=list('ABCD'))
df


# In[187]:


df


# In[188]:


df.loc['a', :]


# In[189]:


df.loc['a']     #引用行可以省略后边的“：”


# In[190]:


df.loc['a':'d', :]      #索引切片包括终值,索引的取值可能无规律，不便知道下一个取值


# In[191]:


df.loc['a':'d']      #引用行可以省略后边的“：”


# In[192]:


df.loc[['a','b','d'], :]


# In[193]:


df.loc[['a','b','d']]      #引用行可以省略后边的“：”


# In[194]:


df.loc[[True,True,True,False,False,False], :] # 前三行（布尔数组长度等于行数）


# In[195]:


df.loc[df['A']>0, :]


# In[196]:


df['A']>0


# In[197]:


type(df['A']>0)


# In[198]:


df.loc[:, 'A'] 


# In[199]:


df['A']        #与上句等效


# In[200]:


df.loc[:, 'A':'C']


# In[201]:


df.loc[,'A':'C']     #引用列不能省略前边的“：”


# In[202]:


df.loc[:, ['A','C']]


# In[203]:


df.loc[:, [True,True,True,False]] # 前三列（布尔列表长度等于列数）


# In[204]:


type([True,True,True,False])


# In[205]:


df.loc[:, df.loc['a']>0]          # a行大于0的列


# In[206]:


df.loc['a']>0


# In[207]:


type(df.loc['a']>0)


# In[208]:


df.loc[df['A']>0, :]          # A列大于0的行


# In[209]:


df['A']>0


# In[210]:


type(df['A']>0)


# In[211]:


df.loc[['a','c','f'], df.columns[2]]  #loc中使用列号


# In[212]:


df.columns[2]


# In[213]:


df


# In[214]:


df.loc[['a','c','f'], df.columns[:2]]        #loc中使用列号列表


# In[215]:


df.columns[:2]


# In[216]:


df.loc[['a','c','f'], ['A','C','D']]   #用loc索引列表取某些行中的某些列-不连续


# In[217]:


df.loc['c':'f', 'B':'D']     #用loc索引切片取某些行中的某些列--连续


# 数字索引

# In[220]:


import numpy as np
import pandas as pd
df = pd.read_csv('data/table.csv',index_col='ID')
df


# In[221]:


df.index


# In[222]:


df.loc[1103]


# In[223]:


df.loc[[1102,2304]]


# In[224]:


df.loc[1304:2103]


# In[225]:


df.loc[2402::-1]


# In[227]:


df.loc[[1101,1102,1105]]


# In[ ]:





# ### 三、 df.iloc[ ]---i(int)表示行号：二维，先行后列
# - 行维度：行号索引、行号切片、行号list、（行号）布尔list
# - 列维度：列号索引、列号切片、列号list、（列号）布尔list
# - 简记为：iloc--行列号所有及布列

# In[230]:


import numpy as np
import pandas as pd
rng = np.random.RandomState(10)   # 设置随机局部种子
df = pd.DataFrame(rng.randn(6,4), index=list('abcdef'), columns=list('ABCD'))
df


# In[232]:


df.iloc[3, :]


# In[74]:


df.iloc[3]


# In[75]:


df.iloc[:3, :]


# In[76]:


df.iloc[[0,2,4], :]


# In[233]:


df.iloc[[True,True,True,False,False,False], :] # 前三行（布尔数组长度等于行数）


# In[234]:


df.iloc[df['A']>0, :]    #  ×   本意是取出A列中>0的所有行 


# In[81]:


df['A']>0          


# In[236]:


type(df['A']>0)   #不是单纯的布尔list


# In[237]:


df.iloc[df.loc[:,'A']>0, :]        #  ×   本意是取出A列中>0的行   


# In[238]:


df.loc[:,'A']>0


# In[239]:


type(df.loc[:,'A']>0)       #不是单纯的布尔list


# In[240]:


df.loc[df.loc[:,'A']>0, :]      #改用本句即可 


# In[241]:


df.iloc[:, df.loc['a']>0]         # ×  本意是取出a行中>0的列


# In[242]:


df.loc['a']>0


# In[243]:


type(df.loc['a']>0)


# In[244]:


df.loc[:, df.loc['a']>0]     #改用本句即可


# In[245]:


df


# In[246]:


df.iloc[:, 1]   #记住是从“0”列开始


# In[247]:


df.iloc[:, 0:3]


# In[248]:


df.iloc[:, [0,2]]


# In[249]:


df.iloc[:, [True,True,True,False]] # 前三列（布尔数组长度等于行数）


# In[250]:


df.iloc[[0,2], [0,2]]    #用iloc序号列表取某些行中的某些列-不连续


# In[251]:


df.iloc[0:2, 0:2]      #用iloc序号切片取某些行中的某些列-连续


# In[252]:


df.loc[df.iloc[:,0]>0, :]    #第0列>0的行


# In[253]:


df.iloc[:,0]>0


# In[254]:


df.loc[:,df.iloc[0,:]>0]    #第0行>0的列


# In[255]:


df.iloc[0,:]>0


# In[256]:


df.loc[:, df.iloc[0]>0]           # 0行大于0的列,iloc中只有一个数字，是行


# ### 四、 df.at[ ]:用索引精确定位单元格
# - 行维度：索引索引
# - 列维度：索引索引

# In[257]:


df


# In[100]:


df.at['a', 'A']


# In[101]:


df.at[0, 'A']    #不能使用序号


# ### 五、 df.iat[ ]：用序号精确定位单元格
# 
# - 行维度： 数字索引（行号）索引
# - 列维度： 数字索引（列号）索引

# In[102]:


df


# In[120]:


df.iat[0, 0]


# In[121]:


df.iat['a', 0]    #不能使用索引


# ### 以下的选讲

# ### Dropping entries from an axis--删除指定轴上的项

# In[ ]:


from pandas import Series, DataFrame    
import pandas as pd
import numpy as np


# ##### 删除Series的项--明确指定index

# In[ ]:


s = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
s


# In[ ]:


new_s = s.drop('c')
new_s


# In[ ]:


s         #自身未变


# In[ ]:


data = DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
data


# In[ ]:


data1=data.drop(['Colorado', 'Ohio'])   #删除某二行
data1


# In[ ]:


data2=data.drop('Colorado')         #删除某一行
data2


# In[ ]:


data     #自身未变


# In[ ]:


data.drop('Colorado',inplace=True)      #   inplace=True 就地操作
data


# In[ ]:


data3=data.drop('two', axis=1)   #删除“列”，要指定 axis=1
data3


# In[ ]:


data


# In[ ]:


data4=data.drop(['two', 'four'], axis=1)
data4


# In[ ]:


data


# In[ ]:


del data['two']   #删除“列”---与以上的区别是，这是“就地操作”
data


# ##### 删除Series的项--未明确指定index

# In[ ]:


s1 = Series(np.arange(5.))
s1


# In[ ]:


s2=s1.drop([0])
s2


# In[ ]:


s1     #自身未变


# In[ ]:


s3=s1.drop([0,2])
s3


# In[ ]:


di = pd.Index(np.arange(3))
di


# In[ ]:


s4=s1.drop(di)
s4


# #### shift函数:对数据进行移动的操作

# In[ ]:


from pandas import Series, DataFrame
df = DataFrame([1,2,3,4], index=list('ABCD'),columns=['value1'])
df


# In[ ]:


df.shift()   #数据依次下移1行


# In[ ]:


df.shift(2) #数据依次下移2行


# In[ ]:


df.shift(-1) #数据依次上移1行


# In[ ]:


df


# #### DataFrame之间数学运算

# In[ ]:


frame


# In[ ]:


df1 = DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
                index=['Ohio', 'Texas', 'Colorado'])
df1


# In[ ]:


df2 = DataFrame(np.arange(12).reshape((4, 3)), columns=list('bde'),
                index=['Utah', 'Ohio', 'Texas', 'Oregon'])
df2


# In[ ]:


df1 + df2     #行、列扩充为二者的并集，具有相同行列index的值相加，否则置为NaN


# #### Arithmetic methods with fill values

# In[ ]:


df1 = DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
df1


# In[ ]:


df2


# In[ ]:


df1 + df2


# In[ ]:


df1


# In[ ]:


df2


# In[ ]:


df1.add(df2, fill_value=0)   #与df2比较，df1中空缺的地方置为0，然后二者相加


# In[ ]:


df1    #自身未变


# In[ ]:


df2


# In[ ]:


df1.reindex(columns=df2.columns, fill_value=0)       #按照df2的列设置df1的列，空缺的值置为0


# #### Operations between DataFrame and Series

# In[ ]:


from pandas import Series, DataFrame   
import pandas as pd
import numpy as np
frame = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])
s = frame.iloc[0]
frame


# In[ ]:


s 


# In[ ]:


type(s)


# In[ ]:


frame - s  #按列匹配，（充填）相减


# In[ ]:


s2 = Series(range(3), index=['b', 'e', 'f'])
s2


# In[ ]:


frame


# In[ ]:


frame + s2     #按列名（index）匹配，匹配不上的地方置为NaN


# In[ ]:


frame * s2     #按列名（index）匹配，匹配不上的地方置为NaN


# In[ ]:


s3 = frame['d']
s3


# In[ ]:


frame


# In[ ]:


frame + s3     #按列名（index）匹配，匹配不上的地方置为NaN


# In[ ]:


frame.add(s3, axis=0)   #每列都加上series3,必须注明“axis=0”


# In[ ]:


frame    


# ### Function application and mapping

# In[ ]:


from pandas import Series, DataFrame   
import pandas as pd
import numpy as np


# In[ ]:


frame = DataFrame(np.random.randn(4, 3), columns=list('bde'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])
frame


# In[ ]:


np.abs(frame)


# In[ ]:


f = lambda x: x.max() - x.min()


# In[ ]:


frame.apply(f)    #每列的最大值减去最小值


# In[ ]:


frame.apply(f, axis=1)   #每行的最大值减去最小值


# In[ ]:


def f(x):
    return Series([x.min(), x.max()], index=['min', 'max'])
frame.apply(f)    #默认是应用到“列”


# In[ ]:


frame


# In[ ]:


format = lambda x: '%.2f' % x
frame.applymap(format)        #输出二位小数的


# In[ ]:


frame['e'].map(format)


# ### Sorting 

# In[ ]:


from pandas import Series, DataFrame    
import pandas as pd
import numpy as np
s = Series(range(4), index=['d', 'a', 'b', 'c'])
s


# In[ ]:


s.sort_index()     #升序排列index,默认是inplace=False，若添加inplace=True，则是就地处理


# In[ ]:


s


# In[ ]:


frame = DataFrame(np.arange(8).reshape((2, 4)), index=['r2', 'r1'],
                  columns=['d', 'a', 'b', 'c'])
frame


# In[ ]:


frame.sort_index()


# In[ ]:


frame.sort_index(axis=1)   #列名按升序排列


# In[ ]:


frame.sort_index(axis=1, ascending=False)#列名按降序排列


# In[ ]:


s = Series([4, 7, -3, 2])
s.sort_values()    #value值按升序排列


# In[ ]:


s = Series([4, np.nan, 7, np.nan, -3, 2])
s.sort_values() 


# In[ ]:


frame = DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
frame


# In[ ]:


frame.sort_values(by='b')    #按照b列的值升序排列


# In[ ]:


frame.sort_values(by=['a', 'b'])   #升序排列，先按a列，再按b列


# ## Summarizing and computing descriptive statistics

# In[ ]:


df = DataFrame([[1.4, np.nan], [7.1, -4.5],
                [np.nan, np.nan], [0.75, -1.3]],
               index=['a', 'b', 'c', 'd'],
               columns=['one', 'two'])
df


# In[ ]:


df.sum()   #按列sum


# In[ ]:


df.sum(axis=1)   #按行sum


# In[ ]:


df.mean(axis=1, skipna=False)   #有NaN没法算


# In[ ]:


df.idxmax()  #各列最大值的index


# In[ ]:


df


# In[ ]:


df.cumsum()   #每列按行累加


# In[ ]:


df.describe()   #给出常见的统计量


# In[ ]:


s = Series(['a', 'a', 'b', 'c'] * 4)
s


# In[ ]:


s.describe()


# ### Filtering out missing data

# In[ ]:


from pandas import Series, DataFrame    
import pandas as pd
import numpy as np
from numpy import nan as NA


# In[ ]:


data = Series([1, NA, 3.5, NA, 7])
data


# In[ ]:


data.dropna()


# In[ ]:


data[data.notnull()]


# In[ ]:


data = DataFrame([[1., 6.5, 3.], [1., NA, NA],
                  [NA, NA, NA], [NA, 6.5, 3.]])
data


# In[ ]:


cleaned = data.dropna()      #删除存在NaN的行
cleaned


# In[ ]:


data.dropna(how='all')    #删除存所有取值为NaN的行


# In[ ]:


data


# In[ ]:


data[4] = NA    #名称为“4”的列赋值为NaN
data


# In[ ]:


data.dropna(axis=1, how='all')   #删除存所有取值为NaN的列


# In[ ]:


df = DataFrame(np.random.randn(7, 3))
df


# In[ ]:


df.iloc[:4, 1] = NA    
df


# In[ ]:


df.iloc[:5, 2] = NA    
df


# In[ ]:


df.dropna(thresh=2)    #保留至少2个非空值的行


# ### Filling in missing data

# In[ ]:


df


# In[ ]:


df.fillna(0)   #空缺值用0填充


# In[ ]:


df.fillna({1: 0.5, 2: -1})    #“1”列空缺值用0.5填充，“2”列空缺值用-1填充


# In[ ]:


df


# In[ ]:


# always returns a reference to the filled sect
df.fillna(0, inplace=True)  #就地修改
df


# In[ ]:


df = DataFrame(np.random.randn(6, 3))
df


# In[ ]:


df.iloc[2:, 1] = NA
df


# In[ ]:


df.iloc[4:, 2] = NA
df


# In[ ]:


df.fillna(method='ffill')   #向上看


# In[ ]:


df


# In[ ]:


df.fillna(method='ffill', limit=2)   #限制可以连续填充的最大数量为2--还是向上看


# In[ ]:


data = Series([1., NA, 3.5, NA, 7])
data


# In[ ]:


data.fillna(data.mean())   #用平均值填充，缺失值不算个数


# ## Hierarchical indexing(选讲)

# In[ ]:


data = Series(np.random.randn(10),
              index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                     [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])  #双重的index
data


# In[ ]:


data.index


# In[ ]:


data['b']


# In[ ]:


data['b':'c']


# In[ ]:


data.loc[['b', 'd']]


# In[ ]:


data


# In[ ]:


data[:, 2]   #所有层中的第二个


# In[ ]:


d=data.unstack()
d


# In[ ]:


d.stack()


# In[ ]:


frame = DataFrame(np.arange(12).reshape((4, 3)),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=[['Ohio', 'Ohio', 'Colorado'],
                           ['Green', 'Red', 'Green']])  #纵横都是双重index
frame


# In[ ]:


#给纵横的双重index命名
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
frame


# In[ ]:


frame['Ohio']


# ### Reordering and sorting levels（选讲）

# In[ ]:


frame


# In[ ]:


frame.swaplevel('key1', 'key2')


# In[ ]:


frame


# In[ ]:


frame.sort_index(1)    #按照第1个index排序--注意index的序号是从0开始


# In[ ]:


frame


# In[ ]:


frame.swaplevel(0, 1).sort_index(0)  #首先交换index 0,1，然后按照0-index排序


# ## Other pandas topics--选讲

# ### Integer indexing

# In[ ]:


ser = Series(np.arange(3.))
ser


# In[ ]:


ser.iloc[-1]


# In[ ]:


ser[-1]      #没有指定的index，此种用法不行


# In[ ]:


ser2 = Series(np.arange(3.), index=['a', 'b', 'c'])
ser2


# In[ ]:


ser2[-1]      #有指定index时 


# In[ ]:


ser.iloc[:1]


# In[ ]:


type(ser.iloc[:1])


# In[ ]:


ser3 = Series(range(3), index=[-5, 1, 3])
ser3


# In[ ]:


ser3.iloc[2]


# In[ ]:


type(ser3.iloc[2])


# In[ ]:


frame = DataFrame(np.arange(6).reshape((3, 2)), index=[2, 0, 1])
frame


# In[ ]:


frame.iloc[0]


# ### ranking(选讲)

# In[ ]:


from pandas import Series, DataFrame    
import pandas as pd
import numpy as np
s = Series(range(4), index=['d', 'a', 'b', 'c'])
s


# In[ ]:


s.rank()       #排名--同等地位


# In[ ]:


s.rank(method='first')   #升序--按照从上到下出现的顺序排名


# In[ ]:


s


# In[ ]:


s.rank(ascending=False, method='max')   #降序--按排名的“较大”值


# In[ ]:


frame = DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1],
                   'c': [-2, 5, 8, -2.5]})
frame


# In[ ]:


frame.rank(axis=1)   #每行按列排名--升序


# In[ ]:


import pandas as pd

data = pd.read_csv('https://raw.github.com/pydata/pandas/master/pandas/tests/data/iris.csv')

data.head()


# In[ ]:


from pandas.tools.plotting import andrews_curves

plt.figure()

andrews_curves(data, 'Name')


# 表格函数应用
可以通过将函数和适当数量的参数作为管道参数来执行自定义操作。 因此，对整个DataFrame执行操作。
例如，为DataFrame中的所有元素相加一个值2。
# In[99]:


import pandas as pd
import numpy as np

def adder(ele1,ele2):
   return ele1+ele2

np.random.seed(293423)
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df


# In[101]:


df.pipe(adder,2)


# 行或列合理函数应用可以使用apply()方法沿DataFrame或Panel的轴应用任意函数，它与描述性统计方法一样，采用可选的axis参数。 
# 
# 默认情况下，操作按列执行，将每列列为数组。

# In[102]:


import pandas as pd
import numpy as np

np.random.seed(293423)
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df


# In[103]:


df.apply(np.mean)  #默认情况下，axis=0：操作按列执行


# In[105]:


df.apply(np.mean,axis=1)    #axis=1:对行操作


# In[ ]:




