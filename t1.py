import pandas as pd


def clean(input_file1, input_file2,output):
    df1 = pd.read_csv(input_file1)
    df2 = pd.read_csv(input_file2)
    df3 = df1.merge(df2,left_on="respondent_id",right_on="id")
    df4 = df3.dropna()
    df5 = df4[~df4["job"].str.contains('insurance|Insurance')]
    df6 = df5.drop(columns="id")
    return df6.to_csv(output, index=False)


#clean("respondent_contact.csv","respondent_other.csv","respondent_cleaned.csv")
clean(input_file1, input_file2,output)