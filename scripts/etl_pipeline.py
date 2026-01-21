import pandas as pd

def extract(path):
    return pd.read_csv(path)

def transform(df):
    # Handle missing values
    df = df.dropna()

    # Example transformation
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    return df

def load(df, output_path):
    df.to_csv(output_path, index=False)

def validate(df):
    assert df.isnull().sum().sum() == 0, "Null values found!"
    assert len(df) > 0, "Dataset is empty!"

if __name__ == "__main__":
    raw_path = r"C:\Users\HP\Desktop\Intern\Python-based-ETL\Housing.csv"
    output_path = r"C:\Users\HP\Desktop\Intern\Python-based-ETL\clean_housing_data.csv"

    df = extract(raw_path)
    df_clean = transform(df)
    validate(df_clean)
    load(df_clean, output_path)

    print("ETL pipeline executed successfully.")
