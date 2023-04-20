# -*- coding: utf-8 -*-
from odoo import fields, models
class Visita(models.Model):
    _name = "visita"
    _description = "Gestor de visitas"

    fecha_entrada = fields.Datetime(required=True)
    fecha_salida = fields.Datetime(required=True)
    nombre_reserva = fields.Char(required=True)
    dni = fields.Char(required=True)
    numero_telefono = fields.Char(required=True)
    es_reserva = fields.Boolean(required=True)
    habitacion = fields.Many2one(required=True, comodel_name="habitacion")
    persona_visitada = fields.Char()
    precio = fields.Integer()