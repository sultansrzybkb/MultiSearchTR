import unicodedata

TRANSLATION_TABLE = str.maketrans({
        'ş': 's', 'Ş': 'S',
        'ı': 'i', 'I': 'i',
        'ç': 'c', 'Ç': 'C',
        'ü': 'u', 'Ü': 'U',
        'ö': 'o', 'Ö': 'O',
        'ğ': 'g', 'Ğ': 'G',
        'İ': 'i'
    })

TRANSLATION_TABLE_TR = str.maketrans({
        'i': 'İ'
    })

def normalize_query(query, tr=False):
    if tr:
        return query.translate(TRANSLATION_TABLE_TR)

    normalized_query = query.translate(TRANSLATION_TABLE).lower()
    return normalized_query