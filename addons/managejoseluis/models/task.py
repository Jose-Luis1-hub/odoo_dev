#-*- coding: utf-8 -*-
import base64
import datetime
import json
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

    def exportar_JSON(self):
        for task in self:
            data = {
                'name': task.name,
                'description': task.description,
                'start_date': task.start_date.strftime('%Y-%m-%d %H:%M:%S') if task.start_date else None, #usamos la funcion strftime para dar formato a las fechas y horas, ya que estas no pueden ser convertidas a JSON
                'end_date': task.end_date.strftime('%Y-%m-%d %H:%M:%S') if task.end_date else None, #usamos la funcion strftime para dar formato a las fechas y horas, ya que estas no pueden ser convertidas a JSON
                'is_paused': task.is_paused,
                'carrera_id': task.carrera_id.id, #pasamos el id de los modelos anexos al de tareas ya que no se puede convertir a json un objeto entero
                'tecnologias_id': task.tecnologias_id.id, #pasamos el id de los modelos anexos al de tareas ya que no se puede convertir a json un objeto entero
                'history_id': task.history_id.name, #pasamos el id de los modelos anexos al de tareas ya que no se puede convertir a json un objeto entero
                'project': task.project.name, #pasamos el id de los modelos anexos al de tareas ya que no se puede convertir a json un objeto entero 
                'definition_date': task.definition_date.strftime('%Y-%m-%d %H:%M:%S') if task.definition_date else None #usamos la funcion strftime para dar formato a las fechas y horas, ya que estas no pueden ser convertidas a JSON
            }
        #convertimos el diccionario en un archivo JSON legible
        datos_json = json.dumps(data, indent = 4)
        #codificamos el json para convertirlo en archivo
        archivo_json = base64.b64encode(datos_json.encode('utf-8'))
        #creamos un archivo adjunto a odoo para que pueda ser descargado y lo configuramos
        archivoAdjunto = self.env['ir.attachment'].create({
            'name': f'{task.name}.json', #nombre del archivo a descargar
            'type': 'binary',
            'datas': archivo_json,
            'res_model': 'managejoseluis.task', #modelo al que nos referimos
            'res_id': task.id, #id al que nos referimos
            'mimetype': 'application/json'
        })
        #por ultimo, devolvemos la opcion de descargar el archivo para el usuario
        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{archivoAdjunto.id}?download=true', #url de descarga
            'target':'self'
        }

    