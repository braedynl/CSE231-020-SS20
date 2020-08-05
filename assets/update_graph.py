from datetime import datetime, timedelta
from urllib.request import urlopen, urlretrieve

import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
from matplotlib.dates import DateFormatter, drange

import seaborn; seaborn.set()


COUNTIES = ['Wayne', 'Kent', 'Washtenaw', 'Ingham', 'Macomb']


def plot_county_data(filename):
    df = pd.read_excel(filename, sheet_name='Data', dtype=str)
    df = df[df['CASE_STATUS'] == 'Confirmed']
    df = df[df['COUNTY'].isin(COUNTIES)]

    fig, ax = plt.subplots()

    for county in COUNTIES:
        county_data = df[df['COUNTY'] == county]

        d1 = datetime.strptime(county_data.head(1)['Date'].values[0][:10], '%Y-%m-%d')
        d2 = datetime.strptime(county_data.tail(1)['Date'].values[0][:10], '%Y-%m-%d')
        delta = timedelta(1)

        dates = drange(d1, d2 + delta, delta)
        cases = county_data['Cases'].to_numpy(dtype=int)

        ax.plot_date(dates, cases, '-', label=county)

    ax.xaxis.set_major_formatter(DateFormatter('%m/%d/%Y'))
    ax.set_title('Confirmed Cases of COVID-19 in Michigan by County')
    ax.set_xlabel('Date')
    ax.set_ylabel('Confirmed Cases')
    ax.legend()

    plt.savefig('assets/images/covid_data.png')

def main():
    filename = 'assets/covid_data.xlsx'

    soup = BeautifulSoup(urlopen('https://www.michigan.gov/coronavirus/0,9753,7-406-98163_98173---,00.html'), features='html.parser')
    link = 'https://www.michigan.gov' + soup.find('a', text='Cases by County by Date').get('href')
    urlretrieve(link, filename=filename)

    plot_county_data(filename)

if __name__ == '__main__':
    main()
