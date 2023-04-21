# -*- coding: utf-8 -*-
from odoo import fields, models
from datetime import datetime

class Visita(models.Model):
    _name = "visita"
    _description = "Gestor de visitas"

    fecha_entrada = fields.Datetime(required=True, default=datetime.now())
    fecha_salida = fields.Datetime(required=True)
    nombre_reserva = fields.Char(required=True)
    dni = fields.Char(required=True)
    numero_telefono = fields.Char(required=True)
    es_reserva = fields.Boolean(required=True, default=False)
    habitacion = fields.Many2one(required=True, comodel_name="habitacion")
    persona_visitada = fields.Char()