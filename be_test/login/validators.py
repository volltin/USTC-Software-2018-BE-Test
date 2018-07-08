from django.contrib.auth.validators import ASCIIUsernameValidator


class UsernameValidator(ASCIIUsernameValidator):
    # regex = r'^[\w.@+-]+$'
    regex = r'^[a-zA-Z\_][\w.@+-]{5, 19}$'  # 首字母必须是字母或者下划线, 长度6-20
    # message = _(
    #     'Enter a valid username. This value may contain only letters, '
    #     'numbers, and @/./+/-/_ characters.'
    #     'And the first letter is required to be letter or underline.'
    # )
    # flags = 0
