import csv
import matplotlib.pyplot as plt
from collections import defaultdict

# ==============================
# Global matplotlib styling
# ==============================

plt.rcParams.update({
    "figure.figsize": (9, 5.5),
    "figure.dpi": 150,

    "font.size": 12,
    "axes.labelsize": 14,
    "axes.titlesize": 15,
    "xtick.labelsize": 13,
    "ytick.labelsize": 13,
    "legend.fontsize": 13,

    "lines.linewidth": 2,
    "lines.markersize": 6,
})

# ==============================
# Read CSV
# ==============================

data = defaultdict(list)

with open("performance_properties_new.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        enforcer = row["Enforcer"].strip()
        num_props = int(row["Num_Properties"])
        time_us = float(row["Total_Time (microseconds)"])
        data[enforcer].append((num_props, time_us))

# Sort by number of properties
for k in data:
    data[k] = sorted(data[k], key=lambda x: x[0])

# ==============================
# Enforcer groups
# ==============================

groups = {
    "Strict Enforcers": [
        "Strict_Monolithic",
        "Strict_Serial",
        "Strict_Parallel"
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

# ==============================
# Style rules
# ==============================

STYLE_MONOLITHIC = dict(color="green", linestyle="-", marker="o")
STYLE_PARALLEL   = dict(color="orange", linestyle="-", marker="o")
STYLE_SERIAL     = dict(color="skyblue", linestyle="-", marker="o")

def style_for(enforcer_name):
    if "Monolithic" in enforcer_name:
        return STYLE_MONOLITHIC
    if "Parallel" in enforcer_name:
        return STYLE_PARALLEL
    if "Serial" in enforcer_name:
        return STYLE_SERIAL
    return {}

# ==============================
# Plotting
# ==============================

for title, enforcer_list in groups.items():

    plt.figure(constrained_layout=True)
    plotted = False

    for enf in enforcer_list:
        if enf not in data or not data[enf]:
            print(f"WARNING: No data for {enf}")
            continue

        if title == "Strict Enforcers":
            filtered = [(p, t) for p, t in data[enf] if p >= 3]
        else:
            filtered = data[enf]

        if not filtered:
            continue

        x = [p for p, _ in filtered]
        y = [t for _, t in filtered]

        plt.plot(x, y, label=enf, **style_for(enf))
        plotted = True

    if plotted:
        plt.xlabel("Number of Properties")
        plt.ylabel("Total Time (microseconds)")
        plt.title(title)
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.legend()

        filename = title.lower().replace(" ", "_") + "_new.png"
        plt.savefig(filename)
        plt.show()
        print(f"Saved {filename}")
    else:
        plt.close()
