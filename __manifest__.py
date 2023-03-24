{
    'name': "Delivery Warning",
    'version': "16.0.1",
    'sequence': -21,
    'installable': True,
    'application': True,

    'depends': ['base', 'sale','stock','sale_stock'],

    'data': [
            'views/delivery_warning_sale.xml',
             'views/delivery_warning_delivery.xml',
             'report/delivery_slip_inherit.xml'
    ]

}
