# -*- coding: utf-8 -*-
from odoo import fields, models, api, SUPERUSER_ID,_
from .xiaomi import XMSport
from odoo.exceptions import UserError


class FunctionPopupWizard(models.TransientModel):
    _name = 'function.popup_wizard'
    _description = '功能弹窗'

    name = fields.Char(string="功能名")
    update_steps = fields.Integer(string="更新步数")

    def run_script(self):
        user_list = self.env.context['user_list']
        error_list = []
        for r in user_list:
            xm_sport = XMSport(user=r['account'], password=r['password'], step=str(self.update_steps),
                               login_token=r['login_token'],
                               app_token=r['app_token'], user_id=r['user_id'])
            result = xm_sport.main_run()
            state = result['state']
            if state == "success":
                if 'login_information' in result:
                    account_id = self.env['xm.update_sport'].search([('account', '=', r['account'])])
                    account_id.write(result['login_information'])
                    return {
                        'type': 'ir.actions.client',
                        'tag': 'display_notification',
                        'params': {
                            'message': '更新成功！',
                            'type': 'success',
                            'sticky': False,
                        }
                    }
            elif state == "login_error":
                error_list.append({"account": r['account']})
                print('账号或密码错误！')
            else:
                print(state, '别的错误')
        if error_list:
            raise UserError(_(f'你的{error_list}账号或密码错误！'))
