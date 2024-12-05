#-*- coding: utf-8 -*-

from odoo import models, fields, api


class genero(models.Model):
    _name = 'filmotecajoseluis.genero'
    _description = 'filmotecajoseluis.genero'

    name = fields.Char(string="Nombre", readonly = False, required = True, help = "Introduzca el nombre")
    description = fields.Text(string="Descripcion")
    peliculas_id = fields.One2many(string= "Peliculas", comodel_name="filmotecajoseluis.pelicula", inverse_name="genero_id")
    