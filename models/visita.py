# -*- coding: utf-8 -*-
from odoo import fields, models, api
from datetime import datetime
from odoo.exceptions import ValidationError

class Visita(models.Model):
    _name = "visita"
    _description = "Gestor de visitas"

    fecha_entrada = fields.Datetime(required=True, default=datetime.now(), string="Fecha y hora de entrada")
    fecha_salida = fields.Datetime(required=True, string="Fecha y hora de salida")
    nombre_reserva = fields.Char(required=True, string="Nombre y Apellidos")
    dni = fields.Char(required=True, string="DNI")
    numero_telefono = fields.Char(required=True, string="Teléfono")
    es_reserva = fields.Boolean(required=True, default=False, string="Reserva habitación")
    habitacion = fields.Many2one(comodel_name="habitacion", string="Habitación")
    persona_visitada = fields.Char(string="Residente Visitado")

    @api.constrains("fecha_entrada","fecha_salida")
    def _check_fecha_entrada_anterior_fecha_salida(self):
        for p in self:
            if (p.fecha_entrada > p.fecha_salida):
                raise ValidationError("La fecha de entrada debe ser anterior a la fecha de salida")

    @api.onchange("es_reserva")
    def onchange(self):
        if self.es_reserva == True:
            self.persona_visitada = None
        else:
            self.habitacion = None