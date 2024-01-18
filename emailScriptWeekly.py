import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
from datetime import datetime, timedelta
import os

class UzdProgressaEpasts:
    def __init__(self, e_pasta_adrese, e_pasta_parole, smtp_serveris, smtp_ports):
        self.E_PASTA_ADRESE = e_pasta_adrese
        self.E_PASTA_PAROLE = e_pasta_parole
        self.SMTP_SERVERIS = smtp_serveris
        self.SMTP_PORTS = smtp_ports

    def sutit_progressa_eapstu(self):

        uzd = self.iegut_uzd_no_csv()

        if uzd:
            temats = 'Uzdevumu ziņojums'
            saturs = "Atjauninājums par uzdevumu progresu pēdējo divu nedēļu laikā:\n\n"
            saturs += "\n\n".join([f"{statuss}: {skaits} uzdevumi\n\n{', '.join(uzdevumi)}" for statuss, skaits, uzdevumi in uzd])
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
            uzdevumu_dati = pd.read_csv(faila_nosaukums)

            # Pārvērst 'Izpildes Datums' kolonnu uz datetime formātu
            uzdevumu_dati['Izpildes Datums'] = pd.to_datetime(uzdevumu_dati['Izpildes Datums'])

            # Aprēķināt perioda sākuma datumu (piemēram, pēdējās divas nedēļas)
            sakuma_datums = datetime.now() - timedelta(weeks=2)

            # Filtrēt uzdevumus norādītajā periodā
            filtretie_uzdevumi = uzdevumu_dati[(uzdevumu_dati['Izpildes Datums'] >= sakuma_datums) & (uzdevumu_dati['Izpildes Datums'] <= datetime.now())]

            # Aprēķināt uzdevumu skaitu un nosaukumus katra statusa grupai
            kopsavilkums = filtretie_uzdevumi.groupby('Statuss').agg(
                Skaits=pd.NamedAgg(column='Nosaukums', aggfunc='count'),
                Uzdevumi=pd.NamedAgg(column='Nosaukums', aggfunc=lambda x: ', '.join(x))
            ).reset_index()

            # Izgūt kopsavilkuma informāciju par katru statusu
            uzd = [
                (statuss, skaits, uzdevumi.split(', ')) for statuss, skaits, uzdevumi in zip(
                    kopsavilkums['Statuss'],
                    kopsavilkums['Skaits'],
                    kopsavilkums['Uzdevumi']
                )
            ]

            return uzd

        else:
            print(f"CSV fails '{faila_nosaukums}' nav atrasts.")
            return []

if __name__ == "__main__":
    # Aizstāt šīs vērtības ar savu faktisko e-pasta un SMTP servera informāciju
    sutitajs = UzdProgressaEpasts(e_pasta_adrese='',
                                    e_pasta_parole='',
                                    smtp_serveris='smtp.gmail.com',
                                    smtp_ports=587)

    sutitajs.sutit_progressa_eapstu()
