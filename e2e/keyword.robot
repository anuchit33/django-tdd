Resource   ${EXECDIR}/e2e/variables.robot

*** Keywords ***

InitData
  Create Session      api    ${base_url}
  ${headers}=    Create Dictionary    Content-Type=application/json
  ${resp}=       GET Request      api     /init-data/
  Should Be Equal As Strings      ${resp.status_code}     200