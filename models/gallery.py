# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Gallery(models.Model):
    _name = "gallery.gallery"
    _description = "Gallery"
    _rec_name = 'title'

    title = fields.Char(string='Title', size=20, required=True)
    img_ids = fields.One2many("gallery.images", "gallery_id", string="Image")

    _sql_constraints = [
        ('title_unique',
         'unique(title)',
         'This gallery already exists!')
    ]