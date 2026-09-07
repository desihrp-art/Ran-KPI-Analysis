import pandas as pd
import os

# =========================
# 1. Load KPI data
# =========================

input_file = "data/sample_lte_kpi.csv"

df = pd.read_csv(input_file)

print("Data loaded successfully")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")

# =========================
# 2. Basic data cleaning
# =========================

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Remove duplicate records
df = df.drop_duplicates()

# =========================
# 3. KPI analysis
# =========================

# High PRB utilization
high_prb = df[df["PRB_Utilization"] >= 85]

# Low DL throughput
low_dl = df[df["DL_Throughput_Mbps"] < 10]

# Low CQI
low_cqi = df[df["CQI"] < 8]

# =========================
# 4. Summary
# =========================

print("\n=== KPI SUMMARY ===")

print(f"Average PRB Utilization: {df['PRB_Utilization'].mean():.2f}%")
print(f"Average DL Throughput: {df['DL_Throughput_Mbps'].mean():.2f} Mbps")
print(f"Average UL Throughput: {df['UL_Throughput_Mbps'].mean():.2f} Mbps")
print(f"Average CQI: {df['CQI'].mean():.2f}")
print(f"Average EUT: {df['EUT_Mbps'].mean():.2f} Mbps")
print(f"Average Availability: {df['Availability'].mean():.2f}%")

# =========================
# 5. Problematic cells
# =========================

print("\n=== HIGH PRB UTILIZATION ===")
print(high_prb[["Site", "Cell", "Band", "PRB_Utilization"]])

print("\n=== LOW DL THROUGHPUT ===")
print(low_dl[["Site", "Cell", "Band", "DL_Throughput_Mbps"]])

print("\n=== LOW CQI ===")
print(low_cqi[["Site", "Cell", "Band", "CQI"]])

# =========================
# 6. Export analysis results
# =========================

os.makedirs("output", exist_ok=True)

df.to_csv("output/cleaned_kpi.csv", index=False)
high_prb.to_csv("output/high_prb_cells.csv", index=False)
low_dl.to_csv("output/low_dl_cells.csv", index=False)
low_cqi.to_csv("output/low_cqi_cells.csv", index=False)

print("\nAnalysis completed successfully.")
print("Results saved in the output folder.")
