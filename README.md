## 报告

### 调用方法

1. 安装需要的依赖，依赖的包在`requirements.txt`内，使用如下命令安装：

   ```shell
   pip3 install requirements.txt
   ```

2. 创建记录和数据表：

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

   ​

3. 启动服务器：

   ```shell
   python manage.py runserver
   ```

   ​

### 注意事项

1. Django可以在服务器运行时指定端口号，默认为8000

2. 为了测试需要，`settings.py`中设置：

   1. `DEBUG = True`;
   2. csrf验证关闭，即把：`django.middleware.csrf.CsrfViewMiddleware`一行注释掉。

   项目安全性要求更高时应打开csrf验证。

### 错误码约定

| 网址     | err_code | err_msg                             | 描述                       |
| -------- | -------- | ----------------------------------- | -------------------------- |
| login    | 0        | ""                                  | 登陆成功                   |
| login    | -1       | "Password does not correst"         | 密码错误                   |
| login    | -2       | "Username does not exist"           | 用户名未注册               |
| login    | -3       | "Please logout before login"        | 在登陆状态下登陆           |
| logout   | 0        | ""                                  | 登出成功                   |
| logout   | -1       | "Please login before you logout"    | 在登出状态下登出           |
| register | 0        | ""                                  | 注册成功                   |
| register | -1       | "Please logout before you register" | 登陆状态时无法注册         |
| register | -2       | "Passwords are different"           | 注册时两次输入的密码不一致 |
| register | -3       | "Username has been used"            | 用户名已被注册             |

