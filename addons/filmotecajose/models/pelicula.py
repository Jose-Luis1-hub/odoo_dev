#-*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api


class pelicula(models.Model):
    _name = 'filmotecajoseluis.pelicula'
    _description = 'filmotecajoseluis.pelicula'

    name = fields.Char(string="Nombre", readonly = False, required = True, help = "Introduzca el nombre")
    description = fields.Text(string="Descripción")

    code = fields.Char(string="Código", compute = "_get_code")
    
    film_date = fields.Date(string= "Dia de rodaje")
    start_date = fields.Datetime(string= "Dia de comienzo")
    end_date = fields.Datetime(string = "Dia de finalizacion")
    is_spanish = fields.Boolean(string = "¿Española?")
    
    imagen = fields.Image(string="Cartel", max_width=1024, max_height=1024)
    language = fields.Selection([('es', 'Español'), ('en', 'Inglés'), ('fr', 'Francés'), ('de', 'Alemán')],string="Idioma",help="Selecciona el idioma de la película")
    opinion = fields.Selection([('0', 'Mala'), ('1', 'Regular'), ('2', 'Buena')], default='1', string= "Opinion")
    color = fields.Boolean(string="Color")

    genero_id = fields.Many2one("filmotecajoseluis.genero", string = "Género", required = True, ondelete = "cascade")
    tecnicas_id = fields.Many2many(comodel_name = "filmotecajoseluis.tecnica",
                                   relation = "tecnicas_peliculas",
                                   column1 = "tecnicas_id",
                                   column2 = "peliculas_id")
    
    def _get_code(self):
        for pelicula in self:
            if len(pelicula.genero_id) == 0:
                pelicula.code = "PELICULA" + str(pelicula.id)
            else:
                pelicula.code = str(pelicula.genero_id.name).upper() + "_" + str(pelicula.id)

    def toggle_color(self): 
        self.color = not self.color

    def f_create(self):
        pelicula = {
            "name": "Prueba ORM",
            "color": True,
            "genero_id": 1,
            "start_date": str(datetime.date(2022,8,8))
        }
        print(pelicula)
        self.env['filmotecajoseluis.pelicula'].create(pelicula)

    def f_search_update(self):
        pelicula = self.env['filmotecajoseluis.pelicula'].search([('name','=', 'Inception')])
        print('search()', pelicula, pelicula.name)

        pelicula.write({
            "name": "Star Wars"
        })

    def f_delete(self): 
        pelicula = self.env['filmotecajoseluis.pelicula'].browse([5])
        pelicula.unlink()
    
