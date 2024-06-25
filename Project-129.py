import pandas as pd

def Remove_NaNs(input_filename, output_filename):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_filename)
    
    # Print the original DataFrame
    print("Original DataFrame:")
    print(df)
    
    # Remove rows with any NaN values
    df_cleaned = df.dropna()

    df_cleaned["radius"] = df_cleaned["radius"].astype(float)
    df_cleaned["mass"] = df_cleaned["mass"].astype(float)

    df_cleaned["radius"] *= 0.102763
    df_cleaned["mass"] *= 0.000954588
    
    
    # Print the cleaned DataFrame
    print("\nCleaned DataFrame (with NaNs removed):")
    print(df_cleaned)
    
    # Save the cleaned DataFrame to a new CSV file
    df_cleaned.to_csv(output_filename, index=True)


if __name__ == "__main__":
    input_filename = 'C-128Web_Scrapping2.csv'  # Replace with your input file name
    output_filename = 'C-129Data_Merging.csv'   # Replace with your desired output file name
    Remove_NaNs(input_filename, output_filename)