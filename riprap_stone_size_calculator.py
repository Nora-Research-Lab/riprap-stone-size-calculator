import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

WATER_DENSITY_SI = 1000.0  # kg/m³
WATER_DENSITY_IMP = 62.4   # lb/ft³
G_SI = 9.81   # m/s²
G_IMP = 32.174  # ft/s²

def calculate_d50(unit_system: str, velocity: float, slope_deg: float,
                  rock_density: float, safety_factor: float):
    """
    Returns (d50_m, d50_mm, d50_in) using Isbash equation.
    unit_system: "SI (m/s, kg/m³)" or "Imperial (ft/s, lb/ft³)"
    """
    if unit_system.startswith("SI"):
        g = G_SI
        water_density = WATER_DENSITY_SI
    else:
        g = G_IMP
        water_density = WATER_DENSITY_IMP

    slope_rad = math.radians(slope_deg)
    cos_theta = math.cos(slope_rad)
    if cos_theta == 0:
        raise ValueError("Slope angle cannot be 90° (cosine zero).")
    sr = rock_density / water_density  # specific gravity
    if sr <= 1.0:
        raise ValueError("Rock density must be greater than water density.")
    d50_m = (velocity**2 * safety_factor) / (2 * g * (sr - 1) * cos_theta)
    if d50_m < 0:
        raise ValueError("Computed D50 negative – check inputs.")
    d50_mm = d50_m * 1000.0
    d50_in = d50_m / 0.0254
    return d50_m, d50_mm, d50_in

def classify_d50(d50_mm: float) -> str:
    if d50_mm < 150:
        return "Small riprap (fine gravel)"
    elif d50_mm <= 300:
        return "Medium riprap"
    elif d50_mm <= 500:
        return "Large riprap"
    else:
        return "Very large riprap (boulders)"

def plot_d50_chart(d50_mm: float):
    """Return a matplotlib figure: bar chart of d50 vs thresholds."""
    thresholds = [150, 300, 500]
    labels = ["Threshold 150 mm", "Threshold 300 mm", "Threshold 500 mm"]
    values = [d50_mm] * 3

    fig, ax = plt.subplots(figsize=(6, 4))
    x = np.arange(len(thresholds))
    width = 0.35

    # Bars for threshold lines (static, at threshold values)
    ax.bar(x - width/2, thresholds, width, label="Thresholds", color="gray", alpha=0.5)

    # Bars for computed D50 (colored green/based on threshold crossing)
    colors = []
    for th in thresholds:
        colors.append("green" if d50_mm <= th else "red")
    ax.bar(x + width/2, values, width, label="Computed D50", color=colors)

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("D50 (mm)")
    ax.set_title("D50 vs Classification Thresholds")
    ax.legend(loc="upper left")
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    fig.tight_layout()
    return fig
