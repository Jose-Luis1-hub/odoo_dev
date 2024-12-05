#-*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api


class sprint(models.Model):
    _name = 'managejoseluis.sprint'
    _description = 'managejoseluis.sprint'

    name = fields.Char(string="Nombre", readonly = False, required = True, help = "Introduzca el nombre")
    description = fields.Char(string="Descripción")

    duration = fields.Integer(default=15)
    start_date = fields.Datetime(string= "Dia de comienzo")
    end_date = fields.Datetime(string = "Dia de finalizacion", compute ="_get_end_date", store = True)

    tareas_id = fields.One2many(string = "Tareas", comodel_name = "managejoseluis.task", inverse_name = "carrera_id")

    project_id = fields.Many2one("managejoseluis.project", string = "Proyecto", required=True, ondelete= "cascade")

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for sprint in self:
            if isinstance(sprint.start_date, datetime.datetime) and sprint.duration > 0:
                sprint.end_date = sprint.start_date + datetime.timedelta(days=sprint.duration)
            else:
                sprint.end_date = sprint.start_date

    