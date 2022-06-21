# -*- coding: utf-8 -*-
from odoo import api, fields, models


class XmUpdateSport(models.Model):
    _name = 'xm.update_sport'
    _description = '修改步数'

    account = fields.Char(string="账户")
    password = fields.Char(string="密码")
    update_steps = fields.Integer(string="更新步数")
    timing = fields.Char(string="定时")
    login_token = fields.Char(string="login_token", default="login_token")
    app_token = fields.Char(string="app_token", default="app_token")
    user_id = fields.Char(string="user_id", default="user_id")
    is_cron = fields.Boolean(string="启用",default=True)

    # 定时器
    def test_timing(self):
        ...

    def test_button(self):
        ...

    def run_script(self):
        user_list = {'user_list': [
            {'account': r.account, 'password': r.password, 'login_token': r.login_token, 'app_token': r.app_token,
             'login_token': r.login_token, 'app_token': r.app_token, 'user_id': r.user_id} for r in self]}
        view_id = self.env.ref('xm_update_sport.function_popup_wizard_view_form').id
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'function.popup_wizard',
            'name': '运行程序',
            'view_mode': 'form',
            'context': user_list,
            'views': [(view_id, "form")],
            'target': 'new',
        }
