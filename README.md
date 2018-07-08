# USTC-Software-2018-BE-Test
USTC iGEM Software 2018 Back-end Test Project

## 报告

be_test注册app'user'，完成功能有用户注册register、登录login、个人信息profile、登出logout
用户能注册新账号（传入注册过的用户名则注册失败）
登录账号（不可重复登录）并且可以在个人信息中看到自己的用户名。
用户登出后将不能在个人信息中看到相关信息。

### 调用方法

注册、登录请求类型为POST，查看信息、登出请求类型为GET
对于注册，传入方法为/user/register 附加POST参数{'username':example_name,'password':example_password}
对于登录，传入方法为/user/login    附加POST参数{'username':example_name,'password':example_password}
查看信息，传入方法为/user/profile/?username=example_name,查询成功会返回错误码0及username
登出传入方法为/user/logout/?username=example_name

### 注意事项

注册、登录、查看信息、登出对应url依次为/user/register/、/user/login/、/user/profile/、/user/logout/
User中用户名为name，与输入时的"username"不同

### 错误码约定

返回格式（json）：
{
    "err_code":错误码,
    "err_msg":错误信息
}

返回的错误码对应的信息为：
|  返回码  |  错误信息  |  解释  |
|  --------  |:----------:|  ----------:|
|  0  |  null  |  正常返回  |
|  1  |  User Exists  |  注册错误，用户已存在  |
|  2  |  User Has Not Logged in  |  查看用户信息/用户登出错误，用户未登录  |
|  3  |  Wrong Password  |  登录错误，密码输入错误  |
|  4  |  User Does Not Exist  |  登录错误，用户名不存在  |
|  5  |  User Has Logged in  |  登录错误，用户已经登录，不可重复登录  |
