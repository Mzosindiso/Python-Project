import pandas as pd

def load_data(file_path):
    # Try different encodings
    encodings = ['utf-8', 'ISO-8859-1', 'latin1', 'cp1252']
    
    for encoding in encodings:
        try:
            return pd.read_csv(file_path, encoding=encoding)
        except UnicodeDecodeError:
            continue
    
    # If none of the encodings work, raise an error
    raise ValueError(f"Unable to read the file with any of the following encodings: {encodings}")

def clean_data(df):
    # Your existing clean_data function
    return df

def save_cleaned_data(df, output_path):
    df.to_csv(output_path, index=False)