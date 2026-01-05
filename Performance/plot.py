import csv
import matplotlib.pyplot as plt
from collections import defaultdict

# Global matplotlib styling

plt.rcParams.update({
    "figure.figsize": (8, 5),
    "figure.dpi": 150,
    "font.size": 11,
    "axes.labelsize": 12,
    "axes.titlesize": 13,
    "legend.fontsize": 10,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "lines.linewidth": 2,
    "lines.markersize": 6,
})

# Read CSV

data = defaultdict(list)

with open("performance_results.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        enforcer = row["Enforcer"]
        size = int(row["Input Size"])
        time_val = float(row["Total Time (s)"])
        data[enforcer].append((size, time_val))

for k in data:
    data[k] = sorted(data[k], key=lambda x: x[0])

# Enforcer groups

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

# Style rules

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

# Plotting

for title, enforcer_list in groups.items():

    # ==============================
    # STRICT ENFORCERS → TWO PLOTS
    # ==============================
    if title == "Strict Enforcers":

        # -------- Zoomed view --------
        plt.figure()
        for enf in enforcer_list:
            x = [p[0] for p in data[enf]]
            y = [p[1] for p in data[enf]]
            plt.plot(x, y, label=enf, **style_for(enf))

        plt.xlabel("Input Size (Number of Events)")
        plt.ylabel("Total Time (seconds)")
        plt.title("Strict Enforcers")

        plt.ylim(-0.1, 0.5)
        plt.yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5])

        plt.grid(True, linestyle="--", alpha=0.6)
        plt.legend()
        plt.tight_layout()
        plt.savefig("strict_enforcers.png")
        plt.show()

    # ==============================
    # DEFAULT PLOTTING
    # ==============================
    plt.figure()
    for enf in enforcer_list:
        x = [p[0] for p in data[enf]]
        y = [p[1] for p in data[enf]]
        plt.plot(x, y, label=enf, **style_for(enf))

    plt.xlabel("Input Size (Number of Events)")
    plt.ylabel("Total Time (seconds)")
    plt.title(title)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()

    filename = title.lower().replace(" ", "_") + ".png"
    plt.savefig(filename)
    plt.show()

    print(f"Saved {filename}")
