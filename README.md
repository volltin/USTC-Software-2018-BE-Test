# USTC-Software-2018-BE-Test
USTC iGEM Software 2018 Back-end Test Project

## 目标

你的目标是使用 GitHub **fork 本仓库**，编写一个简单的 Django 程序，并且**修改本文件**完成文末的简单报告，完成之后**发起 Pull Request**。

截止日期是：2018 年 7 月 8 日 23:00。

### 完成目标的流程

一共有四个步骤：

- fork 本仓库；
- 编写 Django 程序（已经创建在 be_test）；
- 修改本文件完成报告；
- 发起 Pull Request；

### 约定

为了节约大家时间，尽量使用默认情况下的组件：

- 使用 Python 3.6；
- 使用 Django 2.0；
- 使用默认数据库（SQLite）和 ORM；
- 使用默认内建 HTTP Server；
- 使用默认监听端口；
- 不必使用 Template；
- 不必编写 HTML 页面（返回值是 json 或图片）；

### 目标功能

- 注册 login
- 登陆 register
- 个人信息 profile
- 登出 logout （选做）
- 生成图表 chart（选做）

### 功能描述

用户能注册新账号，登陆账号并且在个人信息中看到自己的用户名。

用户登出后将不能在个人信息中看到相关信息。

使用生成图表功能，用户可以传入一列数据，得到一张折线图（横坐标默认为 1, 2, ..., n）。

## 细节

### 数据格式

#### 传入参数

如果为 GET 请求类型，则以 `/api?key=value` 的方式传入；

如果为 POST 请求类型，则以 `/api` 并且附加 POST 参数 `key=value` 的方式传入。

#### 返回内容

返回内容使用 json 格式，如：

```json
{
    "err_code": 0,
    "err_msg": ""
}
```

### 注册

POST /user/register

| 参数 | 默认 | 描述 |
| ------------- |:-------------:| -----:|
| username | 不能为空 | 用户名 |
| password | 不能为空 | 密码 |

| 返回值 | 默认 | 描述 |
| ------------- |:-------------:| -----:|
| err_code | 0 | 错误码 |
| err_msg  | 空 | 错误消息 |

注册一个新账号。

基础要求：

- 传入没有使用过的用户名时能够注册成功，并返回 `err_code` 为 0。

加分项：

- 用户名限制允许的字符集和长度，并返回相应的错误信息；
- 密码限制允许的字符集和长度，并返回相应的错误信息；
- 密码限制最低复杂度，并返回相应的错误信息；

### 登陆

POST /user/login

| 参数 | 默认 | 描述 |
| ------------- |:-------------:| -----:|
| username | 不能为空 | 用户名 |
| password | 不能为空 | 密码 |

| 返回值 | 默认 | 描述 |
| ------------- |:-------------:| -----:|
| err_code | 0 | 错误码 |
| err_msg  | 空 | 错误消息 |

登陆一个账号。

基础要求：

- 用户名密码正确时，登陆成功，并设置 session 为登录状态，返回登陆成功的代码；
- 用户名密码错误时，返回错误信息；

加分项：

- 适当修改接口，使得可以定制保持登陆的时间；
- 记录用户最近一次登陆时间；
- 记录用户最近一次登陆 IP；

### 个人信息

GET /user/profile

| 返回值 | 默认 | 描述 |
| ------------- |:-------------:| -----:|
| err_code | 0 | 错误码 |
| err_msg  | 空 | 错误消息 |
| username  | 空 | 用户名 |

获得登陆账号的信息。

基础要求：

- 如果用户已经登陆，在 `username` 中返回登陆的用户名，否则为空；

加分项：

- 如果用户未登陆，返回错误信息；

### 登出

GET /user/logout

|  返回值  | 默认 |   描述   |
| ------------- |:-------------:| -----:|
| err_code | 0    |  错误码  |
| err_msg  | 空   | 错误消息 |

登出用户。

基本要求：

- 清除登陆的凭证（session）；

加分项：

- 记录用户最后一次登出时间；
- 记录用户最近一次登出 IP；

### 生成图表

POST /chart/simple

自行设置参数格式，返回一张可以在线预览的图片；

基本要求：

- 能够根据给出的数据画出折线图；

加分项：

- 返回的页面正确设置类型，使得图片能在浏览器中直接预览（而不是下载）；
- 对同一组数据不重复生成图片；
- 能够通过参数指定不同大小；

## 检查方式

### 基础要求

使用脚本进行自动检查。

### 加分项

采用人工检查。

### 其他

良好的代码风格（如变量命名）会有额外加分；

良好的文档会有额外加分；

良好的 Git 提交记录（每次提交有明确的信息）会有额外加分；

良好的安全性、鲁棒性、可扩展性会有额外加分；

良好的单元测试有额外加分；

## 报告（需要完成）

请面向该后端应用的使用者（前端组），完成下面报告。

### 调用方法

#### 服务器启动
1. 安装相关依赖
```
pip3 install -r requirements.txt
```

2. 初始化数据库

```
python3 manage.py makemigrations
python3 manage.py migrate
```

3. 启动服务器
```
python3 manage.py runserver
```
#### API接口

1. 用户注册：/user/register POST方法，表单应当有username和password两项。返回相关信息的JSON。

2. 用户登录：/user/login POST方法，表单应当有username和password两项。表单中可选login_time，用户设置有效登陆的时间，单位是小时。返回登陆成功与否的JSON。

3. 用户查询：/user/profile GET方法。如果用户已经登陆，返回的JSON带有username域。否则返回非0的错误码。

4. 用户退出：/user/logout GET方法。如果用户已经登陆则消除凭证，如果未登陆，则否则返回非0的错误码。

5. 画图： /chart/simple POST 方法：接受一个名为number的POST域，其值为一个json字符串，例如：[1,2,3,4,5]等。画图成功时，直接以 content-type：image/png格式返回一个图片。否则返回一个带错误信息的JSON。

### 注意事项

+ 端口： 8000
+ 为了方便开发时测试，打开了DEBUG以及关闭了CRFS。生产环境下需打开
+ 没有使用django自带的auth模块，用户密码也并未加密，因此仅仅用于安全需求极低的测试环境。
+ 谨以此致敬Hustcw同学

### 错误码约定

|网址|  err_code  | err_msg |   描述   |
|-------|------------- |:-------------:| -----:|
| register| 0  | ""    |  注册成功  |
| register| -1  | "Username is too long."    | 用户名太长  |
| register| -2  | "Password is too long"    | 密码太长  |
| register| -3  | "The username has been used"    | 用户重名或注册失败  |
| login | 0  | ""    |  登陆成功  |
| login | -1  | "Login failed"    | 用户不存在或密码错误  |
| profile | 0  | ""    |  查询成功，用户名在‘username’域  |
| profile | -1  | "User is not login yet."   |  用户未登录  |
| logout | 0  | ""   |  用户正常退出  |
| logout | -1  | "User is not login yet."   |  用户未登录  |
| logout | -2  | "Username illegal."   |  用户名非法  |
| chart | -1  | "Cann't find data."   |  没有找到number域  |
| chart | -2  | "JSON decode failed."   |  json解析错误  |

