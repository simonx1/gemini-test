from vertexai.preview.generative_models import GenerativeModel, Part

def generate():
  model = GenerativeModel("gemini-pro-vision")
  responses = model.generate_content(
    [image1, """What's in that photo? Provide deep analysis."""],
    generation_config={
        "max_output_tokens": 2048,
        "temperature": 0.4,
        "top_p": 1,
        "top_k": 32
    },
    )
  
  print(responses)


file_path = 'xray.jpeg'

with open(file_path, 'rb') as image_file:
    file_content = image_file.read()

image1 = Part.from_data(data=file_content, mime_type="image/jpeg")

generate()
