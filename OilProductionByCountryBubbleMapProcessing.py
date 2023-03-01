import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# load preprocessed dataset and parse index as date column
df = pd.read_csv("/Users/macbookpro/Desktop/LinkedIn Work/LinkedIn Posts/Crude Oil Production by Country/Crude Oil Production by Country Pre-processed.csv", index_col=0, parse_dates=True)

# create a new dataframe for storing the top  producers per year
top_producers = pd.DataFrame(columns=['Year', 'Country', 'Production'])

# iterate over each year and select the top producers
for year in df.index.year.unique():
    df_year = df.loc[df.index.year == year]
    df_year = df_year.apply(pd.to_numeric, errors='coerce') # convert to numeric data type
    top_producers_year = df_year.sum().nlargest(20)
    top_producers_year = pd.DataFrame(top_producers_year)
    top_producers_year.columns = ['Production']
    top_producers_year['Country'] = top_producers_year.index
    top_producers_year['Year'] = year
    top_producers_year = top_producers_year[['Year', 'Country', 'Production']]
    top_producers = top_producers.append(top_producers_year)

# save the top 10 producers to a csv file
top_producers.to_csv("/Users/macbookpro/Desktop/LinkedIn Work/LinkedIn Posts/Crude Oil Production by Country/TopProducersPerYear.csv", index=False)

print(top_producers.head(20))