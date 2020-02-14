# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Collab(models.Model):
    _name = 'courriel.collab'
    _rec_name='emailc'

    
    collabd = fields.Char(
        string='Nom'
    )

    emailc = fields.Char(
        string='E-mail'
    )
    