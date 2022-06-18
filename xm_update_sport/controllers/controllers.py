# -*- coding: utf-8 -*-
import json

from odoo import http, SUPERUSER_ID
from odoo.http import request
from ..wizard.xiaomi import XMSport


class XmUpdateSport(http.Controller):
    @http.route('/api/update/', type='http', methods=['GET'],
                auth='public', csrf=False,
                cors="*")
    def update_sport(self, user, password, update_steps, **kw):
        user_id = request.env['xm.update_sport'].with_user(SUPERUSER_ID).search(
            [('account', '=', user), ('password', '=', password)])
        if user_id:
            xm_sport = XMSport(user=user, password=password, step=str(update_steps),
                               login_token='login_token',
                               app_token='app_token', user_id='user_id')
            result = xm_sport.main_run()
            state = result['state']
            if state == "success":
                if 'login_information' in result:
                    user_id.write(result['login_information'])
                    return json.dumps({'states': 'success'})
            elif state == "login_error":
                print('账号或密码错误！')
                return json.dumps({'states': '账号或密码错误！'})
            else:
                return json.dumps({'states': '别的错误！'})
        else:
            return json.dumps({'states': '请先在平台绑定账户！'})
