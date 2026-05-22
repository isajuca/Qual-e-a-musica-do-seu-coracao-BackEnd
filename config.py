# config.py

MUSICA_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "nome_da_musica": {"type": "STRING", "description": "O nome da música real"},
        "artista": {"type": "STRING", "description": "O artista ou banda"},
        "album": {"type": "STRING", "description": "O álbum da música"},
        "ano": {"type": "STRING", "description": "O ano de lançamento"},
        "genero": {"type": "STRING", "description": "O gênero musical"},
        "letra": {"type": "STRING", "description": "Um trecho significativo ou a letra da música"}
    },
    "required": ["nome_da_musica", "artista", "album", "ano", "genero", "letra"]
}

SYSTEM_INSTRUCTION = """
Você é um especialista em música para um Correio Elegante escolar. 
Sua tarefa é receber um sentimento (pode ser uma frase longa ou palavras soltas) e encontrar uma música REAL que combine perfeitamente.
A resposta deve ser SEMPRE em JSON seguindo o schema fornecido. 
Seja romântico e ajude o usuário a expressar seu amor.
"""