# -*- coding : utf 8 -*-
from odoo import fields, models

class Habitacion(models.Model):
    _name = "habitacion"
    _description = "Habitaciones"

    num_habitacion = fields.Integer(required=True)
    precio = fields.Float(required=True)
    num_adultos = fields.Integer(required=True)
    num_ninos = fields.Integer(required=True)