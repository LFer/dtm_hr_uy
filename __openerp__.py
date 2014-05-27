# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#    Copyright (C) 2010-2012 OpenERP s.a. (<http://openerp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Localización de HR para Uruguay',
    'version': '1.0',
    'category': 'Human Resources',
    'description': """

Extension para localizacion de modulo recursos humanos para Uruguay
===================================================================
""",
    'author': 'Datamatic',
    'maintainer': 'Datamatic',
    'website': 'http://www.datamatic.com.uy',
    'depends': ['hr','base','account'],
    'data': ['uy_employee_view.xml','hr_locals_view.xml', 'data/bps_marital_status.xml', 'data/aportaciones_y_tipos_de_contribuyentes.xml', 'data/tipo_de_remunieracion.xml', 'data/bps_functional_link.xml', 'data/paises.xml','data/nacionalidad.xml', 'data/genero.xml', 'data/seguro_salud.xml', 'data/bajas.xml', 'data/exoneracion_de_aportes.xml', 'data/computos_especiales.xml', 'data/horas_semanales.xml', 'data/acumulacion_laboral.xml', 'data/conceptos.xml',
        'data/trabajadores_rurales.xml', 'data/trabajadores_constru.xml', 'data/relaciones_laborales.xml', 'data/naturaleza_juridica.xml', 'data/grupos_de_trabajo.xml', 'data/subgrupos_de_trabajo.xml'],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
