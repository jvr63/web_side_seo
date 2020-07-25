
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
        res = super(WebsiteSaleGuadalstoreProductInfo, self).product(product, category, search, **kwargs)

        ldjson='<script type="application/ld+json">{}</script>'
        pos = res.find("</head>")
        if pos > 0:
            res = res[:pos] + ldjson + res[pos:]

        return res
