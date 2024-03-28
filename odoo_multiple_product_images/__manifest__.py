# -*- coding: utf-8 -*-
{
    'name': "Multiple Images",
    'summary': """
        Multiple Images and Categories on Products""",
    'description': """
        Creates an image gallery section available on every product and also on the product templates.
    """,
    'author': "Alliantum",
    'website': "https://www.alliantum.com/",
    'category': 'Inventory',
    'license': 'AGPL-3',
    'version': '17.0',
    'depends': ['product', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'data/clean_orphans_images.xml',
        'views/product_image_backend.xml',
        
    ],
    'assets': {
        'web.assets_backend': [
            #'odoo_multiple_product_images/static/src/js/*.js',
            'odoo_multiple_product_images/static/src/scss/multiple_images.scss',
        ],
    },
}
