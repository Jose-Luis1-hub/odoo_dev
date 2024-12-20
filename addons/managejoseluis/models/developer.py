from odoo import models, fields, api

class developer(models.Model): 
    _name = 'res.partner'
    _inherit = 'res.partner'

    is_dev = fields.Boolean(string = "¿Es desarrollador?", default = "False")

    technologies = fields.Many2many('managejoseluis.technology', relation = 'developer_technologies', column1 = 'developer_id', column2 = 'technologies_id')

    @api.model
    def crearDesarrollador(self, val):
        val['is_dev'] = True
        return super(developer, self).create(val)
