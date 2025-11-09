import requests
import pykakasi

kks = pykakasi.kakasi()

def get_translation(text_en):
    """ translate text and looking imagens"""

    # --- 1 translate with MyMemory API ---
    jp_text = ""
    try:
        resp = requests.post(
            "https://api.mymemory.translated.net/get",
            params={"q": text_en, "langpair": "en|ja"},
            timeout=10
        )
        resp.raise_for_status()
        data = resp.json()
        jp_text = data.get("responseData", {}).get("translatedText", "")
    except Exception as e:
        print("Translation error:", e)
        jp_text = ""

    # --- 2. Conversion to Kana and Romaji ---
    conv = kks.convert(jp_text or "")
    reading_kana = "".join([item.get('hira', '') for item in conv]).strip()
    reading_romaji = " ".join([item.get('hepburn', '') for item in conv]).strip()

    # --- 3. Image from Pexels API (you can use another API) ---
    headers = {"Authorization": "NEXT_dev._PEXELS_API_KEY"}
    image_url = f"https://via.placeholder.com/400x300?text={text_en}"  # fallback
    try:
        pexels_resp = requests.get(
            "https://api.pexels.com/v1/search",
            params={"query": text_en, "per_page": 1},
            headers=headers,
            timeout=10
        )
        pexels_resp.raise_for_status()
        data = pexels_resp.json()
        if data.get("photos"):
            image_url = data["photos"][0]["src"]["medium"]
    except Exception as e:
        print(f"Could not fetch image: {e}")

    return {
        "english": text_en,
        "japanese": jp_text,
        "kana": reading_kana,
        "romaji": reading_romaji,
        "image": image_url
    }
