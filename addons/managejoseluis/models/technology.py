#-*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api


class technology(models.Model):
    _name = 'managejoseluis.technology'
    _description = 'managejoseluis.technology'

    name = fields.Char(string="Nombre", readonly = False, required = True, help = "Introduzca el nombre")
    description = fields.Char(string="Descripción")
    photo = fields.Image(string="Imagen") 

    tareas_id = fields.Many2many(string ="Tareas", comodel_name ="managejoseluis.task", relation = "tecnologias_tareas", column1 = "tareas_ids", column2 = "tecnologias_ids")