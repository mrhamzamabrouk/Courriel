# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Recepteur(models.Model):

    _name = 'courriel.recepteur'
    _rec_name='nomr'

    nomr = fields.Char(
        string='Récepteur'
    )