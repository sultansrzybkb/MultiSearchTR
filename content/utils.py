import unicodedata

def normalize_query(query):
    translation_table = str.maketrans({
        'ş': 's', 'Ş': 'S',
        'ı': 'i', 'I': 'i',
        'ç': 'c', 'Ç': 'C',
        'ü': 'u', 'Ü': 'U',
        'ö': 'o', 'Ö': 'O',
        'ğ': 'g', 'Ğ': 'G',
        'İ': 'i'
    })
    
    normalized_query = query.translate(translation_table).lower()
    return normalized_query