import openai

openai.api_key = "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"

response = openai.Image.create(
    prompt="a tiger in city",
    n=1,
    size="256x256"
)

image_url = response['data'][0]['url']

print(image_url)