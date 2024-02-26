from odoo import models, fields, api, _
from odoo.exceptions import AccessError, UserError, ValidationError


class InheritHelpDesk(models.Model):
    _inherit = 'helpdesk.ticket'
    #campos nuevos para modelo de mesa de ayuda
    area = fields.Many2one('area.segman', string="Área que reporta")
    engineer = fields.Many2one('engineer.segman', string="Ingeniero Segman")
    series = fields.Char(string="Serie")
    model = fields.Char(string="Módelo")
    location = fields.Char(string="Ubicación")
    state_final = fields.Char(string="Estado final del equipo")
    actions = fields.Char(string="Acciones realizadas")
    arrival_hour = fields.Datetime(string="Fecha y Hora de llegada")
    time_arrival = fields.Char(string="Tiempo de arribo")

    #metodo para calcular diferencia de los dias
    @api.onchange('arrival_hour')
    def _onchange_arrival_hour(self):
        #checar que tengan los campos requeridos para calculo
        if self.arrival_hour:
            if self.create_date:
                #resta de los campos
                resdate = self.create_date - self.arrival_hour
                #asignacion de valor a campo de tiempo de arribo
                self.time_arrival = resdate

    #validacion para campos requeridos en otros estados que no sea nuevo ticket
    @api.onchange('stage_id')
    def _onchange_stage_id(self):
        #checar que el estado no se el de nuevo
        if self.stage_id.name == 'Resuelto':
            #validacion de campos
            if not self.actions:
                raise UserError('Se requiere el campo Acciones realizadas')
            elif not self.state_final:
                raise UserError('Se requiere el campo Estado final del equipo')
            elif not self.time_arrival:
                raise UserError('Se requiere el campo Tiempo de arribo')
            elif not self.arrival_date:
                raise UserError('Se requiere el campo Fecha y Hora de llegada')
            elif not self.series:
                raise UserError('Se requiere el campo Serie')
            elif not self.model:
                raise UserError('Se requiere el campo Módelo')







