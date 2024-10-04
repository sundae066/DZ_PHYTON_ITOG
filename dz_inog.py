import pandas as pd
import random

# Генерация DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразование в one hot вид
one_hot = pd.Series(data['whoAmI']).str.get_dummies()
print(one_hot.head())