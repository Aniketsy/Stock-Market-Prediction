def load_data(file_path):
    import pandas as pd
    """Load stock data from a CSV file."""
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    """Clean the stock data by handling missing values."""
    # Fill missing values with the mean of the column
    cleaned_data = data.fillna(data.mean())
    return cleaned_data