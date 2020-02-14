# -*- coding: utf-8 -*-
import datetime
from datetime import date
from datetime import time
from datetime import datetime, timedelta


from odoo import api, fields, models

class Courriel(models.Model):
    _name = 'courriel.courrie'



    label = fields.Char(
        string='Libellé',
        # required=True
    )

    flag = fields.Boolean(
        string='',
        default=False
    )
    

    def accept(self):
        flag = True


    
    stat_bar = fields.Selection(
        string='Etat de courriel',
        selection=[ ('3', 'Brouillon'), ('2', 'Transmis'), ('4', 'Refuse'), ('5', 'Accepte')],
        default='3'
    )

    @api.one
    def refuse(self):
        self.stat_bar='4'
        self.flag = False
        efrom = "hmabrouk373@gmail.com"
        password = ""
        mailsto = 'hmabrouk373+secretaire@gmail.com'
        Subject = "Refuser (Responsable a refuse ce courrier)" 
        body = "Ce courrier ({}) est refuser par le responsable.".format(self.label)
        self.SendMail(efrom,password,mailsto,Subject,body)
        print "Refus"

    @api.one
    def change_stat(self):
            self.stat_bar='5'
            self.flag = True
            efrom = "hmabrouk373@gmail.com"
            password = ""
            mailsto = 'hmabrouk373+secretaire@gmail.com'
            Subject = "Ce courrier a ete accepter. (Responsable a accepte le courrier)" 
            body = "Ce courrier ({}) est maintenant valable et a ete accepter, veuillez de l'envoyer le plus tot possible.".format(self.label)
            self.SendMail(efrom,password,mailsto,Subject,body)
            print "Ce courrier valable"
        # elif self.stat_bar=='2':
        #     self.stat_bar='3'
    
    @api.one
    def are_stat(self):
            self.stat_bar='3'
            self.flag = False
            efrom = "hmabrouk373@gmail.com"
            password = ""
            mailsto = 'hmabrouk373+secretaire@gmail.com'
            Subject = "A revoir. (Responsable a envoye le courrier pour le verifier)" 
            body = "Veuillez de verifier ce courrier ({}) une autre fois, et de le me transmettre.".format(self.label)
            self.SendMail(efrom,password,mailsto,Subject,body)
            print "A revoir"

    @api.one
    def transmet(self):
        self.stat_bar='2'
        efrom = "hmabrouk373@gmail.com"
        password = ""
        mailsto = 'hmabrouk373+Responsble@gmail.com'
        Subject = "Courrier Transmis. (Secretaire a transmis le courrier)" 
        body = "Veuillez de verifier ce courrier ({}) et de l'accepter.".format(self.label)
        self.SendMail(efrom,password,mailsto,Subject,body)
        print 'Transmettre'

            

    

    type_c = fields.Selection(
        string='Type',
        selection=[('1', u'Telephone'), ('2', u'Email'), ('3', u'Compte rendu'), ('4', u'Lettre'), ('5', u'Lettre Recommandee')],
        # required=True
    )

    degree_c = fields.Selection(
        string="Degree d'importance",
        selection=[('1', u'Faible'), ('2', u'Moyen'), ('3', u'Important'), ('4', u'Urgent')],
        # required=True
    )

    
    date_c = fields.Date(
        string='Date',
        default=fields.Date.context_today,
        # required=True
    )

    
    desc_msg = fields.Html(
        string='Description/Message',
    )
    
    
    piecej = fields.One2many(
        string='Pièce jointe',
        comodel_name='courriel.piecej',
        inverse_name='courriel_id'
    )
    
    emett= fields.Many2one(
        string='Emetteur',
        comodel_name='courriel.collab',
        # required=True
    )

    recep = fields.Many2one(
        string='Récepteur',
        comodel_name='courriel.collab',
        # required=True
    )

    
    ech_date = fields.Date(
        string="Date de l'échéance",
        default=fields.Date.context_today,
        # required=True
    )
    
    rappel = fields.Selection(
        string='Rappel (jours)',
        selection=[('3', '3'), ('7', '7'), ('15', '15')],
        # required=True
    )

    
    collabb = fields.Many2many(
        string='Collaborateurs désignés',
        comodel_name='courriel.collab',
        # required=True
    )

    rec_em = fields.Many2one(
        string='Récepteur',
        comodel_name='courriel.collab',
        # required=True
    )

    em_rec = fields.Many2one(
        string='Emetteur',
        comodel_name='courriel.collab',
        # required=True
    )

    exmails = fields.Many2many(
        string='Emails Externes',
        comodel_name='courriel.exmail'
    )

    # def pro(self): # method of this model
    #     print("oooooooooooooooooooooooooooooooooooooooooooooooo")


    def process_demo_scheduler_queue(self):
        days=[0 ,3, 7, 15]
        print("TESTOOOOOOOOOOOOOooooooooo")
        # efrom = "hmabrouk373@gmail.com"
        # password = ""
        # mailsto = "h.mabrouk373@gmail.com"
        # Subject = "Objet" 
        # body = 'self.desc_msg'
        # self.SendMail(efrom,password,mailsto,Subject,body)
        for courrie in self.env['courriel.courrie'].search([]):
            for day in days:
                if day <= courrie.rappel:
                    print 'testtttgsgsgsgsgqggg&&&&&&&&&&éééééééééééééééééééé'
                    datemaj = datetime.strptime(courrie.date_c, '%Y-%m-%d')+timedelta(days=int(day))
                    if  datemaj.strftime('%Y-%m-%d') == courrie.ech_date :
                        print 'rah dkhaaaaaaaaaaaaaaaaaaaaaaaaaaal'
                        for collabo in courrie.collabb:
                            efrom = "hmabrouk373@gmail.com"
                            password = ""
                            mailsto = collabo.emailc
                            Subject = "Objet" 
                            body = courrie.desc_msg
                            self.SendMail(efrom,password,mailsto,Subject,body)
                        for exmails in courrie.exmails:
                            efrom = "hmabrouk373@gmail.com"
                            password = ""
                            mailsto = exmails.exmail
                            Subject="Objet" 
                            body = courrie.desc_msg
                            self.SendMail(efrom,password,mailsto,Subject,body)

        
    def SendMail(self,efrom,password,to,Subject,body):
        import smtplib
        from email.MIMEMultipart import MIMEMultipart
        from email.MIMEText import MIMEText
        msg = MIMEMultipart()
        msg['From']= efrom
        msg['To']= to
        msg['Subject']= Subject
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.ehlo()
        server.login(efrom,password)
        server.sendmail(efrom,to,msg.as_string())
        server.close()
        return True

    @api.one
    def printt(self):
        efrom = "hmabrouk373@gmail.com"
        password = ""
        mailsto = 'hmabrouk373+Responsble@gmail.com'
        Subject = "Courrier Envoye (Secretaire a envoye le courrier)" 
        body = "Ce courrier ({}) a ete envoyer.  (Secretaire a envoye le courrier)".format(self.label)
        self.SendMail(efrom,password,mailsto,Subject,body)
        days=[0 ,3, 7, 15]
        for day in days:
            if day <= self.rappel:
                print 'testtttgsgsgsgsgqggg&&&&&&&&&&éééééééééééééééééééé'
                datemaj = datetime.strptime(self.date_c, '%Y-%m-%d')+timedelta(days=int(day))
                if  datemaj.strftime('%Y-%m-%d') == self.ech_date :
                    print 'rah dkhaaaaaaaaaaaaaaaaaaaaaaaaaaal'
                    for collabo in self.collabb:
                        efrom = "hmabrouk373@gmail.com"
                        password = ""
                        mailsto = collabo.emailc
                        Subject = "Objet (email collaborateur)" 
                        body = self.desc_msg
                        self.SendMail(efrom,password,mailsto,Subject,body)
                    for exmails in self.exmails:
                        efrom = "hmabrouk373@gmail.com"
                        password = ""
                        mailsto = exmails.exmail
                        Subject="Objet (email externe)"
                        body = self.desc_msg
                        self.SendMail(efrom,password,mailsto,Subject,body)

        print 'Envoyer'
    
