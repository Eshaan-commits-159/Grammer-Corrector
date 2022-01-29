# importing all vital libraries
from logging import PlaceHolder
from happytransformer import TTSettings
from happytransformer import HappyTextToText
import gradio as gr


# ------------------------------------------------

# defining an object using HappyTextToText class
happy_tt = HappyTextToText("T5", "prithivida/grammar_error_correcter_v1")
top_k_sampling_settings = TTSettings(
    do_sample=True, top_k=50, temperature=0.7, min_length=1, max_length=50)

# defining input that is our textbox
app_inputs = gr.inputs.Textbox(lines=2, placeholder="Enter a sentence")

# defining grammar correction function


def correct(sentence):
    result = happy_tt.generate_text(sentence, args=top_k_sampling_settings)
    return result.text


# defining interface
interface = gr.Interface(fn=correct, inputs=app_inputs,
                         outputs='text', title='correct your sentence\'s grammar here')

# launching our interface
interface.launch()
