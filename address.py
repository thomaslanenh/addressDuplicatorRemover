import pandas as pd
import numpy as np


def run():
    df = pd.read_excel('./wrendata.xlsx')
    df2 = pd.read_excel('./wrenactivemembers.xls')

    df['Address'] = df['Address'].str.lower()
    df['City'] = df['City'].str.lower()

    df.sort_values(by=["Last name", "Address", "City",
                       "Email Address"], inplace=True)
    df.drop_duplicates(subset=["Address", "City"], keep="last", inplace=True)

    df = df.sort_values(by=["Last name"])
    df['Address'] = df['Address'].str.title()
    df['City'] = df['City'].str.title()

    df.to_excel(r'/Users/tlane/Desktop/filewithactivemembersincluded.xlsx',
                index=False, header=True)

    mergedData = pd.merge(df, df2, on=['Last name', 'Address'])

    print(mergedData)
    mergedData.to_excel(r'/Users/tlane/Desktop/activemembersmix.xlsx',
                        index=False, header=True)


if __name__ == '__main__':
    run()
