# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Exmail(models.Model):
    _name = 'courriel.exmail'
    _rec_name='exmail'

    
    exmail = fields.Char(
        string='Adresse email'
    )
    
    