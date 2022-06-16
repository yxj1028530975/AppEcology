# -*- coding: utf-8 -*-
{
    'name': "xm_update_sport",

    'summary': """
        修改微信运动步数""",

    'description': """
        修改步数
    """,

    'author': "木不易成楊！",
    'website': "yxj101.cn",

    'category': '实用工具/实用工具',
    'version': '1',

    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/update_sport_security.xml',
        'security/rules.xml',
        'views/xm_update_sport_views.xml',
        'wizard/function_popup_wizard.xml',
        'views/root_menu.xml',
    ],
    'qweb': [
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
