import requests

def generate_image(prompt,negative_prompt="",output_format="png",aspect_ratio="1:1"):
    response = requests.post(
        f"https://api.stability.ai/v2beta/stable-image/generate/core",
        headers={
            "authorization": f"Bearer sk-saMcB871NueeMnAO3SYpTwNiGRyz2D5t1rZtQBI9vfG56wF1 ",
            "accept": "image/*"
        },
        files={
            "none": ''
        },
        data={
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "output_format": output_format,
            "aspect_ratio": aspect_ratio,
        },
    )
    return response
    if response.status_code == 200:
        return 200, response.content
        with open("./lighthouse.png", 'wb') as file:
            file.write(response.content)
    else:
        return response.status_code, str(response.json())
        raise Exception(str(response.json()))

"""
curl -f -sS "https://api.stability.ai/v2beta/stable-image/generate/core" -H "authorization: Bearer sk-saMcB871NueeMnAO3SYpTwNiGRyz2D5t1rZtQBI9vfG56wF1" -H "accept: image/*" -F prompt="Lighthouse on a cliff overlooking the ocean" -F output_format="webp" -o "./lighthouse.webp"
"""


