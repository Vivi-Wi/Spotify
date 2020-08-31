#!/usr/bin/env python
# coding: utf-8

# # Set up

import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from collections import Counter

# # Simple annual line graph

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
    c=dict(c.most_common(50))

    wordcloud = WordCloud(collocations=False, max_words=500, background_color='white').generate_from_frequencies(c)
    plt.figure().set_size_inches(18.5, 10.5)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

