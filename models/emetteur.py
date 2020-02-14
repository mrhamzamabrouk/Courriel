# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Emetteur(models.Model):

    _name = 'courriel.emetteur'
    _rec_name='nome'
    
    nome = fields.Char(
        string='Emetteur'
    )
    