import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import sys

# Add parent directory to path to import chapter1_core
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from chapter1_core import Chapter1ProofEngine

def generate_plots():
    engine = Chapter1ProofEngine(data_path='data/book_numbers.csv')
    os.makedirs('plots', exist_ok=True)

    # 1. Stability Surface 3D (Figure 1.2)
    h_range = np.linspace(0.1, 8, 50)
    l_range = np.linspace(0, 100, 50)
    H, L = np.meshgrid(h_range, l_range)
    Z = np.vectorize(engine.stability_margin_surface)(H, L)

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(H, L, Z, cmap='viridis', edgecolor='none')
    ax.set_xlabel('Inertia (H_sys)')
    ax.set_ylabel('MCP Latency (ms)')
    ax.set_zlabel('Stability Margin')
    ax.set_title('Figure 1.2: The 3D Stability Manifold')
    plt.savefig('plots/stability_surface_3d.png', dpi=300)
    plt.close()

    # 2. Protocol Pivot Costs (Figure 1.1)
    years = np.arange(2018, 2031)
    bau_costs = [engine.cost_protocol_pivot(y, 'BAU') for y in years]
    mcp_costs = [engine.cost_protocol_pivot(y, 'MCP') for y in years]

    plt.figure(figsize=(10, 6))
    plt.fill_between(years, bau_costs, color='red', alpha=0.3, label='Business as Usual (Manual Triage)')
    plt.plot(years, bau_costs, color='red', linewidth=2)
    plt.fill_between(years, mcp_costs, color='green', alpha=0.3, label='MCP-Enabled (Autonomous Resilience)')
    plt.plot(years, mcp_costs, color='green', linewidth=2)
    plt.xlabel('Year')
    plt.ylabel('Cost (€ Billion)')
    plt.title('Figure 1.1: Projected Grid Intervention Costs')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('plots/protocol_pivot_costs.png', dpi=300)
    plt.close()

    # 3. RoCoF Sensitivity
    h_sys_range = np.linspace(50, 200, 100)
    rocof_vals = [engine.calculate_rocof(1.0, h) for h in h_sys_range]
    
    plt.figure(figsize=(10, 6))
    plt.plot(h_sys_range, rocof_vals, color='blue', linewidth=2)
    plt.axvline(x=130, color='red', linestyle='--', label='The 130 GVA·s Cliff')
    plt.xlabel('System Inertia (H_sys) [GVA·s]')
    plt.ylabel('RoCoF [Hz/s]')
    plt.title('RoCoF Sensitivity to Inertia (ΔP = 1 GW)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('plots/rocoF_sensitivity.png', dpi=300)
    plt.close()

    print("All book figures generated in 'plots/' directory.")

if __name__ == "__main__":
    generate_plots()
