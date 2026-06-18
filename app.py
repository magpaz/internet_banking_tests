from flask import Flask, jsonify, request

app = Flask(__name__)

contas = {
    1: {"saldo": 1000.0, "extrato": []},
    2: {"saldo": 500.0, "extrato": []},
}

@app.route("/saldo/<int:conta_id>", methods=["GET"])
def saldo(conta_id):
    conta = contas.get(conta_id)
    if not conta:
        return jsonify({"erro": "Conta não encontrada"}), 404
    return jsonify({"conta_id": conta_id, "saldo": conta["saldo"]}), 200

@app.route("/transferencia", methods=["POST"])
def transferencia():
    dados = request.get_json() or {}

    origem = dados.get("origem")
    destino = dados.get("destino")
    valor = dados.get("valor")

    if origem not in contas or destino not in contas:
        return jsonify({"erro": "Conta de origem ou destino não encontrada"}), 404

    if not isinstance(valor, (int, float)) or valor <= 0:
        return jsonify({"erro": "Valor inválido"}), 422

    if contas[origem]["saldo"] < valor:
        return jsonify({"erro": "Saldo insuficiente"}), 422

    contas[origem]["saldo"] -= valor
    contas[destino]["saldo"] += valor

    contas[origem]["extrato"].append({"tipo": "saida", "valor": valor, "destino": destino})
    contas[destino]["extrato"].append({"tipo": "entrada", "valor": valor, "origem": origem})

    return jsonify({"mensagem": "Transferência realizada com sucesso"}), 200

@app.route("/extrato/<int:conta_id>", methods=["GET"])
def extrato(conta_id):
    conta = contas.get(conta_id)
    if not conta:
        return jsonify({"erro": "Conta não encontrada"}), 404
    return jsonify({"conta_id": conta_id, "extrato": conta["extrato"]}), 200

if __name__ == "__main__":
    app.run(debug=True)