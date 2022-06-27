# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ImgUrl(models.Model):
    _name = 'img.url'
    _description = '图床'

    name = fields.Char(string="名称")
    enclosure = fields.Many2many('ir.attachment', string="附件")
    img_category = fields.Many2one('img.category', string="类别",required=True)
    link = fields.Char(string="链接", compute='_compute_link')
    avatar = fields.Html('头像', compute='_compute_avatar')


    def notification(self):
        """
        当用户点击通知图标时调用的函数。
        """
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'message': '复制成功！',
                'type': 'success',
                'sticky': False,
            }
        }

    def _compute_link(self):
        """
        计算图片url
        """
        base_url = self.env["img.config.settings"].search([], limit=1)
        if base_url:
            base_url = base_url.base_url
        else:
            base_url = "http://localhost:8080/img/"
        for r in self:
            access_token = r.enclosure.access_token
            if access_token:
                r.link = base_url + f"/web/content/{r.enclosure.id}?access_token={access_token}"
                r.name = r.enclosure.name
            else:
                r.link = base_url + f"/web/content/{r.enclosure.id}?access_token={r.enclosure.generate_access_token()[0]}"
                r.name = r.enclosure.name

    @api.depends('link')
    def _compute_avatar(self):
        """
        它计算用户的头像
        """
        for each_record in self:
            if each_record.link:
                each_record.avatar = f"""<img src="{each_record.link}" style="max-width:100px;">"""
            else:
                each_record.avatar = False

    def test_button(self):
        # view_id = self.env.ref('img_url.function_popup_wizard_view_form').id
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'img_url.popup_wizard',
            'name': '运行程序',
            'view_mode': 'form',
            # 'context': user_list,
            # 'views': [(view_id, "form")],
            'target': 'new',
        }

    def copy_url(self):
        """
        它将当前选项卡的 URL 复制到剪贴板
        """
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'message': '复制成功！',
                'type': 'success',
                'sticky': False,
            }
        }
