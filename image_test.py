import argparse
from vertexai.preview.generative_models import GenerativeModel, Part

def generate(file_path):
    with open(file_path, 'rb') as image_file:
        file_content = image_file.read()

    image1 = Part.from_data(data=file_content, mime_type="image/jpeg")

    model = GenerativeModel("gemini-pro-vision")
    responses = model.generate_content(
        [image1, """What is in this photo? Provide as many details as you can."""],
        generation_config={
            "max_output_tokens": 2048,
            "temperature": 0.4,
            "top_p": 1,
            "top_k": 32
        },
    )
  
    print(responses)

def main():
    parser = argparse.ArgumentParser(description='Process image file for content generation.')
    parser.add_argument('file_path', type=str, help='Path to the image file')
    args = parser.parse_args()
    generate(args.file_path)

if __name__ == '__main__':
    main()
