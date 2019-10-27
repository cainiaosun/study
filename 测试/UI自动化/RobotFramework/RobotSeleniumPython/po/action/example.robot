#setting部分导入测试库、资源文件、变量文件、初始化测试套件和用例等
*** Settings ***
Library  SeleniumLibrary
Library  mock
Library     example
#Library  sys

#variables部分定义需要使用的变量
*** Variables ***
${VOLID_USER}         1111
${VOLID_PASSWORD}    2222

${LOGIN_URL}          https://www.baidu.com/

${LOGIN_LING}         //a[@onclick="login();return false"]  #主页面登录链接xpth
${USER_LOCAL}         input1  #登录页面账户名输入框ID
${PASSWORD_LOCAL}     input2  #登录页面密码输入框ID
${LOGIN_BTN}            signin  #登录按钮ID

#testcase部分编写测试用例
*** Test Cases ***
Invlid Login
    Open Brower To Home Page
    Maximize Browser Window




#keyword部分，对框架已经实现的关键字进行组合，创建自己的关键字
*** Keywords ***
Open Brower To Home Page
    OPEN BROWSER  ${login_url}   ff
    MAXIMIZE BROWSER WINDOW
    #Home Page Should Be Open


Go To Login Page
    CLICK LINK  ${LOGIN_LING}
    LOGIN PAGE SHOULD BE OPEN

Home Page Should Be Open
    TITLE SHOULD BE  博客园 - 代码改变世界

Login Page Should Be open
    TITLE SHOULD BE  用户登录 - 博客园

Input User Name
    [Arguments]  ${USERNAME}
    WAIT UNTIL ELEMENT IS VISIBLE  ${USER_LOCAL}
    INPUT TEXT  ${USER_LOCAL}  ${USERNAME}

Input Password
    [Arguments]  ${PASSWORD}
    WAIT UNTIL ELEMENT IS VISIBLE  ${PASSWORD_LOCAL}
    INPUT TEXT  ${PASSWORD_LOCAL}  ${PASSWORD}