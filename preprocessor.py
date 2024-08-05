import pandas as pd


df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

def preprocess():
    global df,region_df

    #filtering for summer olympics
    df = df[df['Season'] == 'Summer']

    #merge with region_df
    df = df.merge(region_df, on='NOC', how='left')

    #dropping duplicates
    df.drop_duplicates(inplace=True)

    #one hot encoding medals(convert just medal to categorical too)
    df1 = pd.get_dummies(df['Medal']).astype(int)
    df = pd.concat([df, df1], axis=1)

    return df
