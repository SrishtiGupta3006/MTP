import csv
import matplotlib.pyplot as plt
from collections import defaultdict

data = defaultdict(list)

with open("scaling_results.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        enforcer = row["Enforcer"]
        size = int(row["Input Size"])
        time_val = float(row["Total Time (s)"])
        data[enforcer].append((size, time_val))

# Sort data by input size
for k in data:
    data[k] = sorted(data[k], key=lambda x: x[0])

# Enforcer groups

groups = {
    "Strict Enforcers": [
        "Strict_Monolithic",
        "Strict_Serial"
    ],
    "Least Effort Enforcers": [
        "LE_Monolithic",
        "LE_Parallel"
    ],
    "Exclusive Enforcers": [
        "Exclusive_Monolithic",
        "Exclusive_Parallel"
    ]
}

# Plotting each group separately

for title, enforcer_list in groups.items():
    plt.figure()

    for enf in enforcer_list:
        if enf not in data:
            continue

        x = [p[0] for p in data[enf]]
        y = [p[1] for p in data[enf]]

        plt.plot(x, y, marker='o', label=enf)

    plt.xlabel("Input Size")
    plt.ylabel("Total Time (seconds)")
    plt.title(title)
    plt.legend()
    plt.grid(True)

    # Save figure
    filename = title.lower().replace(" ", "_") + ".png"
    plt.savefig(filename)
    plt.show()

    print(f"Saved {filename}")
