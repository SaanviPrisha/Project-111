import random
import statistics
import pandas as pd
import plotly_express = px 
import plotly.figure_factory as ff 
import plotly.graph_objects as go 

file1 = pd.read_csv("data.csv")
data = file1["id"].to_list()

datamean = statistics.mean(data)
datastdDev = statistics.stdev(data)

print("Mean of the data is {}".format(datamean))
print("Standard Deviation of the data is {}".format(datastdDev))

def randomSetOfMean(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

meanlist = []
for i in range(0,1000):
    SetOfMean = randomSetOfMean(100)
    meanlist.append(SetOfMean)

stdDev = statistics.stdev(meanlist)
mean = statistics.mean(meanlist)

firststdDevStart, firststdDevEnd = mean - stdDev, mean + stdDev
secondstdDevStart, secondstdDevEnd = mean - (2*stdDev), mean + (2*stdDev)
thirdstdDevStart, thirdstdDevEnd = mean - (3*stdDev), mean + (3*stdDev)

meanOfSample = statistics.mean(data)

print("Mean of Sampling Distribution", meanOfSample)

graph = ff.create_distplot([meanlist],["Population Mean"], show_hist = False)
graph.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17],mode = "lines",name = "Mean"))
graph.add_trace(go.Scatter(x=[meanOfSample, meanOfSample], y=[0,0.17],mode = "lines",name = "Mean of Sample"))
graph.add_trace(go.Scatter(x=[firststdDevEnd,firststdDevEnd], y=[0,0.17],mode = "lines",name = "Standard Deviation 1 end"))

graph.show()

zScore = (meanOfSample - mean)/stdDev
print("Z Score is ", zScore)