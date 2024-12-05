# -*- coding: utf-8 -*-
# from odoo import http


# class Managejoseluis(http.Controller):
#     @http.route('/managejoseluis/managejoseluis', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/managejoseluis/managejoseluis/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('managejoseluis.listing', {
#             'root': '/managejoseluis/managejoseluis',
#             'objects': http.request.env['managejoseluis.managejoseluis'].search([]),
#         })

#     @http.route('/managejoseluis/managejoseluis/objects/<model("managejoseluis.managejoseluis"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('managejoseluis.object', {
#             'object': obj
#         })
