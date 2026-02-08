import pandas as pd

input_path = "data/raw/NTD_2022_Public_Transit.csv"
df = pd.read_csv(input_path)

# Standardization of the column names after a cursory review of the CSV file
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace("/", "_")
      .str.replace(" ", "_")
      .str.replace(r"[()]", "", regex=True)
)

# Identify numeric service fields
numeric_fields = [
    "agency_voms",
    "primary_uza_area_sq_miles",
    "primary_uza_population",
    "service_area_sq_miles",
    "service_area_population",
    "actual_vehicle_passenger_car_miles",
    "actual_vehicle_passenger_car_revenue_miles",
    "actual_vehicle_passenger_car_deadhead_miles",
    "scheduled_vehicle_passenger_car_revenue_miles",
    "actual_vehicle_passenger_car_hours",
    "actual_vehicle_passenger_car_revenue_hours",
    "actual_vehicle_passenger_car_deadhead_hours",
    "charter_service_hours",
    "school_bus_hours",
    "trains_in_operation",
    "train_miles",
    "train_revenue_miles",
    "train_deadhead_miles",
    "train_hours",
    "train_revenue_hours",
    "train_deadhead_hours",
    "unlinked_passenger_trips_upt",
    "ada_upt",
    "sponsored_service_upt",
    "passenger_miles_traveled",
    "directional_route_miles"
]

# Remove commas and convert to numeric
for col in numeric_fields:
    if col in df.columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(",", "", regex=False)
            .replace("nan", None)
            .astype(float)
        )


# Basic data validation: drop records missing critical identifiers
df = df.dropna(subset=["agency", "state", "report_year"])

# Ensure report year is numeric and reasonable
df["report_year"] = df["report_year"].astype(int)
df = df[df["report_year"].between(2022, 2024)]

# Log negative service values; Did not remove them to preserve data and integrity
for col in numeric_fields:
    if col in df.columns:
        negative_count = (df[col] < 0).sum()
        if negative_count > 0:
            print(f"{col}: {negative_count} negative values detected")


# Sort for reporting consistency
df = df.sort_values(
    by=["state", "agency", "report_year"]
)

# Data Quality Summary: Total missing values in each numeric column
print("\nData Quality Summary:")
print(f"Total records after cleaning: {len(df)}\n")

for i, col in enumerate(numeric_fields):
    if col in df.columns:
        missing = df[col].isna().sum()
        if missing > 0:
            print(f"{i}. {col}: {missing} missing values")

# Export cleaned dataset
output_path = "data/processed/ntd_2022_public_transit_clean.csv"
df.to_csv(output_path, index=False)

print(f"\nCleaned NTD service dataset saved with {len(df)} records.")
