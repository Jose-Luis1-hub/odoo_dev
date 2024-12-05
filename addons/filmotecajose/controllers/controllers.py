# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json


# class Filmotecajose(http.Controller):
#     @http.route('/filmotecajose/filmotecajose', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/filmotecajose/filmotecajose/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('filmotecajose.listing', {
#             'root': '/filmotecajose/filmotecajose',
#             'objects': http.request.env['filmotecajose.filmotecajose'].search([]),
#         })

#     @http.route('/filmotecajose/filmotecajose/objects/<model("filmotecajose.filmotecajose"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('filmotecajose.object', {
#             'object': obj
#         })


class pelicula_controller(http.Controller):

    @http.route('/api/peliculas', auth='public', method=['GET'], csrf=False)
    def get_peliculas(self, **kw):
        try:
            peliculas = http.request.env['filmotecajoseluis.pelicula'].sudo().search_read([], ['id', 'name', 'color'])
            res = json.dumps(peliculas, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)
