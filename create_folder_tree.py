import os
import csv

ASSETS_ROOT = "design_brand_plan_assets_logos"
CSV_FILE = "logotype_combinations_matrix_all.csv"

with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    print("CSV Columns:", reader.fieldnames)

    for row in reader:
        lockup_type = row['\ufeffLockup Type'].strip()  # fixed BOM column name
        layout = row['Layout'].strip()
        style = row['Style'].strip()
        file_name = row['File Name'].strip().replace('.svg', '').replace('.png', '').replace('.pdf', '')

        folder_path = os.path.join(ASSETS_ROOT, lockup_type, layout, style, file_name)
        os.makedirs(folder_path, exist_ok=True)

print(f"✅ Folder tree created in: {ASSETS_ROOT}")
