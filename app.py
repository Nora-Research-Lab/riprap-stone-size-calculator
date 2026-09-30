import gradio as gr
from riprap_stone_size_calculator import (
    calculate_d50,
    classify_d50,
    plot_d50_chart,
)

def compute(unit_system, velocity, slope_deg, rock_density, safety_factor):
    try:
        d50_m, d50_mm, d50_in = calculate_d50(unit_system, velocity, slope_deg, rock_density, safety_factor)
        classification = classify_d50(d50_mm)
        chart = plot_d50_chart(d50_mm)
        return f"{d50_mm:.1f}", f"{d50_in:.2f}", classification, chart
    except Exception as e:
        return "Error", "Error", f"Invalid input: {e}", None

with gr.Blocks(title="Riprap Stone Size Calculator") as demo:
    gr.Markdown("# Riprap Stone Size Calculator (Isbash Equation)")
    with gr.Row():
        with gr.Column():
            unit_system = gr.Radio(choices=["SI (m/s, kg/m³)", "Imperial (ft/s, lb/ft³)"],
                                   value="SI (m/s, kg/m³)", label="Unit System")
            velocity = gr.Number(value=3.0, label="Flow Velocity", minimum=0.5, maximum=10.0, step=0.1)
            slope = gr.Slider(minimum=0, maximum=60, value=30, label="Bank Slope Angle (degrees)", step=1)
            rock_density = gr.Number(value=2650, label="Rock Density", minimum=1000, maximum=5000, step=10)
            safety_factor = gr.Slider(minimum=1.0, maximum=2.0, value=1.2, label="Safety Factor", step=0.05)
            calc_btn = gr.Button("Calculate")
        with gr.Column():
            d50_mm_out = gr.Textbox(label="D50 (mm)")
            d50_in_out = gr.Textbox(label="D50 (inches)")
            classification_out = gr.Textbox(label="Classification")
            chart_out = gr.Plot(label="D50 vs Thresholds")
    calc_btn.click(
        fn=compute,
        inputs=[unit_system, velocity, slope, rock_density, safety_factor],
        outputs=[d50_mm_out, d50_in_out, classification_out, chart_out]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
