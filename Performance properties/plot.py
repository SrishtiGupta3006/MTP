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
# Plot: Property Scaling Comparison
# -------------------------------------------------------

plt.figure(figsize=(7, 5))

plot_order = [
    "LE_Parallel",
    "Strict_Parallel",
    "Exclusive_Parallel"
]

for enf in plot_order:
    if enf not in data:
        continue

    x = [p for p, _ in data[enf]]
    y = [t for _, t in data[enf]]

    plt.plot(x, y, marker='o', linewidth=2, label=enf)

plt.xlabel("Number of Properties")
plt.ylabel("Total Time (seconds)")
plt.title("Property-Scaling Performance (Parallel Enforcers)")
plt.legend()
plt.grid(True)

plt.savefig("property_scaling_parallel_enforcers.png", bbox_inches="tight")
plt.show()

print("Saved property_scaling_parallel_enforcers.png")
