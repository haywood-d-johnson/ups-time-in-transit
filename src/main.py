import json
from transit_time import get_transit_time
from save_to_excel import save_results_to_excel

ORIGIN_ZIP = "76226"
DEST_ZIP_FILE = "../data/destination_zips.json"

def load_zip_codes():
    """Load destination ZIP codes from JSON file."""
    with open(DEST_ZIP_FILE, "r") as file:
        return json.load(file)

def main():
    """Main function to fetch transit times and save results."""
    destination_zips = load_zip_codes()
    data_list = []

    for zip_code in destination_zips:
        transit_data = get_transit_time(ORIGIN_ZIP, zip_code)
        if transit_data and "ServiceSummary" in transit_data:
            for service in transit_data["ServiceSummary"]:
                data_list.append({
                    "Destination ZIP": zip_code,
                    "Service": service["Service"]["Description"],
                    "Estimated Days": service["EstimatedArrival"]["BusinessTransitDays"]
                })

    save_results_to_excel(data_list)

if __name__ == "__main__":
    main()
