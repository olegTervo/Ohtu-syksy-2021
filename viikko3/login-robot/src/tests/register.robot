*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User  test  test1234

*** Test Cases ***
Register With Valid Username And Password
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command And Create User  test  test1234
    Output Should Contain  User with username test already exists

Register With Too Short Username And Valid Password
    Input New Command And Create User  a  test1234
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input New Command And Create User  testi  test12
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command And Create User  testi  testtest
    Output Should Contain  Password should contain at least one number
