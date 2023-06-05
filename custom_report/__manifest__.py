# -*- coding: utf-8 -*-
{
    'name': 'Make Report',
    'version': '1.0.0',
    'category': 'report',
    'author': 'tony',
    'summary': 'for sale report',
    'description': 'make custom sale report',
    'depends': ['account','web'],
    'data': [
        "report/invoice_external_layout.xml",
        "report/custom_invoice_report.xml",
        "report/invoice_custom_report_action.xml",
    ],
    'demo': [],
    "assets": {
    'web.report_assets_common': [
        "custom_report/static/src/css/font.scss",
    ],
},

}