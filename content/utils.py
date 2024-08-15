TRANSLATION_TABLE = str.maketrans({
        'ş': 's', 'Ş': 'S',
        'ı': 'i', 'I': 'i',
        'ç': 'c', 'Ç': 'C',
        'ü': 'u', 'Ü': 'U',
        'ö': 'o', 'Ö': 'O',
        'ğ': 'g', 'Ğ': 'G',

        
    })

def normalize_query(query):
    return query.translate(TRANSLATION_TABLE).lower()