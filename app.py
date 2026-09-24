import gradio as gr
from drainage_density_calculator import calculate_drainage_density

def compute(area, length):
    if area is None or length is None:
        return "Please enter both values.", ""
    if area <= 0 or length <= 0:
        return "Both values must be positive numbers greater than zero.", ""
    result = calculate_drainage_density(area, length)
    dd = result["drainage_density"]
    classification = result["classification"]
    color_map = {
        "Low drainage density (coarse texture)": "green",
        "Medium drainage density (moderate texture)": "orange",
        "High drainage density (fine texture)": "red"
    }
    color = color_map.get(classification, "black")
    dd_text = f"Drainage Density: {dd:.2f} km/km²"
    class_html = f"<p style='color:{color}; font-weight:bold;'>{classification}</p>"
    return dd_text, class_html

with gr.Blocks(title="Drainage Density Calculator", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Drainage Density Calculator")
    gr.Markdown("Enter the watershed area and total stream length to compute the drainage density (km/km²).")
    with gr.Row():
        area_input = gr.Number(label="Watershed Area (km²)", value=None, precision=2)
        length_input = gr.Number(label="Total Stream Length (km)", value=None, precision=2)
    calc_btn = gr.Button("Calculate Drainage Density")
    dd_output = gr.Textbox(label="Drainage Density", interactive=False)
    class_output = gr.HTML(label="Classification")
    calc_btn.click(fn=compute, inputs=[area_input, length_input], outputs=[dd_output, class_output])

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
