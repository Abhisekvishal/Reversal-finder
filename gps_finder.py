# This code finds possible reversal setups (gps setups & dps setups)
# for next day market


from nsetools import Nse
from csv_writer import append_list_as_row, csv_header, clear_csv
import time
import pandas as pd

start_time = time.time()

# stocks name
fno_stock_name = ['MANAPPURAM', 'INFRATEL', 'JINDALSTEL', 'GLENMARK', 'M&MFIN', 'INDUSINDBK', 'BHARTIARTL', 'BIOCON',
                  'IBULHSGFIN', 'RBLBANK', 'TATACONSUM', 'TATACHEM', 'ZEEL', 'EXIDEIND', 'PETRONET', 'VEDL',
                  'BANDHANBNK', 'ADANIPORTS', 'CHOLAFIN', 'ICICIBANK', 'JSWSTEEL', 'APOLLOTYRE', 'AMBUJACEM',
                  'HINDPETRO', 'TATAMOTORS', 'LICHSGFIN', 'DLF', 'SUNTV', 'SBIN', 'MCDOWELL-N', 'MARICO', 'BHARATFORG',
                  'AXISBANK', 'WIPRO', 'TVSMOTOR', 'IGL', 'ITC', 'CADILAHC', 'TATASTEEL', 'HINDALCO', 'TORNTPOWER',
                  'DABUR', 'CUMMINSIND', 'CONCOR', 'POWERGRID', 'SUNPHARMA', 'ICICIPRULI', 'UPL', 'BPCL', 'ADANIENT']

print(len(fno_stock_name))

# printing headers to csv
csv_header()

# printing stocks having gps
x = 0
while x <= 49:

    # getting stock quote
    time.sleep(1)
    nse = Nse()
    quote = nse.get_quote(fno_stock_name[x])

    # getting ohlc data
    day_open = quote['open']
    day_close = quote['closePrice']
    high = quote['dayHigh']
    low = quote['dayLow']

    # key pivots
    total_range = abs(high - low)
    cam_h4 = day_close + total_range * 1.1 / 2
    cam_h3 = day_close + total_range * 1.1 / 4
    pivot = (high + low + day_close) / 3
    r1_pivot = 2 * pivot - low
    bc_pivot = (high + low)/2
    tc_pivot = (pivot - bc_pivot) + pivot

    # checking for gps
    if tc_pivot > bc_pivot:
        if bc_pivot < cam_h3 < tc_pivot:
            print(fno_stock_name[x])

    elif tc_pivot < bc_pivot:
        if bc_pivot > cam_h3 > tc_pivot:
            print(fno_stock_name[x])

    # calculating dps
    if abs(r1_pivot - cam_h4) <= (day_close * 0.2) / 100:

        # stock name for list
        name = fno_stock_name[x]

        # percentage separation of that stock
        per_difference = (100 / day_open) * abs(r1_pivot - cam_h4)

        # Making a list combining both
        list_1 = [name, per_difference]

        # Printing it to dps_list.csv
        append_list_as_row('dps_list', list_1)

    x += 1
    time.sleep(5)

print('------------end------------')
print(time.time() - start_time)

# PRINTING DPS
# reading dps list
df = pd.read_csv('dps_list')

# sort by sep percentage
df_sorted = df.sort_values(by=['number'], ignore_index=True)

# printing scan results
print(df_sorted)

# clearing csv file
clear_csv()
