@'

\# Matriz de Rastreabilidade - Internet Banking



| ID | Requisito | Caso de teste | Artefato | Evidência | Status |

|---|---|---|---|---|---|

| CT-001 | RF-01 - Consultar saldo de conta existente | test\_saldo\_conta\_existente | test\_ia\_gerado.py | report.xml | passou |

| CT-002 | RF-02 - Consultar saldo de conta inexistente | test\_saldo\_conta\_inexistente | test\_ia\_gerado.py | report.xml | passou |

| CT-003 | RF-03 - Realizar transferência válida | test\_transferencia\_valida | test\_ia\_gerado.py | report.xml | passou |

| CT-004 | RF-04 - Bloquear transferência com saldo insuficiente | test\_transferencia\_saldo\_insuficiente | test\_ia\_gerado.py | report.xml | passou |

| CT-005 | RF-05 - Validar contrato HTTP da API | schemathesis run openapi.yaml | openapi.yaml | schemathesis\_output.txt | executado |

'@ | Set-Content -Encoding utf8 matriz\_rastreabilidade.md

