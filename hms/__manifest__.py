
{
    'name': 'hospital',
    'version': '1.0',
    'summary': 'Module for patients in a hospital',
    'author': 'Marwa',
    'depends': ['base' , 'contacts'],

    'data': [
        'security/hms_security.xml',
        'security/ir.model.access.csv',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/department_view.xml',
        'views/log_history_view.xml',
        'views/res_partner_view.xml',
        'views/menus.xml',
        'report/report_patient_template.xml',
        
       
        
    ],

}
