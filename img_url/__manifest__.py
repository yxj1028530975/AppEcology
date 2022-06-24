# -*- coding: utf-8 -*-
{
    'name': "img_url",
    'summary': """
        图床
        """,
    'description': """
        图床
    """,

    'author': "木不易成楊！",
    'website': "http://www.yourcompany.com",

    'category': '实用工具/实用工具',
    'version': '1',

    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/img_url_security.xml',
        'views/img_url_views.xml',
        'views/img_category_views.xml',
        # 'views/assets.xml',
        'data/data.xml',
        'wizard/function_popup_wizard.xml',
        'views/res_config_settings_view.xml',
        'views/root_menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'img_url/static/src/js/hotel_room_summary.js',
            'img_url/static/src/css/room_summary.css',
        ],
        'web.assets_qweb': [
            "img_url/static/src/xml/hotel_room_summary.xml",
        ],
    },
    'demo': [
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
