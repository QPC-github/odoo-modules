# -*- coding: utf-8 -*-

{
    'name': "Abandoned Carts",
    'version': '12.0.1.2',
    'depends': ['website_sale', 'crm', 'account', 'project', 'calendar', 'queue_job'],
    'description': """
- User can delete Abandoned Customers & Orders
- User can see deleted Customers or Orders log in Removed Log menu inside Sales --> Abandoned Log menu.
- Abandoned customers are identify based on customer those have no Lead/Opportunity, no Calendar Event, no Phone call, no Invoice, no Sale order, no Account move, no Project task,is customer, is inactive and that record is created with system user.
- Abandoned Orders are identify based on order those are created by system user, its status is Quotation, Sales Team is Website Sales and its create date is before order retention period.
    """,
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron.xml',
        'views/res_config_settings_views.xml',
        'views/removed_record_log_views.xml',
        'views/assets.xml',
        'wizard/sale_order_view.xml',
        'wizard/customer_view.xml',
    ],
    'author': "Nitrokey GmbH, Odoo Community Association (OCA)",
    'license': 'AGPL-3',
    'website': "https://github.com/OCA/abandoned_carts",
}
