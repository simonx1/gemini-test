import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part

def multiturn_generate_content():
    config = {
        "max_output_tokens": 8192,
        "temperature": 0.2,
        "top_p": 1
    }
    model = GenerativeModel("gemini-pro")
    chat = model.start_chat()
    print(chat.send_message(""""That lawyer is my brother" testified the accountant. But the lawyer testified he didn't have a brother. Who is lying?""", generation_config=config))




multiturn_generate_content()

