import pandas as pd

import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/dados.json')
def serve_json():
    with open('dados.json', 'r') as f:
        data = f.read()
    return jsonify(data)

def processar_planilha(arquivo):
    # Ler o arquivo CSV com delimitador ;
    df = pd.read_csv(arquivo, delimiter=';')
    # Aqui você pode adicionar qualquer processamento necessário para as colunas.
    # Como exemplo, vamos supor que você queira preencher valores nulos com zero:
    df.fillna(0, inplace=True)

    # Salvar os dados tratados em um novo arquivo ou sobrescrever o existente
    df.to_csv("planilha_tratada.csv", index=False, sep=';')

def converter_para_json(arquivo):
    df = pd.read_csv(arquivo, delimiter=';')
    json_str = df.to_json(orient='records')
    with open('dados.json', 'w') as f:
        f.write(json_str)

if __name__ == "__main__":
    nome_do_arquivo = "osinfo/unificado.csv"
    processar_planilha(nome_do_arquivo)
    converter_para_json("planilha_tratada.csv")
    app.run(debug=True, host='0.0.0.0', port=8080)
