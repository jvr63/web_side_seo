
# -*- coding: utf-8 -*-

import logging

from odoo import fields, http, tools, _
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

_logger = logging.getLogger(__name__)

class WebsiteSaleGuadalstoreProductSeo(WebsiteSale):

    @http.route()
    def product(self, product, category='', search='', **kwargs):
        """ Added ref and barcode to original response """
        res = super(WebsiteSaleGuadalstoreProductSeo, self).product(product, category, search, **kwargs)

        res.update({
            seoldjson: "{'name': 'El nombre'}"
        })

        return res
