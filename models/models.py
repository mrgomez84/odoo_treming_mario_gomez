# -*- coding: utf-8 -*-

from odoo import models, fields


class treming_mario_gomez(models.Model):
    _name = 'treming_mario_gomez.treming_mario_gomez'
    _description = 'treming_mario_gomez.treming_mario_gomez'

    date = fields.Datetime(string='Fecha',use='required')
    name = fields.Char(string='Nombre del Visitante',use='required')
    value = fields.Many2one('res.partner', string='Paciente',use='required')
    description = fields.Text(use='required')

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
