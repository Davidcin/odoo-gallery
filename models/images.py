# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Images(models.Model):
    _name = "gallery.images"
    _description = "Images"
    _rec_name = "img_name"

    img_name = fields.Char(string="Image Name", size = 40, required = True)
    img = fields.Binary(string="Image", required=True)
    gallery_id = fields.Many2one("gallery.gallery")
