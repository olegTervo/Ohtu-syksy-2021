*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Register With Valid Username And Password
    Go To Registration Page
    Set Username  kalle
    Set Password  kalle456
    Set Password Confirmation  kalle456 
    Submit Credentials
    Wellcome Page Should Be Open

Register With Too Short Username And Valid Password
    Go To Registration Page
    Set Username  k
    Set Password  kalle456
    Set Password Confirmation  kalle456
    Submit Credentials
    Registration Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Go To Registration Page
    Set Username  kalle
    Set Password  k56
    Set Password Confirmation  k56
    Submit Credentials
    Registration Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Go To Registration Page
    Set Username  kalle
    Set Password  kalle456
    Set Password Confirmation  kalle4567
    Submit Credentials
    Registration Should Fail With Message  Password Confirmation doesn't match

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set PasswordConfirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
