#-*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api


class task(models.Model):
    _name = 'managejoseluis.task'
    _description = 'managejoseluis.task'

    code = fields.Char(string ="Codigo", compute = "_get_code")
    name = fields.Char(string="Nombre", readonly = False, required = True, help = "Introduzca el nombre")
    description = fields.Char(string="Descripción")

    start_date = fields.Datetime(string= "Dia de comienzo")
    end_date = fields.Datetime(string = "Dia de finalizacion")
    is_paused = fields.Boolean(string = "¿Pausado?")

    carrera_id = fields.Many2one("managejoseluis.sprint", string = "Carrera", ondelete = "cascade", compute = "_get_sprint", store = True)
    tecnologias_id = fields.Many2many(comodel_name = "managejoseluis.technology", relation = "tecnologias_tareas", column1 ="tecnologias_ids", column2 = "tareas_ids")

    history_id = fields.Many2one("managejoseluis.history", string ="Historia", required = True, ondelete = "cascade")

    project = fields.Many2one('managejoseluis.project', related='history_id.project_id', readonly = True)

    definition_date = fields.Datetime(default= lambda p: datetime.datetime.now())

    def _get_code(self):
        for task in self:
            task.code = "TSK_" + str(task.id)

    @api.depends('code')
    def _get_sprint(self):
        for task in self:
            sprints = self.env['managejoseluis.sprint'].search([('project_id', '=', task.history_id.project_id.id)])
            found = False 
            for sprint in sprints:
                if isinstance(sprint.end_date, datetime.datetime) and sprint.end_date > datetime.datetime.now():
                    task.carrera_id = sprint.id
                    found = True
            if not found:
                task.carrera_id = False


    