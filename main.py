import pandas as pd
import pandas_profiling as pp

df = pd.read_csv('cars_engage_2022.csv')
print(df)

profile = pp.ProfileReport(df, minimal=True)

# Creating Minimal Profiling of .csv sheet into .html file
profile.to_file(output_file="cars_engage_2022.html")
