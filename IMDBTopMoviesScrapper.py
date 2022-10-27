# -*- coding: utf-8 -*-
from lxml import html
import requests
import numpy as np
import pandas as pd
#%%
urlM = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
urlTV = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
xpathB = '//strong | //*[contains(concat( " ", @class, " " ), concat( " ", "titleColumn", " " ))]'
#%%
page = requests.get(urlM)
tree = html.fromstring(page.content) 
muvs = tree.xpath(xpathB)
#print(muvs)
muvs = list(map(lambda x: x.text_content(), muvs))
muvs = list(zip(*[iter(muvs)]*2))
muvs1 = list(zip(*muvs))[0]
muvs2 = list(zip(*muvs))[1]
#%%
muvsF1 = list(map(lambda x: str(x)[1:].split("\n")[:-1], muvs1))
#print(muvsF1)
#%%
muvsF2 = list(map(lambda x: list(map(lambda y: y.strip(), x)), muvsF1))
#print(muvsF2)
#%%
muvsF3 = list(map(lambda x: tuple(x), muvsF2))
#print(muvsF3)
#%%
col1 = list(zip(*muvsF3))[0]
col1 = list(map(lambda x: x.replace(".",""), col1))
col2 = list(zip(*muvsF3))[1]
col3 = list(zip(*muvsF3))[2]
col3 = list(map(lambda x: x.replace("(","").replace(")",""), col3))
#%%
table = np.transpose(np.vstack((np.array(col1), np.array(col2), np.array(col3), np.array(muvs2))))
df = pd.DataFrame(table)
print(df)