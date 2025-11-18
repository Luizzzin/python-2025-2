import json

class Avaliador:
    def __init__(self):
        self.profissoes = self._carregar_profissoes()

    def _carregar_profissoes(self):

        with open("data/profissoes.json", "r") as f:
            return json.load(f)

    def _calcular_afinidade(self, respostas_usuario, pesos_profissao):

        pontos = 0
        total = 4  # T, A, C, P

        for r_user, r_prof in zip(respostas_usuario, pesos_profissao):
            if r_user == r_prof:
                pontos += 1

        afinidade = (pontos / total) * 100
        return round(afinidade, 2)

    def analisar(self, respostas_usuario):



        resultados = []

        for profissao in self.profissoes:
            nome = profissao["nome"]
            pesos = profissao["pesos"]

            afinidade = self._calcular_afinidade(respostas_usuario, pesos)

            resultados.append((nome, afinidade))


        resultados.sort(key=lambda x: x[1], reverse=True)

        melhor_profissao, melhor_afinidade = resultados[0]
        segunda_profissao, segunda_afinidade = resultados[1]

        return melhor_profissao, melhor_afinidade, segunda_profissao, segunda_afinidade
