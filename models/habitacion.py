# -*- coding : utf 8 -*-
from odoo import fields, models

class Habitacion(models.Model):
    _name = "habitacion"
    _description = "Habitaciones"

    num_habitacion = fields.Integer(required=True, string="Número de habitación")
    precio = fields.Float(required=True, string="Precio")
    num_adultos = fields.Integer(required=True, string="Número de adultos")
    num_ninos = fields.Integer(required=True, string="Número de niños")