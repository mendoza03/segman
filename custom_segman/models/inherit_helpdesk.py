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
    arrival_date = fields.Datetime(string="Fecha de llegada")
    arrival_hour = fields.Datetime(string="Hora de llegada")
    time_arrival = fields.Char(string="Tiempo de arribo")

    #metodo para calcular diferencia de los dias
    @api.onchange('arrival_date')
    def _onchange_arrival_date(self):
        #checar que tengan los campos requeridos para calculo
        if self.arrival_hour:
            if self.create_date:
                #resta de los campos
                resdate = self.create_date - self.arrival_hour
                #asignacion de valor a campo de tiempo de arribo
                self.time_arrival = resdate
                print('resDAte', resdate.days)


    @api.onchange('arrival_hour')
    def _onchange_arrival_hour(self):
        if self.arrival_date:
            if self.create_date:
                resdate = self.create_date - self.arrival_hour
                self.time_arrival = resdate
                print('resDAte2', resdate.days)

    #validacion para campos requeridos en otros estados que no sea nuevo ticket
    @api.onchange('stage_id')
    def _onchange_stage_id(self):
        #checar que el estado no se el de nuevo
        if self.stage_id.sequence != 0:
            #validacion de campos
            if not self.actions:
                raise UserError('Se requiere el campo acciones realizadas')







