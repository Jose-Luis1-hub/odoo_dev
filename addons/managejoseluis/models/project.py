#-*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api


class project(models.Model):
    _name = 'managejoseluis.project'
    _description = 'managejoseluis.project'

    name = fields.Char(string="Nombre", readonly = False, required = True, help = "Introduzca el nombre")
    description = fields.Char(string="Descripción")

    history_id = fields.One2many(string= "Historia", comodel_name= "managejoseluis.history", inverse_name= "project_id")

    sprint_id = fields.One2many(string = "Sprint", comodel_name = "managejoseluis.sprint", inverse_name = "project_id")
    