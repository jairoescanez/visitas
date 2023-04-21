# -*- coding : utf 8 -*-
from odoo import fields, models

class Habitacion(models.Model):
    _name = "habitacion"
    _description = "Habitaciones"

    numHabitacion = fields.Integer(required=True)
    precio = fields.Float(required=True)
    numAdultos = fields.Integer(required=True)
    numNinos = fields.Integer(required=True)