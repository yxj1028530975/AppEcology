# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ImaCategory(models.Model):
    _name = 'img.category'
    _description = '商品类别'

    name = fields.Char(
        string='名称',
        required=True
    )

    parent_id = fields.Many2one(
        comodel_name='img.category',
        index=True,
        ondelete="cascade",
        string='上级类别'
    )

    child_ids = fields.One2many(
        comodel_name='img.category',
        inverse_name='parent_id',
        string='下级类别'
    )
    parent_path = fields.Char(index=True)




