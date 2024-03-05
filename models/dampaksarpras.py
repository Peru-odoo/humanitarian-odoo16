from odoo import models, fields

class DampakSarpras(models.Model):
    _name = "humanitarian.dampaksarpras"
    _description = 'Dampak Sarpras'

    kerusakan = fields.Char(string="Kerusakan")
    site_id = fields.Char(string="Situation")
    jumlah = fields.Integer(string="Jumlah")
    satuan = fields.Char(string="Satuan")