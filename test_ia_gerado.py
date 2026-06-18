from app import app

def test_saldo_conta_existente():
    client = app.test_client()
    resposta = client.get("/saldo/1")
    assert resposta.status_code == 200
    assert "saldo" in resposta.get_json()

def test_saldo_conta_inexistente():
    client = app.test_client()
    resposta = client.get("/saldo/999")
    assert resposta.status_code == 404

def test_transferencia_valida():
    client = app.test_client()
    resposta = client.post("/transferencia", json={
        "origem": 1,
        "destino": 2,
        "valor": 100.0
    })
    assert resposta.status_code == 200
    assert resposta.get_json()["mensagem"] == "Transferência realizada com sucesso"

def test_transferencia_saldo_insuficiente():
    client = app.test_client()
    resposta = client.post("/transferencia", json={
        "origem": 2,
        "destino": 1,
        "valor": 999999.0
    })
    assert resposta.status_code == 422