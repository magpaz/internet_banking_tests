import xml.etree.ElementTree as ET
from pathlib import Path

REPORT = Path("report.xml")

casos = [
    {
        "id": "CT-001",
        "requisito": "RF-01 - Consultar saldo de conta existente",
        "caso": "test_saldo_conta_existente",
        "artefato": "test_ia_gerado.py",
        "evidencia": "pytest / report.xml",
    },
    {
        "id": "CT-002",
        "requisito": "RF-02 - Consultar saldo de conta inexistente",
        "caso": "test_saldo_conta_inexistente",
        "artefato": "test_ia_gerado.py",
        "evidencia": "pytest / report.xml",
    },
    {
        "id": "CT-003",
        "requisito": "RF-03 - Realizar transferência válida",
        "caso": "test_transferencia_valida",
        "artefato": "test_ia_gerado.py",
        "evidencia": "pytest / report.xml",
    },
    {
        "id": "CT-004",
        "requisito": "RF-04 - Bloquear transferência com saldo insuficiente",
        "caso": "test_transferencia_saldo_insuficiente",
        "artefato": "test_ia_gerado.py",
        "evidencia": "pytest / report.xml",
    },
    {
        "id": "CT-005",
        "requisito": "RF-05 - Validar contrato HTTP da API",
        "caso": "schemathesis run openapi.yaml",
        "artefato": "openapi.yaml",
        "evidencia": "schemathesis_output.txt",
    },
]

def status_do_caso(nome_caso):
    if not REPORT.exists():
        return "não executado"

    tree = ET.parse(REPORT)
    root = tree.getroot()

    for testcase in root.iter("testcase"):
        nome = testcase.attrib.get("name", "")
        if nome_caso.lower() in nome.lower():
            if testcase.find("failure") is not None or testcase.find("error") is not None:
                return "falhou"
            return "passou"

    if "schemathesis" in nome_caso:
        return "executado em arquivo separado"

    return "não encontrado"

print("# Matriz de Rastreabilidade - Internet Banking\n")
print("| ID | Requisito | Caso de teste | Artefato | Evidência | Status |")
print("|---|---|---|---|---|---|")

for caso in casos:
    print(
        f"| {caso['id']} | {caso['requisito']} | {caso['caso']} | "
        f"{caso['artefato']} | {caso['evidencia']} | {status_do_caso(caso['caso'])} |"
    )