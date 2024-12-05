#-*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api


class history(models.Model):
    _name = 'managejoseluis.history'
    _description = 'managejoseluis.history'

    name = fields.Char(string="Nombre", readonly = False, required = True, help = "Introduzca el nombre")
    description = fields.Text(string="Descripción")

    project_id = fields.Many2one("managejoseluis.project", string = "Proyecto", required=True, ondelete= "cascade")

    task_id = fields.One2many(string= "Tarea", comodel_name= "managejoseluis.task", inverse_name= "history_id")

    used_technologies = fields.Many2many("managejoseluis.technology", compute = "_get_used_technologies")

    @api.depends('task_id.tecnologias_id')
    def _get_used_technologies(self):
        for history in self:
            technologies = self.env['managejoseluis.technology']  # Inicializamos un conjunto vacío
            for task in history.task_id:
                technologies |= task.tecnologias_id  # Usamos '|' para combinar tecnologías
            history.used_technologies = technologies
