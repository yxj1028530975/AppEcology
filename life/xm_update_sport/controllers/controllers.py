# -*- coding: utf-8 -*-
# from odoo import http


# class XmUpdateSport(http.Controller):
#     @http.route('/crm_sale_inherit/crm_sale_inherit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_sale_inherit/crm_sale_inherit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_sale_inherit.listing', {
#             'root': '/crm_sale_inherit/crm_sale_inherit',
#             'objects': http.request.env['crm_sale_inherit.crm_sale_inherit'].search([]),
#         })

#     @http.route('/crm_sale_inherit/crm_sale_inherit/objects/<model("crm_sale_inherit.crm_sale_inherit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_sale_inherit.object', {
#             'object': obj
#         })
