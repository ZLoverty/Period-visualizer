from utils import *

period_dir = r'period.txt'
date_list = read_date(period_dir)
lap = compute_lap(date_list)
plot_period(date_list, lap)
plt.savefig("period.jpg")
