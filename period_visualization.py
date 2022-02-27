# %% codecell
from utils import *
# %% codecell
period_dir = r'period.txt'
date_list = read_date(period_dir)
lap = compute_lap(date_list)
plot_period(date_list, lap)
plt.savefig("period.jpg")
# %% markdown
# ## Development
#
# - deal with missing data
# - show data at different scale (year/month)
# %% codecell
def fix_missing_data(lap):
    """
    If for some months data are missing, estimate by the mean.
    For example, an element in lap is 60, divide into 2 months of 30 days.
    """

    for i, l in enumerate(lap):
        nMonth = np.around(l/28)
        if nMonth > 1:
            # recursive
            divided = []

# %% codecell
# test DataFrame
import pandas as pd
date_list = read_date(period_dir)
data = pd.DataFrame({'date_string': date_list})

lap = [np.nan]
for i in data.index[:-1]:
    lap_item = date(data['date_string'][i+1]) - date(data['date_string'][i])
    lap.append(lap_item)

data['lap'] = lap
