import unicodedata

def normalize_query(query):
    translation_table = str.maketrans({
        'ş': 's', 'Ş': 'S',
        'ı': 'i', 'I': 'i',
        'İ': 'i',
        'ç': 'c', 'Ç': 'C',
        'ü': 'u', 'Ü': 'U',
        'ö': 'o', 'Ö': 'O',
        'ğ': 'g', 'Ğ': 'G'
    })
    
    normalized_query = query.translate(translation_table).lower()
    return unicodedata.normalize('NFKD', normalized_query)

test_queries = [
    "İstanbul",
    "istanbul",
    "Çeşme",
    "çesme",
    "şeker",
    "Seker",
    "Göl",
    "gol",
    "Iğdır",
    "igdir",
]

for query in test_queries:
    normalized = normalize_query(query)
    print(f"Original: {query} -> Normalized: {normalized}")