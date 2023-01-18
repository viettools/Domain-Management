# -*- coding: utf-8 -*-
# Copyright (c) 2023 DUNG.CC. (https://dung.cc)

from odoo import api, fields, models, _

class DomainsExtensions(models.Model):
    _name = 'domains.extensions'
    _description = 'Domains Extensions'
    _rec_name = 'name'

    name = fields.Char(string='Domain Name', required=True)
    domain_type = fields.Selection([('infrastructure', 'Infrastructure'),
                                    ('generic', 'Generic'),
                                    ('sponsored', 'Sponsored'),
                                    ('generic-restricted', 'Generic Restricted'),
                                    ('country-code', 'Country Code')], string='Domain Type', required=True)
    tld_managers = fields.Char(string='TLD Managers', required=True)