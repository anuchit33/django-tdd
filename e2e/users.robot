*** Settings ***
Library     Selenium2Library
Library     String
Library     Collections
Library     RequestsLibrary
Library	    OperatingSystem

Resource   ${EXECDIR}/e2e/keyword.robot
Resource   ${EXECDIR}/e2e/variables.robot

Suite Setup     InitData
Suite teardown   Close Browser

*** Test Cases ***
test01 เข้าหน้ารายการ users
  Open Browser        ${base_url}   chrome

  # พบ user 3ชื้อผู้ใช้งาน
  Wait Until Page Contains        user1
  Wait Until Page Contains        user2
  Wait Until Page Contains        user3