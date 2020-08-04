import matplotlib.pyplot as plt
import seaborn; seaborn.set()

def plot_data(data):
    fig, ax = plt.subplots()

    days = []
    world = []
    canada = []
    china = []
    finland = []
    italy = []
    south_korea = []
    us = []

    for i, line_list in enumerate(data):
        days.append(i)
        world.append(int(line_list[1]))
        canada.append(int(line_list[2]))
        china.append(int(line_list[3]))
        finland.append(int(line_list[4]))
        italy.append(int(line_list[5]))
        south_korea.append(int(line_list[6]))
        us.append(int(line_list[7]))

    ax.plot(days, world, label='World')
    ax.plot(days, canada, label='Canada')
    ax.plot(days, china, label='China')
    ax.plot(days, finland, label='Finland')
    ax.plot(days, italy, label='Italy')
    ax.plot(days, south_korea, label='South Korea')
    ax.plot(days, us, label='United States')

    ax.set_xlabel('Days (Day 0 = 12/31/2019)')
    ax.set_ylabel('Confirmed Cases')
    ax.set_title('Confirmed Cases of COVID-19 Per Day')
    ax.legend()

    plt.show()