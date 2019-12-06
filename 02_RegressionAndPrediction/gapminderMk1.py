import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import time

data_url = 'http://bit.ly/2cLzoxH'
gapminder = pd.read_csv(data_url)
#print(gapminder.head(30))


def createCountryPlot(countryName, file):
        indx=0
        x=[]
        y=[]
        for index, row in file.iterrows():
            if(countryName ==  row['country']):
                x.append(row['year'])
                y.append(row['gdpPercap']/1000)
            indx=indx+1
        fig, ax = plt.subplots();
        xi = list(range(len(x)))

        plt.plot(y, label=countryName, color='red');
        plt.xticks(xi, x)
        plt.xlabel('year')
        plt.ylabel('GDP per Capita [k$]')
        plt.legend()
        ax.grid()
        plt.show()

def createCountryPlot(file, countryName, countryName2, parameter):
        indx=0
        x=[]
        y=[]
        for index, row in file.iterrows():
            if(countryName ==  row['country']):
                x.append(row['year'])
                if(parameter=='gdpPercap'):
                    y.append(row[parameter]/1000)
                else:
                    y.append(row[parameter])
            indx=indx+1
        fig, ax = plt.subplots();

        xx=[]
        yy=[]
        indx=0
        for index, row in file.iterrows():
                if(countryName2 ==  row['country']):
                        xx.append(row['year'])
                        if(parameter=='gdpPercap'):
                            yy.append(row[parameter]/1000)
                        else:
                            yy.append(row[parameter])
                indx=indx+1

        xxi = list(range(len(xx)))
        xi = list(range(len(x)))
        plt.plot(y, label=countryName, color='blue');

        plt.plot(yy, label=countryName2, color='red');

        plt.xticks(xi, x)
        plt.xticks(xxi, xx)
        plt.xlabel('year')
        if(parameter=='gdpPercap'):
            plt.ylabel('GDP per Capita [k$]')
        elif (parameter=='lifeExp'):
            plt.ylabel('Life expectancy [years]')
        plt.legend()
        ax.grid()
        plt.show()

def createSingleCountryComparison(file, countryName):
        indx=0
        x=[]
        y=[]
        for index, row in file.iterrows():
                if(countryName ==  row['country']):
                    x.append(row['gdpPercap']/1000)
                    y.append(row['lifeExp'])
                indx=indx+1
        fig, ax = plt.subplots();
        xi = list(range(len(x)))
        #plt.plot(y, label=countryName, color='blue');
        plt.plot(x, y, '.', color='red', label=countryName);
        plt.xticks(xi, x)
        plt.xlabel('GDP per Capita [k$]')
        plt.ylabel('Life Expectancy [years]')
        ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        plt.legend()
        ax.grid()
        plt.show()

def createDualCountryComparison(file, countryName, countryName2):
        indx=0
        xValue='gdpPercap';
        yValue='lifeExp'
        x=[]
        y=[]
        for index, row in file.iterrows():
                if(countryName ==  row['country']):
                    x.append(row[xValue])
                    y.append(row[yValue])
                indx=indx+1

        fig, ax = plt.subplots();
        indx=0
        xx=[]
        yy=[]
        for index, row in file.iterrows():
                if(countryName2 ==  row['country']):
                    xx.append(row[xValue])
                    yy.append(row[yValue])
                indx=indx+1

        xi = list(range(len(x)))
        xxi = list(range(len(xx)))

        #plt.plot(y, kind='scatter', label=countryName, color='blue');
        plt.plot(x, y, '.', color='blue', label=countryName);
        #plt.plot(yy, kind='scatter', label=countryName2, color='red');
        plt.plot(xx, yy, 'x', color='red', label=countryName2);
        #plt.xticks(xi, x)
        #plt.xticks(xxi, xx)
        plt.xlabel('GDP per Capita [k$]')
        plt.ylabel('Life Expectancy [years]')
        ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        plt.legend()
        ax.grid()
        plt.show()

def createGeneralOverview(gapminder):
        fig, ax = plt.subplots()
        gapminder.plot(kind='scatter', x='gdpPercap', y='lifeExp', ax=ax)
        # Turn on the grid
        ax.grid()
        plt.show()

#createGeneralOverview(gapminder)
#createCountryPlot(gapminder, "Sweden","Mexico", 'lifeExp')

#createSingleCountryComparison(gapminder, "Mexico")
createDualCountryComparison(gapminder, "Germany", 'Mexico')
