import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part

def generate():
  model = GenerativeModel("gemini-pro-vision")
  responses = model.generate_content(
    """"That lawyer is my brother" testified the accountant. But the lawyer testified he didn't have a brother. Who is lying?""",
    generation_config={
        "max_output_tokens": 2048,
        "temperature": 0.4,
        "top_p": 1,
        "top_k": 32
    },
    )
  
  print(responses)


generate()

