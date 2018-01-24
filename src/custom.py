import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image
from bokeh.io import show, output_notebook , output_file
from bokeh.models import (
    GMapPlot, GMapOptions, ColumnDataSource, Circle, Range1d, PanTool, WheelZoomTool, BoxSelectTool, HoverTool)
output_notebook()

def clean_file(filename):
    '''Reads in the path and filename for the terroist attack file then cleans and Returns
    it into a Pandas DataFrame
    INPUT:
    filename as a string
    OUTPUT:
    df as Pandas DataFrame
    '''

    #Read the lines of the file
    with open(filename) as f:
        content = f.readlines()

    #Grab the first row for the column labels
    column_labels = content[0].strip('\n')
    column_labels = column_labels.split(',')

    #Create a list of lists of the content
    content_lst =[]
    for i in range(1,len(content)):

        #Remove the \n (next line) and split the line of text at the ,
        line =content[i].strip('\n').split(',')

        #Checking that the number of columns in the line matches the column labels
        if len(line)== len(column_labels):
            content_lst.append(content[i].strip('\n').split(','))
    #Create a Pandas DataFrame from the content list and column_labels
    df = pd.DataFrame.from_records(content_lst, columns = column_labels)

    #Turn the latitude and Longitude columns into float type
    df['latitude']=df['latitude'].map(lambda x: x.strip(''))
    df['latitude']=df['latitude'].map(lambda x: np.nan if x == '' else x)
    df['latitude']=df['latitude'].astype('float')
    df['latitude']=df['latitude'].map(lambda x: np.round(x,2))
    df['longitude']=df['longitude'].map(lambda x: x.strip(''))
    df['longitude']=df['longitude'].map(lambda x: np.nan if x == '' else x)
    df['longitude']=df['longitude'].astype('float')
    df['longitude']=df['longitude'].map(lambda x: np.round(x,2))
    df = df[~df.isin([np.nan, np.inf, -np.inf, None]).any(1)]

    return df
