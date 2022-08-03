*** Settings ***
Library  RequestsLibrary
Variables  config.py

*** Test Cases ***
Testar API Catalago Kabum
    Configurar Sessao
    Realizar requisicao no catalago    
    Validar os campos obrigatorios
*** Keywords ***
Configurar Sessao   
    Create Session  requisicao_catalago  https://servicespub.prod.api.aws.grupokabum.com.br  headers=${HEADERS}  verify=true

Realizar requisicao no catalago
    ${resposta_catalog}=  Get on Session  requisicao_catalago  /catalog/v2/releases
     Log To Console  ${resposta_catalog}
     Set Test Variable  ${resposta_catalog}

Validar os campos obrigatorios
    Request Should Be Sucessful  ${resposta_catalog}
    Should Not Be Empty  ${resposta_catalog.json()}[data]