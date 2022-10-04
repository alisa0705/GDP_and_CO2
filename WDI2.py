import pandas as pd
df=pd.read_csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")


# pull out the column
#newdf=df["Mortality rate, infant (per 1,000 live births)","GDP per capita (constant 2010 US$)","Country Name"]

newdf=df[["Mortality rate, infant (per 1,000 live births)","GDP per capita (constant 2010 US$)","Country Name"]]

#make plot
import matplotlib.pyplot as plt
plt.scatter(newdf["GDP per capita (constant 2010 US$)"],newdf["Mortality rate, infant (per 1,000 live births)"])

####change later
