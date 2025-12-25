import csv
import matplotlib.pyplot as plt
from collections import defaultdict

# -------------------------------------------------------
# Load CSV data
# -------------------------------------------------------

data = defaultdict(list)

with open("performance_properties_results.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        enforcer = row["Enforcer"]
        props = int(row["Num_Properties"])
        time_val = float(row["Total_Time(s)"])
        data[enforcer].append((props, time_val))

# Sort by number of properties
for enf in data:
    data[enf] = sorted(data[enf], key=lambda x: x[0])

# -------------------------------------------------------
# Enforcer groups
# -------------------------------------------------------

groups = {
    "Strict Enforcers": [
        "Strict_Parallel"
    ],
    "Least Effort Enforcers": [
        "LE_Parallel"
    ],
    "Exclusive Enforcers": [
        "Exclusive_Parallel"
    ]
}

# -------------------------------------------------------
# Plot each group separately
# -------------------------------------------------------

for title, enforcer_list in groups.items():
    plt.figure()

    for enf in enforcer_list:
        if enf not in data:
            continue

        x = [p[0] for p in data[enf]]
        y = [p[1] for p in data[enf]]

        plt.plot(x, y, marker='o', linewidth=2, label=enf)

    plt.xlabel("Number of Properties")
    plt.ylabel("Total Time (seconds)")
    plt.title(f"{title} – Property Scaling")
    plt.legend()
    plt.grid(True)

    filename = title.lower().replace(" ", "_") + "_properties.png"
    plt.savefig(filename, bbox_inches="tight")
    plt.show()

    print(f"Saved {filename}")