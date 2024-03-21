# -*- coding: utf-8 -*-
{
    'name': "Gymcore",

    'summary': "Module custom of gymcore",

    'description': """
Custom views, models and add new function and fields-
    """,

    'author': "Dooers",
    'website': "https://dooers.odoo.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'gymcore',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
         #view
        'views/res_partner_view.xml',
        'views/product_template_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

