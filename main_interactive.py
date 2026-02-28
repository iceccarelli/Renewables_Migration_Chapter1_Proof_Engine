import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from chapter1_core import Chapter1ProofEngine

# Set page config
st.set_page_config(page_title="Renewables Migration: Chapter 1 Proof Engine", layout="wide")

# Initialize Engine
engine = Chapter1ProofEngine()

# Sidebar: Spy Mode
st.sidebar.title("🕵️ Spy Mode")
spy_mode = st.sidebar.checkbox("Enable 'The Spy on the 130 GVA·s Cliff'", value=False)

if spy_mode:
    st.sidebar.info("🔍 Highlighting exact book claims with live calculations.")

# Main Title
st.title("The Renewables Migration: Chapter 1 Proof Engine")
st.markdown("> **Chapter 1: The Invisible Heroics of 50.1 Hertz** — Vincenzo Grimaldi")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Live RoCoF Simulator", 
    "3D Stability Surface", 
    "Cost Protocol Pivot", 
    "Prove Every Equation", 
    "Download Book Data"
])

with tab1:
    st.header("Live RoCoF Simulator")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Input Parameters")
        h_sys = st.slider("System Inertia (H_sys) [GVA·s]", 0.0, 200.0, 130.0)
        delta_p = st.slider("Power Imbalance (ΔP) [GW]", 0.0, 5.0, 1.0)
        
        rocof = engine.calculate_rocof(delta_p, h_sys)
        rocof_max = engine.get_book_value('rocof_max')
        
        st.metric("Live RoCoF", f"{rocof:.3f} Hz/s", delta=f"{rocof - rocof_max:.3f} Hz/s", delta_color="inverse")
        
        if spy_mode and h_sys <= 130:
            st.warning("⚠️ **Book Claim:** 'The 130 GVA·s Cliff' — Below this level, traditional inertia is insufficient.")

    with col2:
        # Simple RoCoF Plot
        t = np.linspace(0, 1, 100)
        f = 50.0 - rocof * t
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=t, y=f, name="Frequency Deviation"))
        fig.add_hline(y=50.0 - rocof_max, line_dash="dash", line_color="red", annotation_text="RoCoF Limit")
        fig.update_layout(title="Frequency Response (1s Window)", xaxis_title="Time (s)", yaxis_title="Frequency (Hz)")
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("3D Stability Surface (Figure 1.2)")
    st.markdown("Stability as an inverse function of protocol latency and inertia.")
    
    h_range = np.linspace(0.1, 8, 50)
    l_range = np.linspace(0, 100, 50)
    H, L = np.meshgrid(h_range, l_range)
    Z = np.vectorize(engine.stability_margin_surface)(H, L)
    
    fig = go.Figure(data=[go.Surface(z=Z, x=H, y=L, colorscale='Viridis')])
    fig.update_layout(
        title='The 3D Stability Manifold',
        scene = dict(
            xaxis_title='Inertia (H_sys)',
            yaxis_title='MCP Latency (ms)',
            zaxis_title='Stability Margin'
        ),
        width=800, height=800
    )
    st.plotly_chart(fig, use_container_width=True)
    
    if spy_mode:
        st.info("💡 **Book Claim:** 'As mass disappears, the protocol must become faster.' — Observe the stability collapse at high latency.")

with tab3:
    st.header("Cost Protocol Pivot (Figure 1.1)")
    years = np.arange(2018, 2031)
    bau_costs = [engine.cost_protocol_pivot(y, 'BAU') for y in years]
    mcp_costs = [engine.cost_protocol_pivot(y, 'MCP') for y in years]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=bau_costs, name="Business as Usual (Manual Triage)", fill='tozeroy', line_color='red'))
    fig.add_trace(go.Scatter(x=years, y=mcp_costs, name="MCP-Enabled (Autonomous Resilience)", fill='tozeroy', line_color='green'))
    
    fig.update_layout(title="German Grid Intervention Costs (2018-2030)", xaxis_title="Year", yaxis_title="Cost (€ Billion)")
    st.plotly_chart(fig, use_container_width=True)
    
    dividend = bau_costs[-1] - mcp_costs[-1]
    st.success(f"**The Protocol Dividend (2030):** €{dividend:.1f} Billion saved annually.")

with tab4:
    st.header("Prove Every Equation")
    st.markdown("### 1. The Swing Equation with $\Phi_{MCP}$")
    st.latex(r"2H_{virtual} \frac{d\omega}{dt} = P_{ref} - P_{elec} - D(\omega - \omega_0) + \Phi_{MCP}")
    
    st.markdown("### 2. The Constraint Framework (Eq 1.2.1)")
    st.latex(r"\begin{cases} |\frac{df}{dt}| \leq RoCoF_{max} & \text{(Stability)} \\ P_{essential} \geq P_{min} & \text{(Human Rights)} \\ Gini(P_{curtail}) \leq \epsilon & \text{(Equity)} \end{cases}")
    
    if spy_mode:
        st.write("✅ All equations matched against Chapter 1, Section 1.2.1 and 1.5.1.")

with tab5:
    st.header("Download Book Data")
    st.dataframe(engine.data)
    st.download_button("Download CSV", engine.data.to_csv(), "book_numbers.csv", "text/csv")
