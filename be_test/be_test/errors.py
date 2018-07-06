"""
Global Error Definition (0~99)

For reference:
User        100~199
Chart       200~299
"""

SUCCESS = {'err_code': 0, 'err_msg': ''}
NOT_IMPLEMENTED = {'err_code': 1, 'err_msg': 'Not implemented'}
INSUFFICIENT_ARGS = {'err_code': 2, 'err_msg': 'Insufficient arguments'}
LOGGED_IN = {'err_code': 3, 'err_msg': 'Already logged in'}
NOT_LOGGED_IN = {'err_code': 4, 'err_msg': 'Not logged in'}
