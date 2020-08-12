#!/usr/bin/env python
# coding: utf-8

# # Set up

# In[15]:


import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt

from bokeh.plotting import figure
from bokeh.io import output_notebook, show, output_file
from bokeh.models import ColumnDataSource, HoverTool, Panel
from bokeh.models.widgets import Tabs

from wordcloud import WordCloud, ImageColorGenerator
from collections import Counter


# # Simple annual line graph

# In[18]:


def year_plot(y, df, hue=None, palette="viridis"):
    g = sns.relplot(x='year',
                    y=y,
                    height=5,
                    aspect=1.5,
                    facet_kws=dict(sharex=False),
                    palette=palette,
                    kind="line",
                    legend="full",
                    hue=hue,
                    estimator=np.median,
                    data=df)


# # Dataframe wordcloud

# In[19]:


def wc(data):
    '''
    Takes in a dataframe, removes ' and returns a wordcloud graph based on the 
    frequencies of the expressions within the entire frame.
    '''
    dicts=[]
    for col in data:
        try:
            data[col]=data[col].str.replace("'","")
        except:
            pass
        dicts.append(data[col].value_counts().to_dict())

    c = Counter()
    for d in dicts:
        c.update(d)    

    wordcloud = WordCloud(collocations=False, max_words=500, background_color="white").generate_from_frequencies(c)
    plt.figure().set_size_inches(18.5, 10.5)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

