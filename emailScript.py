import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
from datetime import datetime
import os

class UzdAtgEpastsSutitajs:
    def __init__(self, e_pasta_adrese, e_pasta_parole, smtp_serveris, smtp_ports):
        self.E_PASTA_ADRESE = e_pasta_adrese
        self.E_PASTA_PAROLE = e_pasta_parole
        self.SMTP_SERVERIS = smtp_serveris
        self.SMTP_PORTS = smtp_ports

    def sutit_uzd_epastu(self):
        sodien = datetime.now().strftime("%Y-%m-%d")

        uzd = self.iegut_uzd_no_csv()

        if uzd:
            temats = f'Uzdevumu Atgādinājums'
            saturs = f"Uzdevumi šodien ({sodien}):\n\n"
            saturs += "\n\n".join([f"Uzdevums: {uzdevums['Nosaukums']}\nApraksts: {uzdevums['Apraksts']}\nStatuss: {uzdevums['Statuss']}" for uzdevums in uzd])
            sanemejs = self.E_PASTA_ADRESE

            self.sutit_epastu(temats, saturs, sanemejs)

    def sutit_epastu(self, temats, saturs, sanemejs):
        try:
            # Iestatīt e-pasta serveri
            serveris = smtplib.SMTP(self.SMTP_SERVERIS, self.SMTP_PORTS)
            serveris.starttls()
            serveris.login(self.E_PASTA_ADRESE, self.E_PASTA_PAROLE)

            # Izveidot e-pasta saturu
            msg = MIMEMultipart()
            msg['From'] = self.E_PASTA_ADRESE
            msg['To'] = sanemejs
            msg['Subject'] = temats
            msg.attach(MIMEText(saturs, 'plain'))

            # Sūtīt e-pastu
            serveris.sendmail(self.E_PASTA_ADRESE, sanemejs, msg.as_string())
            serveris.quit()

            print("E-pasts nosūtīts veiksmīgi!")

        except Exception as e:
            print(f"Kļūda, nosūtot e-pastu: {e}")

    def iegut_uzd_no_csv(self):
        faila_nosaukums = "data.csv"

        if os.path.isfile(faila_nosaukums):
            # Nolasīt CSV failu DataFrame
            uzdevuma_dati = pd.read_csv(faila_nosaukums)

            # Iegūt šodienas uzdevumus, kuri nav atzīmēti kā "Pabeigts"
            sodien = datetime.now().strftime("%Y-%m-%d")
            uzd = uzdevuma_dati[(uzdevuma_dati['Izpildes Datums'] == sodien) & (uzdevuma_dati['Statuss'] != 'Pabeigts')].to_dict('records')

            return uzd

        else:
            print(f"CSV fails '{faila_nosaukums}' nav atrasts.")
            return []

if __name__ == "__main__":
    # Aizstāt šīs vērtības ar savu faktisko e-pasta un SMTP servera informāciju
    sutitajs = UzdAtgEpastsSutitajs(e_pasta_adrese='automatizesanaprojekts@gmail.com',
                                    e_pasta_parole='yxky ziex drzo etuo',
                                    smtp_serveris='smtp.gmail.com',
                                    smtp_ports=587)

    sutitajs.sutit_uzd_epastu()
