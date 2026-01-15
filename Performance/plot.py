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

with open("performance_results_avg_opt.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        enforcer = row["Enforcer"].strip()
        size = int(row["Input Size"])
        time_val = float(row["Average Time (s)"])
        data[enforcer].append((size, time_val))

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

    # -------- STRICT ZOOMED VIEW --------
    if title == "Strict Enforcers":
        plt.figure(constrained_layout=True)

        plotted = False
        for enf in enforcer_list:
            if enf not in data or not data[enf]:
                print(f"WARNING: No data for {enf}")
                continue

            x = [p[0] for p in data[enf]]
            y = [p[1] for p in data[enf]]
            plt.plot(x, y, label=enf, **style_for(enf))
            plotted = True

        if plotted:
            plt.xlabel("Input Size (Number of Events)")
            plt.ylabel("Total Time (seconds)")
            plt.title("Strict Enforcers")

            plt.ylim(-0.1, 0.5)
            plt.yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5])

            plt.grid(True, linestyle="--", alpha=0.6)
            plt.legend()
            plt.savefig("strict_enforcers_1_avg_opt.png")
            plt.show()
        else:
            plt.close()

    # -------- DEFAULT VIEW --------
    plt.figure(constrained_layout=True)

    plotted = False
    for enf in enforcer_list:
        if enf not in data or not data[enf]:
            print(f"WARNING: No data for {enf}")
            continue

        x = [p[0] for p in data[enf]]
        y = [p[1] for p in data[enf]]
        plt.plot(x, y, label=enf, **style_for(enf))
        plotted = True

    if plotted:
        plt.xlabel("Input Size (Number of Events)")
        plt.ylabel("Total Time (seconds)")
        plt.title(title)
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.legend()

        filename = title.lower().replace(" ", "_") + "_avg_opt.png"
        plt.savefig(filename)
        plt.show()
        print(f"Saved {filename}")
    else:
        plt.close()
