"""100 Meters""" # this code is also fcking dirty
time1 = float(input())
time2 = float(input())
time3 = float(input())
time4 = float(input())
time5 = float(input())
time6 = float(input())
time7 = float(input())
time8 = float(input())

# find gold medal
GOLD = 1
gold_time = time1

if time2 < gold_time:
    GOLD = 2
    gold_time = time2
if time3 < gold_time:
    GOLD = 3
    gold_time = time3
if time4 < gold_time:
    GOLD = 4
    gold_time = time4
if time5 < gold_time:
    GOLD = 5
    gold_time = time5
if time6 < gold_time:
    GOLD = 6
    gold_time = time6
if time7 < gold_time:
    GOLD = 7
    gold_time = time7
if time8 < gold_time:
    GOLD = 8
    gold_time = time8

# find sliver medal
SLIVER = 0
silver_time = float('inf')

if GOLD != 1 and time1 < silver_time:
    SLIVER = 1
    silver_time = time1
if GOLD != 2 and time2 < silver_time:
    SLIVER = 2
    silver_time = time2
if GOLD != 3 and time3 < silver_time:
    SLIVER = 3
    silver_time = time3
if GOLD != 4 and time4 < silver_time:
    SLIVER = 4
    silver_time = time4
if GOLD != 5 and time5 < silver_time:
    SLIVER = 5
    silver_time = time5
if GOLD != 6 and time6 < silver_time:
    SLIVER = 6
    silver_time = time6
if GOLD != 7 and time7 < silver_time:
    SLIVER = 7
    silver_time = time7
if GOLD != 8 and time8 < silver_time:
    SLIVER = 8
    silver_time = time8

# find bronze medal
BRONZE = 0
bronze_time = float('inf')

if GOLD != 1 and SLIVER != 1 and time1 < bronze_time:
    BRONZE = 1
    bronze_time = time1
if GOLD != 2 and SLIVER != 2 and time2 < bronze_time:
    BRONZE = 2
    bronze_time = time2
if GOLD != 3 and SLIVER != 3 and time3 < bronze_time:
    BRONZE = 3
    bronze_time = time3
if GOLD != 4 and SLIVER != 4 and time4 < bronze_time:
    BRONZE = 4
    bronze_time = time4
if GOLD != 5 and SLIVER != 5 and time5 < bronze_time:
    BRONZE = 5
    bronze_time = time5
if GOLD != 6 and SLIVER != 6 and time6 < bronze_time:
    BRONZE = 6
    bronze_time = time6
if GOLD != 7 and SLIVER != 7 and time7 < bronze_time:
    BRONZE = 7
    bronze_time = time7
if GOLD != 8 and SLIVER != 8 and time8 < bronze_time:
    BRONZE = 8
    bronze_time = time8
print(GOLD, SLIVER, BRONZE)
