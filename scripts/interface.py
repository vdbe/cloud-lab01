import gradio as gr
import numpy as np

from fastai.learner import load_learner

learn1 = load_learner(fname="./models/fastai-resnet34.pkl", cpu=True)

def predict(ndarray):
    if not isinstance(ndarray, (np.ndarray)):
        return ""

    prediction = learn1.predict(ndarray)

    label = prediction[0]
    return chr(label + 64)

interface = gr.Interface(
    fn=predict,
    inputs=gr.Paint(tool="sketch", type="numpy", shape=(28,28), invert_colors=True, image_mode="L"),
    outputs="text",
    live=True,
)

interface.launch(server_name="0.0.0.0")