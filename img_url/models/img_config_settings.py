from odoo import _, fields, models
import uuid

aaa = uuid.uuid1()


class ImgConfigSettings(models.Model):
    _name = "img.config.settings"
    _description = '图床'
    base_url = fields.Char(string="网址ip")
    token = fields.Char(string="身份令牌", default=aaa)
