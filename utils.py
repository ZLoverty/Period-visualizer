import time
import matplotlib.pyplot as plt
import dufte
import numpy as np
plt.style.use(dufte.style)

def read_date(period_dir):
    L = []
    with open(period_dir, 'r') as f:
        while True:
            a = f.readline()
            if a == '':
                break        
            L.append(a.replace('\n', ''))
    return L
def compute_lap(date_list):
    count = 0
    lapL = []
    for l in date_list:
        date = l.split('/')
        t = (int(date[2]), int(date[0]), int(date[1]), 0, 0, 0, 0, 0, 0)
        if count == 0:        
            t0 = time.mktime(t)
            count += 1
        else:
            count += 1
            t1 = time.mktime(t)
            lap = (t1 - t0) / 24 / 3600
            lapL.append(lap)
            t0 = t1
    return lapL
def plot_period(date_list, lap):
    l = len(date_list)
    x = np.arange(0, l-1)
    ind = np.floor(np.linspace(0, l-2, 4)).astype('int')
    fig, ax = plt.subplots(dpi=300)
    ax.bar(x, lap)
    ax.set_xticks(x[ind])
    ax.set_xticklabels(date_to_month(date_list, ind))
    for i in range(26, 30):
        if i == 28:
            ax.plot([0, l], [28, 28], color='#098d36', ls='--', lw=2)
        ax.plot([0, l], [i, i], ls='--', color='gray', lw=0.5)     
    dufte.legend()
    ax.set_ylim([22, np.array(lap).max()])
    ax.set_yticks(range(25, 31))
    ax.set_yticklabels(range(25, 31))
    
def date_to_month(date_list, ind):
    """
    Convert date list to month list (strings)
    e.g. 2/28/2020 -> 'Feb'
    """
    mapper = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 
              7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    month_list = []

    for i in ind:
        date = date_list[i]
        month = int(date.split('/')[0])
        month_str = mapper[month]
        month_list.append(month_str)
    
    return month_list