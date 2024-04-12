import requests

def generate_image(prompt):
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
            "output_format": "png",
        },
    )

    if response.status_code == 200:
        with open("./lighthouse.png", 'wb') as file:
            file.write(response.content)
    else:
        raise Exception(str(response.json()))

"""
curl -f -sS "https://api.stability.ai/v2beta/stable-image/generate/core" -H "authorization: Bearer sk-saMcB871NueeMnAO3SYpTwNiGRyz2D5t1rZtQBI9vfG56wF1" -H "accept: image/*" -F prompt="Lighthouse on a cliff overlooking the ocean" -F output_format="webp" -o "./lighthouse.webp"
"""