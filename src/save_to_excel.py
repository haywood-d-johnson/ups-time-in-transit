import pandas as pd

def save_results_to_excel(data_list, filename="../data/ups_transit_times.xlsx"):
    """Save transit time results to an Excel file."""
    df = pd.DataFrame(data_list)
    df.to_excel(filename, index=False)
    print(f"Saved results to {filename}")
