import pandas as pd

# load the dataset
df = pd.read_csv("/Users/macbookpro/Desktop/LinkedIn Work/LinkedIn Posts/Crude Oil Production by Country/Crude Oil Production by Country.csv")

# drop the Flag column
df.drop("Flag", axis=1, inplace=True)

# transpose the dataframe
df = df.set_index("Country").T.reset_index()

# drop all columns with zeros
df = df.loc[:, (df != 0).any(axis=0)]

# drop the last 5 columns
df = df.iloc[:, :-5]

# set the index column to a datetime column
df["index"] = pd.to_datetime(df["index"])

# set the index column as the dataframe's index
df.set_index("index", inplace=True)

# save the pre-processed dataframe as a CSV file
df.to_csv("/Users/macbookpro/Desktop/LinkedIn Work/LinkedIn Posts/Crude Oil Production by Country/Crude Oil Production by Country Pre-processed.csv")
