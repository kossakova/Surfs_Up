# Surfs Up

## Overview of the statistical analysis:

Aloha! Welcome to Beautiful Oahu, Hawaii. A friend of ours is planning to open a **Surf n’ Shake** shop serving surfboards and ice cream to locals. Before the business plan comes the analysis, and the main factor for this business- the weather. We determined if location, weather, temperature, precipitation levels etc. are worth investments and if the business is going to be successful. 

## Results:

***Resources: SQLite, SQLAlchemy, Python, Pandas, Flask***

First, we retrieved data from a flat SQLite file, then we put it into DataFrame to pursue our analysis. Our data had weather measurements such as temperature and precipitation levels, and included records from 2016 from 9 different stations.

### Summary Statistics for June
Using Python function df.describe() we got compound information about temperature for the month of June. There were total amount of 1700 records of temperature for June. The average temperature is 74.9°F, while the highest is 85°F and the minimum is 64°F. Our df.describe()  function also gave us records for std, 25%, 50% and 75%. 

![school_summary_after](https://github.com/kossakova/Surfs_Up/blob/main/PNG/June_Temps.png)

### Summary Statistics for December
Using the Python function df.describe() we got compound information about temperature for the month of December. Overall average temperature for December is 71°F, while max is 83°F and min is 56°F. 

![school_summary_after](https://github.com/kossakova/Surfs_Up/blob/main/PNG/December_Temps.png)

Going through our analysis results we can address the three key differences in weather between June and December:
- Overall average temperature does not differ a lot; it's 74.9°F in June versus 71°F in December.
- Maximum temperature of 85°F in June did not have much of a difference comparing to Decembers 83°F.
- The biggest difference was for minimum temperature June 64°F and December 56°F. 

## Summary:
***Aloha!*** Our analysis looks great! Weather in Oahu perfectly suits our surfing & ice cream shop. Our work provided an depth analysis that will be very helpful and useful if our friend will decide to open another shop in the future! But that’s not all, we can also parse precipitation levels to gather more weather data for June and December.
```
results = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date)==6).all()
df = pd.DataFrame(results, columns=['date','precipitation'])
df.set_index(df['date'], inplace=True)
df.describe()
```
```
results = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date)==12).all()
df = pd.DataFrame(results, columns=['date','precipitation'])
df.set_index(df['date'], inplace=True)
df.describe()
```
