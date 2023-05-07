from odoo import http
from odoo.http import request
from odoo.addons.account.controllers import portal


class InheritPortalAccount(portal.CustomerPortal):


    @http.route(['/my/invoices/<int:invoice_id>'], type='http', auth="public", website=True)
    def portal_my_invoice_detail(self, invoice_id, access_token=None, report_type=None, download=False, **kw):
        res =super().portal_my_invoice_detail(invoice_id, access_token, report_type, download, **kw)
        print("gggggggg")
        return res
        

