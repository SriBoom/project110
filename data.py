import statistics
import csv
import pandas as pd
import random
import plotly.figure_factory as ff

df=pd.read_csv("medium_data.csv")
data=df["title"].tolist()

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df], ["Number of Articles"], show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_mean=random_set_of_mean(30)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
    mean=statistics.mean(mean_list)
    print(mean)

setup()

def main2():
    std_dev_list=[]
     #we are taking only 100 random data from the data
    for i in range(0,1000):
        random_index=random_set_of_mean(100)
        std_dev_list.append(random_index)
    show_fig(std_dev_list)
    standard_deviation=statistics.stdev(std_dev_list)
    print(standard_deviation)

main2()
