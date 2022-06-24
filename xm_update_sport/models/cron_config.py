# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import UserError


class CronConfig(models.Model):
    _name = 'cron.config'
    _description = '定时配置'

    interval_type = fields.Selection([('minutes', '分'),
                                      ('hours', '时'),
                                      ('days', '天'),
                                      ('weeks', '周'),
                                      ('months', '月')], string='定时执行', default='days')
    is_cron = fields.Boolean(string="启用")
    nextcall = fields.Datetime(string='下次开始时间', required=True, default=fields.Datetime.now,
                               help="开始时间")
    lastcall = fields.Char(string='调用次数',
                           help="调用次数限制，负数代表无限次")
    doall = fields.Boolean(string='错漏重做',
                           help="服务重启导致错漏重做")

    @api.model
    def create(self, vals_list):
        cron_config_id = self.env['cron.config'].search([])
        print(self.env)
        if cron_config_id:
            raise UserError('已有配置！')
        else:
            xm_update_sport_id = self.env['ir.model'].search([('name', '=', 'xm.update_sport')])
            if not xm_update_sport_id:
                raise UserError('模块出错！')
            ir_cron_id = self.env['ir.cron'].create([{
                'name': f'{self.env.user.name}-定时任务',
                'user_id': self.env.user,
                'model_id': xm_update_sport_id.id,
                'nextcall': self.nextcall,
                'active': self.is_cron,
                'numbercall': self.lastcall,
                'doall': self.doall,
            }])
            if not ir_cron_id:
                raise UserError('创建定时任务出错！')
        return super(CronConfig, self).create(vals_list)


