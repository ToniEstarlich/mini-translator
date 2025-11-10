import requests

# URL de la API
url = 'https://api.mymemory.translated.net/get'

# Parámetros de la solicitud
params = {
    'q': 'hello',             # Texto a traducir
    'langpair': 'en|ja'       # Idiomas: inglés a japonés
}

# Hacer la solicitud GET con verify=False para evitar errores SSL
response = requests.get(url, params=params, verify=False)

# Convertir a JSON
data = response.json()

# Mostrar toda la respuesta
print("Respuesta completa de la API:")
print(data)

# Extraer la traducción principal
translated_text = data['responseData']['translatedText']
print("\nTraducción:")
print(translated_text)