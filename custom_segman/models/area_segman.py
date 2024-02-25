# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class AreaSegman(models.Model):
    _name = 'area.segman'
    #campos para modelo de area
    name = fields.Char(string="Nombre")
    display_name = fields.Char(string="display name", compute='_compute_display_name')
    #codigo para desplegar nombre en vistas
    def _compute_display_name(self):
        for area in self:
            area.display_name = area.name
