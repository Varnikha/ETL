import pandas as pd

# -------------------------
# EXTRACT
# -------------------------
def extract(path):
    print("Extracting data from:", path)
    return pd.read_csv(path)

# -------------------------
# TRANSFORM
# -------------------------
def transform(df):
    print("Initial shape:", df.shape)

    df_original = df.copy()

    # Validation BEFORE cleaning
    print("\nNull values BEFORE cleaning:")
    print(df.isnull().sum())

    print("\nDuplicate rows BEFORE:", df.duplicated().sum())

    # Handle missing values by dropping rows (simple approach)
    # Reason: Avoid incorrect training due to incomplete data
    df = df.dropna()

    # Standardize column names (improves consistency)
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    # Validation AFTER cleaning
    print("\nNull values AFTER cleaning:")
    print(df.isnull().sum())

    print("\nDuplicate rows AFTER:", df.duplicated().sum())

    
    # Row comparison
    print("\nRows before cleaning:", len(df_original))
    print("Rows after cleaning:", len(df))

    print("Final shape:", df.shape)

    return df

# -------------------------
# LOAD
# -------------------------
def load(df, output_path):
    df.to_csv(output_path, index=False)
    print("Cleaned data saved to:", output_path)

# -------------------------
# VALIDATE
# -------------------------
def validate(df):
    # Ensure dataset is not empty
    assert len(df) > 0, "Dataset is empty!"

    # Ensure no missing values remain
    assert df.isnull().sum().sum() == 0, "Null values found after cleaning!"

# -------------------------
# MAIN PIPELINE
# -------------------------
if __name__ == "__main__":
    raw_path = r"C:\Users\HP\Desktop\Intern\Python-based-ETL\data\raw\Housing.csv"
    output_path = r"C:\Users\HP\Desktop\Intern\Python-based-ETL\data\processed\clean_housing_data.csv"

    # Run ETL steps
    df = extract(raw_path)
    df_clean = transform(df)
    validate(df_clean)
    load(df_clean, output_path)

    print("\nETL pipeline executed successfully.")
