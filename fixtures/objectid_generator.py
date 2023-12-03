from datetime import datetime

from bson.objectid import ObjectId

dates = [
    [2010, 1, 1],
    [2011, 1, 1],
    [2012, 1, 1],
    [2013, 1, 1],
    [2014, 1, 1],
    [2015, 1, 1],
    [2016, 1, 1],
    [2017, 1, 1],
    [2018, 1, 1],
    [2019, 1, 1],
    [2020, 1, 1],
]

for date in dates:
    # 4b3d3b000000000000000000
    gen_time = datetime(date[0], date[1], date[2])
    print(ObjectId.from_datetime(gen_time))
