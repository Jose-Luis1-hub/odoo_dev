from odoo import models, fields, api

class tecnica(models.Model):
    _name = 'filmotecajoseluis.tecnica'
    _descripcion = 'filmotecajoseluis.tecnica'

    name = fields.Char(string="Nombre")
    descripcion = fields.Text(string = "Descripcion")
    foto = fields.Image(string="Imagen") 

    peliculas_id = fields.Many2many(comodel_name = "filmotecajoseluis.pelicula",
                                    relation = "tecnicas_peliculas",
                                    column1 = "peliculas_id",
                                    column2 = "tecnicas_id"
                                    )