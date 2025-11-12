import requests

# ------------------------
# MyMemory Translation API
# ------------------------
url_translation = 'https://api.mymemory.translated.net/get'

params = {
    'q': 'hello',         # text to translate
    'langpair': 'en|ja'   # language pair: English -> Japanese
    # 'key': 'YOUR_API_KEY'  # optional if needed for Japanese
}

# Make request (verify SSL certificate for safety)
response = requests.get(url_translation, params=params)
data = response.json()

print("Full API Response:")
print(data)

# Get the best available translation from matches
translated_text = None
for match in data.get('matches', []):
    if match.get('translation'):
        translated_text = match['translation']
        break

print("\nTranslation:")
print(translated_text)

# ------------------------
# Pexels API
# ------------------------
url_pexels = "https://api.pexels.com/v1/search"
headers = {
    "Authorization": "pZfFJ8TG6tJnZVUlgoOK7A9CQYYDibcMrZNLVFsqxFQoftV2UjB1dF1N"
}
params_pexels = {
    "query": "cat",
    "per_page": 5
}

response = requests.get(url_pexels, headers=headers, params=params_pexels)
data = response.json()

print("\nPexels Photos:")
for photo in data.get('photos', []):
    print(photo['id'], photo['url'])
