# -*- coding: utf-8 -*-
# from odoo import http


# class TremingMarioGomez(http.Controller):
#     @http.route('/treming_mario_gomez/treming_mario_gomez/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/treming_mario_gomez/treming_mario_gomez/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('treming_mario_gomez.listing', {
#             'root': '/treming_mario_gomez/treming_mario_gomez',
#             'objects': http.request.env['treming_mario_gomez.treming_mario_gomez'].search([]),
#         })

#     @http.route('/treming_mario_gomez/treming_mario_gomez/objects/<model("treming_mario_gomez.treming_mario_gomez"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('treming_mario_gomez.object', {
#             'object': obj
#         })
