# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class EngineerSegman(models.Model):
    _name = 'engineer.segman'
    # campos para modelo de ingenieros
    name = fields.Char(string="Nombre")
    display_name = fields.Char(string="display name", compute='_compute_display_name')
    #codigo para desplegar nombre en vistas
    def _compute_display_name(self):
        for engineer in self:
            engineer.display_name = engineer.name

