import requests
r = requests.post(
    "https://api.deepai.org/api/text-generator",
    data={
        'text': 'YOUR_TEXT_URL',
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
print(r.json())