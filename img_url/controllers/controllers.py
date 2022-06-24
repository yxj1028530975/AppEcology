# -*- coding: utf-8 -*-
import json

from odoo import http, SUPERUSER_ID
from odoo.http import request


class ImgUrlController(http.Controller):
    @http.route('/api/category/search', type='http', methods=['GET'],
                auth='public', csrf=False,
                cors="*")
    def img_category_search(self, token, category=None, **kw):
        """
        返回图像链接和图像名称的函数。

        :param token: 令牌是您在配置中设置的令牌。
        :param category: 类别名称，如果不是，则返回所有图片。
        :return: 一个 JSON 对象。
        """
        img_config_settings_id = request.env['img.config.settings'].with_user(SUPERUSER_ID).search(
            [('token', '=', token)])
        if not img_config_settings_id:
            return json.dumps({'states': 'token错误！'})
        if category:
            img_category_id = request.env['img.category'].with_user(SUPERUSER_ID).search(
                [('name', '=', category)])
            if not img_category_id:
                return json.dumps({'states': '类别错误！'})
            img_url_id = request.env['img.url'].with_user(SUPERUSER_ID).search(
                [('category_id', '=', img_category_id.id)])
            img_url_list = [{'name': img_url.name, 'link': img_url.link} for img_url in img_url_id]
            return json.dumps({'states': 'success', 'img_url_list': img_url_list})
        else:
            img_url_id = request.env['img.url'].with_user(SUPERUSER_ID).search([])
            img_url_list = [{'name': img_url.name, 'link': img_url.link} for img_url in img_url_id]
            return json.dumps({'states': 'success', 'img_url_list': img_url_list})

    @http.route('/api/search/category', type='http', methods=['GET'],
                auth='public', csrf=False,
                cors="*")
    def img_search_category(self, token, **kw):
        """
        查询图片类别
        :param token: 令牌与配置文件中的令牌相同。
        :return: 具有键“状态”和值“成功”以及键“img_category_list”和值“img_category_list”的 json 对象
        """
        img_config_settings_id = request.env['img.config.settings'].with_user(SUPERUSER_ID).search(
            [('token', '=', token)])
        if not img_config_settings_id:
            return json.dumps({'states': 'token错误！'})
        img_category_id = request.env['img.category'].with_user(SUPERUSER_ID).search([])
        img_category_list = [img_category.name for img_category in img_category_id]
        return json.dumps({'states': 'success', 'img_category_list': img_category_list})

    @http.route('/api/name/search', type='http', methods=['GET'],
                auth='public', csrf=False,
                cors="*")
    def img_name_search(self, token, name, **kw):
        """
        > 此功能按名称搜索图像

        :param token: 您从登录方法获得的令牌
        :param name: 要搜索的图像的名称。
        """
        img_config_settings_id = request.env['img.config.settings'].with_user(SUPERUSER_ID).search(
            [('token', '=', token)])
        if not img_config_settings_id:
            return json.dumps({'states': 'token错误！'})
        img_url_id = request.env['img.url'].with_user(SUPERUSER_ID).search([('name', '=', name)])
        if not img_url_id:
            return json.dumps({'states': '图片名称错误！'})
        img_url_list = [{'name': img_url.name, 'link': img_url.link} for img_url in img_url_id]
        return json.dumps({'states': 'success', 'img_url_list': img_url_list})
