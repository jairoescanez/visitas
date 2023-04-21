# -*- coding: utf-8 -*-
from odoo import fields, models, api
from datetime import datetime
from odoo.exceptions import ValidationError

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

    @api.constrains("fecha_entrada","fecha_salida")
    def _check_fecha_entrada_anterior_fecha_salida(self):
        for p in self:
            if (p.fecha_entrada > p.fecha_salida):
                raise ValidationError("La fecha de entrada debe ser anterior a la fecha de salida")
