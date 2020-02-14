# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Piecej(models.Model):
    _name = 'courriel.piecej'
    _rec_name='piece_j'

    
    piece_j = fields.Binary(
        string='Pièce jointe',
    )

    
    nomf = fields.Char(
        string='Nom du fichier'
    )

    
    date_cr = fields.Date(
        string='Date de création',
        default=fields.Date.context_today,
    )
    
    date_md = fields.Date(
        string='Date de modifiction',
        default=fields.Date.context_today,
    )

    
    desc = fields.Html(
        string='Message'
    )
    
    
    courriel_id = fields.Many2one(
        string='Courriel',
        comodel_name='courriel.courrie'
    )
    
    
     