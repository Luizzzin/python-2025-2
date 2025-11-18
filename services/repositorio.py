import os
import json

class Repositorio:
    def __init__(self, arquivo="data/perfis.json"):
        self.arquivo = arquivo
        os.makedirs("data", exist_ok=True)  # garante que a pasta exista

    def salvar_perfil(self, nome, respostas, prof1, afi1, prof2, afi2):
        perfis = self.listar_todos()

        dados = {
            "nome": nome,
            "respostas": respostas,
            "melhor_profissao": prof1,
            "afinidade_1": afi1,
            "segunda_profissao": prof2,
            "afinidade_2": afi2
        }

        perfis.append(dados)

        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(perfis, f, indent=4, ensure_ascii=False)

    def listar_todos(self):
        if not os.path.exists(self.arquivo):
            return []

        with open(self.arquivo, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
