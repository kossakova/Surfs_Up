# Surfs Up

## Overview of the statistical analysis:

Beautiful Oahu, Hawaii. Friend of ours is planning to open A Surf n’ Shake shop serving surfboards and ice cream to locals. Before business plan comes analysis, analysis we passed the main factor for this business- the weather. We determine if location, weather, temperature, precipitation levels etc. is worth investments and business going to be successful. 

## Results:

Resources: SQLite, SQLalchemy, Python, Pandas, Flask

First, we retrieved data from flat SQLite file, then we put it into DataFrame to pursue our analysis. Our data had weather measurements of weather such as temperature and precipitation levels, records from 2016 from 9 different stations.

### Summary Statistics for June
Using Python function df.describe() we got compound information about temperature for a month of June. There were total amount of 1700 records of temperature for June. Average temperature is 74.9, while highest is 85 and minimal is 64, describe()  function also gave us records for std, 25%, 50% and 75%. 

![school_summary_after](https://github.com/kossakova/Surfs_Up/blob/main/PNG/June_Temps.png)

### Summary Statistics for December
Using Python function df.describe() we got compound information about temperature for a month of December. Overall average temperature for December is 71, while max is 83 and min is 56. 

![school_summary_after](https://github.com/kossakova/Surfs_Up/blob/main/PNG/December_Temps.png)

Going thru our analysis results we can address the three key differences in weather between June and December:
- Overall average temperature does not defer a lot its 74.9 in June versus 71 in December.
- Maximum temperature of 85 in June did not have much of a excellence comparing to Decembers 83.
- Biggest distinction was for minimum temperature June 64 and December 56. 

## Summary:
Aloha! Our analysis looks great! Weather in Oahu suits perfect for surfing and ice cream shop. Our work provided in depth analysis that will be very helpful and useful if our friend will decide to open another shop in the future! But that’s no all, we can also parse precipitation levels to gather more weather data for June and December.

results = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date)==6).all()
df = pd.DataFrame(results, columns=['date','precipitation'])
df.set_index(df['date'], inplace=True)
df.describe()

results = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date)==12).all()
df = pd.DataFrame(results, columns=['date','precipitation'])
df.set_index(df['date'], inplace=True)
df.describe()
