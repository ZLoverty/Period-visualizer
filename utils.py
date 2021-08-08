import time
import matplotlib.pyplot as plt
import dufte
import numpy as np
plt.style.use(dufte.style)

class date:
    """
    Implement date algebra: add date, subtract two dates
    
    '8/7/2021' + 1 = '8/8/2021'
    '8/8/2021' - '/8/7/2021' = 1
    """
    def __init__(self, date_str):
        self.string = date_str
        self.format = '%m/%d/%Y'
        self.struct_time = time.strptime(date_str, self.format)
    def __add__(self, a):
        sec = time.mktime(self.struct_time)
        result = time.localtime(sec+a*24*3600)
        return time.strftime(self.format, result)
    def __repr__(self):
        return self.string
    def __sub__(self, another_date):
        assert(type(another_date)==date)
        t0 = time.mktime(self.struct_time)
        t1 = time.mktime(another_date.struct_time)
        return int((t0-t1) / 24 / 3600)
    
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
    """
    Visualize period data using bar plot.
    Features:
        - 2 scale options ('all' and 'year'), all is default
        - color the bars base on the deviation from 28 days (red, yellow and gray)
        - ...
    
    Args:
    date_list -- data read from period.txt, return value of read_date()
    lap -- lapse day of each period
    
    Returns:
    Nothing    
    """
    
    l = len(date_list)
    x = np.arange(0, l-1)
    ind = np.floor(np.linspace(0, l-2, 4)).astype('int')
    
    # generate color list
    
    c = []
    for lap_1 in lap:
        d = abs(lap_1-28)
        if d < 2:
            c.append('#9B99B6')
        elif d == 2:
            c.append('#D4D3E2')
        else:
            c.append('#93778A')
    
    fig, ax = plt.subplots(dpi=300)
    ax.bar(x, lap, color=c)
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