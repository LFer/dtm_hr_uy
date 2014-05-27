# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2004 TINY SPRL. (http://tiny.be) All Rights Reserved.
# Fabien Pinckaers
#

from openerp.osv import osv, fields

class hr_company_uy(osv.osv):

    _inherit = 'res.company'
    _columns={
        'contribution_id':fields.many2one('hr.uy.bps.contributions.and.taxpayer.type', 'Type of contribution'),
        'taxpayer_id':fields.many2one('hr.uy.bps.contributions.and.taxpayer.type','Type of taxpayer'),
        'exemption_of_contribution':fields.many2one('hr.uy.bps.exemption.of.contribution', 'Exemption of contributcion'),
        'legal_nature':fields.many2one('hr.uy.bps.legal.nature', 'Legal nature'),
        'locals':fields.one2many('hr.locals', 'company_id'),
        'rut_id':fields.integer('RUT number',size=15),
        'police_section':fields.integer('Police section',size=3),
        'judicial_section':fields.char('Judicial section',size=30),
        'bps_id':fields.char('BPS number',size=30),
        'bse_id':fields.char('BSE number',size=30),
        'main_activity':fields.char('Main activity',size=30),
        'mtss_id':fields.char('MTSS number', size=30),
        'mtss_group':fields.many2one('hr.uy.mtss.working.groups','MTSS group'),
        'mtss_sub_group':fields.many2one('hr.uy.mtss.working.subgroups', 'MTSS subgroup'),
        'collective_agreement':fields.char('Collective agreement',size=30),
        'collective_agreement_expiration_date':fields.date('Expiry date of contract'),
        'start_date_of_activity':fields.date('Start date of activity'),
        'payment_calendar':fields.char('Payment schedule',size=30),
        'commerce_service':fields.boolean('Trade or service'),
        'bulk_sales':fields.boolean('Wholesale'),
        'retail_sales':fields.boolean('Retail sale'),
        'industry':fields.boolean('Industry'),
        'industry_inputs':fields.char('Main raw materials used'),
        'industry_outputs':fields.char('Main line of products made'),
        'transport':fields.boolean('Transportation'),
        'terrestrial_transport':fields.selection([('U','Urban'),('C','Cargo'),('D','Interdepartamental'),('P','Passengers'),('I','Internaional')],'Type of work'),
        'construction':fields.boolean('Construction'),
        'construction_architecture':fields.boolean('Architecture work'),
        'construction_engineering':fields.boolean('Engineering Work'),
        'construction_masonry_and_concrete':fields.boolean('Concrete and masonry'),
        'subcontracting':fields.char('Subcontract'),
        }


class hr_employee_uy(osv.osv):

    _inherit = 'hr.employee'
    #hackish
    def onchange_names(self, cr, uid, ids,first_name,second_name,first_surname,second_surname,birthday,context=None):
        #pdb.set_trace()
        name = ""
        if not birthday:
            return { 'value' : { 'name' : name , 'autogen_name' : 'Completar Fecha de Nacimiento'}}
        autogen = "" + birthday[2] + birthday[3] + birthday[5] + birthday[6] + birthday [8] + birthday[9] + " "

        for s in [first_surname,second_surname,first_name,second_name]:
            if s:
                autogen = autogen + s[0]
        name = first_name

        for s in [second_name,first_surname,second_surname]:
            if s:
                name = name + u' ' + s
        #self.write(cr, uid, ids, { 'name' : name }, context=context)
        return { 'value' : { 'name' : name , 'autogen_name' : autogen}}

    def generate_name(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for line in self.browse(cr,uid,ids,context=context):
            res[line.id]=line.name
        return res

    _columns = {

        'name_gen':fields.function(generate_name,type='char',method=True,string='Hack'),
        'family':fields.one2many('hr.employee.family','employee_id','Familirares'),
        #datos basicos
        'employee_number':fields.char('Employee number',size=10),
        'country_of_birth':fields.many2one('hr.uy.bps.country','Contry of birth'),
        'country_of_id':fields.many2one('hr.uy.bps.country','Country of document'),
        'credential':fields.char('Polling card',size=10),
        'first_surname':fields.char('First surname',size=20),
        'second_surname':fields.char('Second surname',size=20),
        'first_name':fields.char('First name', size=20),
        'second_name':fields.char('Second name', size=20),

        #datos laborales
        'date_hired':fields.date('Date of admission'),
        'date_fired':fields.date('Date of leaving'),
        'date_job_start':fields.date('In office since'),
        'pay_type':fields.selection([('M','Monthly'),('W','Working day')],'Type of work'),

        #pestania forma de pago
        'payment_method':fields.selection([('C','Cash'),('P','Paycheck'),('D','Deposit to account')],'Method of payment'),
        'account_type':fields.selection([('C','Checking account'),('S','Savings bank'),(' ','Others')],'Account tipe'),
        'account_number':fields.char('Account number',size=30),
        'account_bank':fields.many2one('res.bank',"Bank of account"),

        #pestania salud
        'health_card_id':fields.char('Health cad ID',size=15),
        'health_card_expiration_date':fields.date('Expiration date'),
        'health_care_provider':fields.char('Health care provider',size=20),
        'health_care_provider_user_id':fields.char('Associate ID',size=20),
        'emergency_health_care_provider':fields.char('Medical emergency',size=20),
        'emergency_health_care_provider_user_id':fields.char('Associated ID',size=20),

        #bps
        'autogen_name':fields.char('Selfgenerated',size=12),
        'work_timetable':fields.many2one('hr.uy.hours.per.week','Hour'),
        'termination_code':fields.many2one('hr.uy.bps.termination','Termnation code'),
        'bps_category_type':fields.selection([('1','General category'),('2','Rural worker'),('3','Contruction worker')],'Type of category',required=True),
        'bps_category_general':fields.many2one('hr.uy.bps.category','Category'),
        'bps_category_construction':fields.many2one('hr.uy.bps.category.construction','Contruction worker category'),
        'bps_category_rural':fields.many2one('hr.uy.bps.category.rural','Rural worker category'),
        'bps_category_date':fields.date('Category date'),
        'bps_type_of_remuneration':fields.many2one('hr.uy.bps.type.of.remuneration','Type of remunaration'),
        'bps_functional_link':fields.many2one('hr.uy.bps.functional.link','Functional link'),
        'bps_labor_relations':fields.many2one('hr.uy.bps.labor.relations','Labor relations'),
        'bps_health_insurance':fields.many2one('hr.uy.bps.health.insurance','Healt insurance'),
        'mtss_sheet':fields.integer('MTSS Sheet',size=3)
    }

    _sql_constraints = [
        ('credential_unique', 'unique(credential)', 'Ya existe un empleado con la credencial ingresada!'),
        ('employee_number_unique', 'unique(employee_number)', 'Ya existe un empleado con el numero de empleado ingresado!')]

hr_employee_uy()

class hr_employee_family(osv.osv):
    _name = "hr.employee.family"
    _columns = {
        'first_surname':fields.char('First surname',size=20,required=True),
        'second_surname':fields.char('Second surname',size=20,required=True),
        'employee_id':fields.many2one('hr.employee','Associated employee',select=True),
        'first_name':fields.char('First name', size=20,required=True),
        'second_name':fields.char('Second name', size=20),
        'gender': fields.many2one('hr.uy.bps.gender', 'Gender'),
        'date_of_birth':fields.date('Date of birth'),
        'kinship':fields.char('Kinship', size=20),
        'country_of_birth':fields.many2one('hr.uy.bps.country','Contry of birth', size=20),
        'nationality':fields.many2one('hr.uy.bps.nationality','Nationality', size=20),
        'address_home_id':fields.many2one('res.partner', 'Adress', size=20),
        'document_type':fields.many2one('hr.uy.document.type','Type of document'),
        'country_id':fields.many2one('hr.uy.bps.country', 'Contry of document', size=20),
        'id_number':fields.char('Document id', size=20),
        'polling_card':fields.char('Polling card', size=20),




    }

hr_employee_family ()


class hr_locals(osv.osv):
    _name = "hr.locals"
    _columns = {
        'company_id':fields.many2one('res.company', 'Main company'),
        'local_id':fields.char('Local', size=20),
        'local_description':fields.char('Description', size=20),
    }


hr_locals()

class hr_department_uy(osv.osv):
    _inherit='hr.department'
    _columns={
        'section_ids':fields.one2many('hr.section','department_id','Sections')
    }

hr_department_uy()

class section (osv.osv):
    _name="hr.section"
    _columns={
        'department_id':fields.many2one('hr.department', 'Department'),
        'section':fields.integer('Section',size=5),
        'desc_seccion':fields.char('Description of section', size=20)
    }
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['department_id','section','desc_seccion'], context=context)
        res = []
        for record in reads:
            #in case there is no description, don't use it or type error will pop
            description = record['desc_seccion']
            if not description:
                description = 'No descr'
            res.append((record['id'],u'' + record['department_id'][1] + u' - Section ' + str(record['section']) + u' - ' + description))
        return res

section()

class bps_contributions_and_taxpayer_type(osv.osv):
    _description = "Contributions and taxpayer type"
    _name="hr.uy.bps.contributions.and.taxpayer.type"
    _columns= {
        'contribution_code':fields.char('Código de aportación', size=3),
        'description_of_contribution':fields.char('Descripcíon de aportación', size=50),
        'code_type_of_taxpayer':fields.char('Código de tipo de contribuyente', size=3),
        'description_of_type_of_taxpayer':fields.char('Descrición de tipo decontribuyente', size=50),
    }

    def __get_truncated_descr(self,description):
        if len(description) > 20:
            return description[0:19] + '...'
        else:
            return description
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['contribution_code','code_type_of_taxpayer','description_of_contribution'], context=context)
        res = []
        for record in reads:
            #in case there is no description, don't use it or type error will pop
            description = record['description_of_contribution']
            if not description:
                description = 'No descr'
            else:
                description = self.__get_truncated_descr(description)
            res.append((record['id'],u'Code ' + str(record['contribution_code']) + u' - ' + str(record['code_type_of_taxpayer']) + u' - ' + description))
        return res

bps_contributions_and_taxpayer_type()

class bps_type_of_remuneration(osv.osv):
    _description = "Type of remuneration"
    _name="hr.uy.bps.type.of.remuneration"
    _columns= {
        'remuneration_code':fields.integer('Remuneration code', size=3),
        'description_of_remuneration':fields.char('Description of remuneration', size=50),
    }
    def __get_truncated_descr(self,description):
        if len(description) > 20:
            return description[0:19] + '...'
        else:
            return description
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['remuneration_code','description_of_remuneration'], context=context)
        res = []
        for record in reads:
            #in case there is no description, don't use it or type error will pop
            description = record['description_of_remuneration']
            if not description:
                description = 'No descr'
            else:
                description = self.__get_truncated_descr(description)
            res.append((record['id'],u'' + str(record['remuneration_code']) + u' - ' + description))
        return res

bps_type_of_remuneration()

class bps_functional_link(osv.osv):
    _description = "Vinculo funcional"
    _name= "hr.uy.bps.functional.link"
    _columns= {
        'functional_code_link':fields.integer('Functional link code', size=3),
        'functional_code_description':fields.char('Functional link description', size=50),
    }
    def __get_truncated_descr(self,description):
        if len(description) > 20:
            return description[0:19] + '...'
        else:
            return description
        def name_get(self, cr, uid, ids, context=None):
            if not ids:
                return []
            reads = self.read(cr, uid, ids, ['functional_code_link','functional_code_description'], context=context)
            res = []
            for record in reads:
                #in case there is no description, don't use it or type error will pop
                description = record['functional_code_description']
                if not description:
                    description = 'No descr'
                else:
                    description = self.__get_truncated_descr(description)
                res.append((record['id'],u'' + str(record['functional_code_link']) + u' - ' + description))
            return res

bps_functional_link()

class bps_country(osv.osv):
    _description = "Country"
    _name= "hr.uy.bps.country"
    _columns= {
        'country_id':fields.char('Country', size=56),
        'country_code':fields.char('Country code',size=33),
    }
bps_country()

class bps_gender(osv.osv):
    _description="Sexo"
    _name="hr.uy.bps.gender"
    _columns={
        'gender':fields.char('Gender', size=10),#selection([('M', 'Male'),('F','Female')],'Gender', size=10),
        'gender_id':fields.integer('Gender code', size=1),
    }
    """
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
            reads = self.read(cr, uid, ids, ['gender'], context=context)
            res = []
            for record in reads:
                res.append((record['id'],u'' + str(record['gender']) ))
            return res
            """
bps_gender()

class bps_nationality(osv.osv):
    _description= "Nationality"
    _name= "hr.uy.bps.nationality"
    _columns= {
        'nationality_code':fields.integer('Nationality code', size=1),
        'nationality_description':fields.char('Nationality description', size=50),
    }
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['nationality_description'], context=context)
        res = []
        for record in reads:
            res.append((record['id'],u'' + str(record['nationality_description']) ))
        return res
bps_nationality()

class bps_marital_status(osv.osv):
    _description= "Marital status"
    _name= "hr.uy.bps.marital.status"
    _columns= {
        'marital_status_code':fields.integer('Marital status code', size=2,required=True),
        'marital_status_description':fields.char('Marital status description', size=50),
    }
    def __get_truncated_descr(self,description):
        if len(description) > 20:
            return description[0:19] + '...'
        else:
            return description
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['marital_status_code','marital_status_description'], context=context)
        res = []
        for record in reads:
           #in case there is no description, don't use it or type error will pop
            description = record['marital_status_description']
            if not description:
                description = 'No descr'
            else:
                description = self.__get_truncated_descr(description)
            res.append((record['id'],u'' + str(record['marital_status_code']) + u' - ' + description ))
        return res

bps_marital_status()

class bps_health_insurance(osv.osv):
    _description= "Health insurance"
    _name= "hr.uy.bps.health.insurance"
    _columns= {
        'health_insurance_code':fields.integer('Health insurance code', size=3),
        'health_insurance_description':fields.char('Health insurance description', size=100),
    }

    def __get_truncated_descr(self,description):
        if len(description) > 20:
            return description[0:19] + '...'
        else:
            return description
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['health_insurance_code','health_insurance_description'], context=context)
        res = []
        for record in reads:
            #in case there is no description, don't use it or type error will pop
            description = record['health_insurance_description']
            if not description:
                description = 'No descr'
            else:
                description = self.__get_truncated_descr(description)
            res.append((record['id'],u'' + str(record['health_insurance_code']) + u' - ' + description ))
        return res

bps_health_insurance()

class bps_termination(osv.osv):
    _description= "Terminations"
    _name= "hr.uy.bps.termination"
    _columns= {
        'termination_code':fields.integer('Termination code', size=3),
        'termination_description':fields.char('Description of termination', size=40),
    }

    def __get_truncated_descr(self,description):
        if len(description) > 20:
            return description[0:19] + '...'
        else:
            return description
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['termination_code','termination_description'], context=context)
        res = []
        for record in reads:
            #in case there is no description, don't use it or type error will pop
            description = record['termination_description']
            if not description:
                description = 'No descr'
            else:
                description = self.__get_truncated_descr(description)
            res.append((record['id'],u'Termination Code ' + str(record['termination_code']) + u' - ' + description))
        return res

bps_termination()

class bps_exemption_of_contribution(osv.osv):
    _description= "Exemption of contribution"
    _name= "hr.uy.bps.exemption.of.contribution"
    _columns= {
        'exemption_code':fields.integer('Exemption code', size=3),
        'exemption_description':fields.char('Description of exemption', size=50),
    }

    def __get_truncated_descr(self,description):
        if len(description) > 20:
            return description[0:19] + '...'
        else:
            return description
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['exemption_code','exemption_description'], context=context)
        res = []
        for record in reads:
            #in case there is no description, don't use it or type error will pop
            description = record['exemption_description']
            if not description:
                description = 'No descr'
            else:
                description = self.__get_truncated_descr(description)
            res.append((record['id'],u'Excemption Code ' + str(record['exemption_code']) + u' - ' + description))
        return res
bps_exemption_of_contribution()

class bps_special_computing(osv.osv):
    _description= "Special computing"
    _name= "hr.uy.bps.special.computing"
    _columns= {
        'computing_code':fields.integer('Computing code', size=3),
        'computing_description':fields.char('Computing description', size=100),
    }
    def __get_truncated_descr(self,description):
        if len(description) > 20:
            return description[0:19] + '...'
        else:
            return description
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['computing_code','computing_description'], context=context)
        res = []
        for record in reads:
            #in case there is no description, don't use it or type error will pop
            description = record['computing_description']
            if not description:
                description = 'No descr'
            else:
                description = self.__get_truncated_descr(description)
            res.append((record['id'],u'Special computing code' + str(record['computing_code']) + u' - ' + description))
        return res

bps_special_computing()

class bps_hours_per_week(osv.osv):
    _description= "Hours per week"
    _name= "hr.uy.hours.per.week"
    _columns= {
        'hour':fields.integer('Hours', size=2,required=True),
    }
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['hour'], context=context)
        res = []
        for record in reads:
            res.append((record['id'],u'Horas: ' + str(record['hour'])))
        return res
bps_hours_per_week()

class bps_accumulation_labor(osv.osv):
    _description= "Accumulation labor"
    _name= "hr.uy.accumulation.labor"
    _columns= {
        'acumulation_code':fields.integer('Accumulation code', size=1),
        'acumulation_description':fields.char('Accumunlation description', size=50),
    }
    def __get_truncated_descr(self,description):
        if len(description) > 20:
            return description[0:19] + '...'
        else:
            return description
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['acumulation_code','acumulation_description'], context=context)
        res = []
        for record in reads:
            #in case there is no description, don't use it or type error will pop
            description = record['acumulation_description']
            if not description:
                description = 'No descr'
            else:
                description = self.__get_truncated_descr(description)

            res.append((record['id'],u'Acumulation code' + str(record['acumulation_code']) + u' - ' + description))
        return res

bps_accumulation_labor()

class bps_concept(osv.osv):
    _description= "Concept"
    _name= "hr.uy.bps.concept"
    _columns= {
        'concept_code':fields.integer('Concept code', size=3),
        'concept_description':fields.char('Concept description', size=220),
    }
    def __get_truncated_descr(self,description):
        if len(description) > 20:
            return description[0:19] + '...'
        else:
            return description
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
                return []
        reads = self.read(cr, uid, ids, ['concept_code','concept_description'], context=context)
        res = []
        for record in reads:
            #in case there is no description, don't use it or type error will pop
            description = record['concept_description']
            if not description:
                description = 'No descr'
            else:
                description = self.__get_truncated_descr(description)
            res.append((record['id'],u'Concept ' + str(record['concept_code']) + u' - ' + description))
        return res

bps_concept()

class bps_category_rural(osv.osv):
    _description= "Rural workers"
    _name= "hr.uy.bps.category.rural"
    _columns= {
        'worker_code':fields.integer('Worker code', size=3),
        'concept_description':fields.char('Concept description', size= 256),
        'worker_group':fields.char('Group'),
    }

bps_category_rural()

class bps_category(osv.osv):
    _description= "Worker category"
    _name= "hr.uy.bps.category"
    _columns= {
        'category_code':fields.integer('Code', size=5),
        'category_description':fields.char('Category description', size=20),
    }
    def __get_truncated_descr(self,description):
        if len(description) > 20:
            return description[0:19] + '...'
        else:
            return description
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['category_code','category_description'], context=context)
        res = []
        for record in reads:
            #in case there is no description, don't use it or type error will pop
            description = record['category_description']
            if not description:
                description = 'No descr'
            else:
                description = self.__get_truncated_descr(description)

            res.append((record['id'],u'Category ' + str(record['category_code']) + u' - ' + description))
        return res

bps_category()

class bps_category_construction(osv.osv):
    _description= "Contruction workers"
    _name= "hr.uy.bps.category.construction"
    _columns= {
        'code':fields.char('Code', size=300),
        'category':fields.char('Category', size=2000),
        'type_of_income':fields.char('Type of income', size=10),
    }
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['category','code'], context=context)
        res = []
        for record in reads:
            res.append((record['id'],u'Category ' + record['category'] + u' - Code ' + str(record['code'])))
        return res

bps_category_construction()

class bps_labor_relations(osv.osv):
    _description= "Labor relations"
    _name= "hr.uy.bps.labor.relations"
    _columns= {
        'code_of_labor_relation':fields.integer('Labor relation code', size=3),
        'description_of_labor_relation':fields.char('Labor relation description', size=50),
    }

    def __get_truncated_descr(self,description):
        if len(description) > 20:
            return description[0:19] + '...'
        else:
            return description
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['code_of_labor_relation','description_of_labor_relation'], context=context)
        res = []
        for record in reads:
            #in case there is no description, don't use it or type error will pop
            description = record['description_of_labor_relation']
            if not description:
                description = 'No descr'
            else:
                description = self.__get_truncated_descr(description)
            res.append((record['id'],u'' + str(record['code_of_labor_relation']) + u' - ' + description))
        return res

bps_labor_relations()

class bps_legal_nature(osv.osv):
    _description= "Legal nature"
    _name= "hr.uy.bps.legal.nature"
    _columns= {
        'code_of_legal_nature':fields.integer('Legal nature code', size=3),
        'description_of_legal_nature':fields.char('Legal nature description', size=50),
    }
    def __get_truncated_descr(self,description):
        if len(description) > 20:
            return description[0:19] + '...'
        else:
            return description
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['code_of_legal_nature','description_of_legal_nature'], context=context)
        res = []
        for record in reads:
            #in case there is no description, don't use it or type error will pop
            description = record['description_of_legal_nature']
            if not description:
                description = 'No descr'
            else:
                description = self.__get_truncated_descr(description)
            res.append((record['id'],u'' + str(record['code_of_legal_nature']) + u' - ' + description))
        return res
bps_legal_nature()

class mtss_working_groups(osv.osv):
    _description= "Working groups"
    _name= "hr.uy.mtss.working.groups"
    _columns= {
        'group':fields.integer('Group', size=3),
        'description':fields.char('Description', size=100),
    }
    def __get_truncated_descr(self,description):
        if len(description) > 20:
            return description[0:19] + '...'
        else:
            return description
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['group','description'], context=context)
        res = []
        for record in reads:
            #in case there is no description, don't use it or type error will pop
            description = record['description']
            if not description:
                description = 'No descr'
            else:
                description = self.__get_truncated_descr(description)
            res.append((record['id'],u'Mtss group ' + str(record['group']) + u' - ' + description))
        return res

mtss_working_groups()

class mtss_working_subgroups(osv.osv):
    _description= "Working subgroups"
    _name= "hr.uy.mtss.working.subgroups"
    _columns= {
            'subgroup':fields.integer('Subgroup', size=3),
            'group':fields.integer('Group', size=3),
            'description':fields.char('Description', size=50),
                }
    def __get_truncated_descr(self,description):
        if len(description) > 20:
            return description[0:19] + '...'
        else:
            return description
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['subgroup','description'], context=context)
        res = []
        for record in reads:
            #in case there is no description, don't use it or type error will pop
            description = record['description']
            if not description:
                description = 'No descr'
            else:
                description = self.__get_truncated_descr(description)

            res.append((record['id'],u'Mtss subgroup ' + str(record['subgroup']) + u' - ' + description))
        return res

mtss_working_subgroups()

class hr_uy_category(osv.osv):
    _description="Category"
    _name="hr.uy.category"
    _columns={
        'category_code':fields.integer('Category code', size=5),
        'category_id':fields.char('Category description', size=50),
    }
    def __get_truncated_descr(self,description):
        if len(description) > 20:
            return description[0:19] + '...'
        else:
            return description
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['category_code','category_id'], context=context)
        res = []
        for record in reads:
            #in case there is no description, don't use it or type error will pop
            description = record['category_id']
            if not description:
                description = 'No descr'
            else:
                description = self.__get_truncated_descr(description)

            res.append((record['id'],u'Category ' + str(record['category_code']) + u' - ' + description))
        return res
hr_uy_category()

class hr_uy_positions(osv.osv):
    _description="Positions"
    _name="hr.uy.positions"
    _columns={
        'position_code':fields.integer('Position code', size=5),
        'position_id':fields.char('Position description', size=50),
        'mtss_code':fields.integer('MTSS code', size=3),
            }
hr_uy_positions()

class hr_uy_document_type(osv.osv):
    _description="Document type"
    _name="hr.uy.document.type"
    _columns={
        'document_id':fields.char('Document id'),
        'document_description':fields.char('Document description'),
                    }
    _sql_constraints = [
                 ('document_unique', 'unique(document_id)', 'document identifiers must be unique')]


hr_uy_document_type()


