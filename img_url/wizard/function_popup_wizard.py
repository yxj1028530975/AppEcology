# -*- coding: utf-8 -*-
from odoo import fields, models, api, SUPERUSER_ID
from .create_title_img import run_main
import time
import base64


class ImgUrlPopupWizard(models.TransientModel):
    _name = 'img_url.popup_wizard'
    _description = '功能弹窗'

    xg_img_width = fields.Integer(string="画布宽", default=600)
    xg_img_height = fields.Integer(string="画布高", default=400)
    title = fields.Char(string="标题")
    border = fields.Integer(string="边框", default=20)

    def run(self):
        for r in self:
            path_ls = run_main(xg_img_width=r.xg_img_width, xg_img_height=r.xg_img_height, title=r.title,
                               border=r.border)
            print(path_ls)
            with open(path_ls, 'rb') as f:
                img_content_base64 = f.read()
                print(img_content_base64)
                f.close()
            print(base64.encodebytes(img_content_base64))
            data = {
                'name': time.time(),
                'datas': base64.encodebytes(img_content_base64),
                'type': 'binary',
                'res_model': 'img.url',
                'res_id': 0,
                'mimetype': "image/png",
            }
            ir_attachment_id = self.env['ir.attachment'].create([data])
            print(ir_attachment_id)
            img_url_id = self.env['img.url'].create([{
                'enclosure': ir_attachment_id if ir_attachment_id else None
            }])
            print(img_url_id)
