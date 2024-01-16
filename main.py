import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import pandas as pd
from datetime import datetime
import os

class TaskManagerApp:
    DATI = "data.csv"
    ILGUMS = 3000

    def __init__(self, root):
        self.root = root
        self.root.title("Uzdevumu pārvaldnieks")

        self.datu_inicializesana()

        self.saskarnes_izveide()

        self.atjauno_treeview()

        self.statusa_izvelne()

        self.izv_uzd = None
        self.kart_var = tk.StringVar(value='Nekā')
        self.kart_sec_var = tk.StringVar(value='Augoša')
        self.filtra_var = tk.StringVar(value='Visus')

    def datu_inicializesana(self):
        if os.path.isfile(self.DATI):
            self.uzd_dati = pd.read_csv(self.DATI)
        else:
            self.uzd_dati = pd.DataFrame(columns=['Izveides Datums', 'Nosaukums', 'Apraksts', 'Izpildes Datums', 'Statuss'])

    def statusa_izvelne(self):
        self.statuss_menu = tk.Menu(self.root, tearoff=0)
        satusu_opcijas = ['Pending', 'Hold', 'Completed', 'Failed']
        for option in satusu_opcijas:
            self.statuss_menu.add_command(label=option, command=lambda s=option: self.atjauno_statusu(s))

    def saskarnes_izveide(self):
        self.nosaukums_var = tk.StringVar()
        self.apraksts_var = tk.StringVar()
        self.izp_dat_var = tk.StringVar()

        self.ievades_lauki("Nosaukums:", 0, 0)
        self.ievades_lauki("Apraksts:", 1, 0)
        self.datuma_ievade("Izpildes Datums:", 2, 0)

        ttk.Button(self.root, text="Saglabāt uzdevumu", command=self.save_uzd).grid(row=3, column=0, columnspan=2, pady=10)

        self.uzd_treeview = ttk.Treeview(self.root, columns=('Nosaukums', 'Apraksts', 'Izpildes Datums', 'Statuss'), show='headings')
        self.uzd_treeview.grid(row=4, column=0, columnspan=2, pady=10, sticky=tk.W + tk.E)

        self.uzd_treeview.heading('Nosaukums', text='Nosaukums')
        self.uzd_treeview.heading('Apraksts', text='Apraksts')
        self.uzd_treeview.heading('Izpildes Datums', text='Izpildes Datums')
        self.uzd_treeview.heading('Statuss', text='Statuss')

        self.uzd_treeview.bind('<ButtonRelease-1>', self.handle_treeview_click)

        ttk.Button(self.root, text="Atjaunot Statusu", command=self.atjauno_statusu).grid(row=5, column=0, pady=10)
        ttk.Button(self.root, text="Izdzēst", command=self.izdzest_uzd).grid(row=5, column=1, pady=10)
        ttk.Button(self.root, text="Filtrēt/Kārtot", command=self.filtru_popup).grid(row=6, column=0, columnspan=2, pady=10)

        self.pazinojums = ttk.Label(self.root, text="", foreground="red")
        self.pazinojums.grid(row=0, column=1, pady=10)

    def ievades_lauki(self, inp_teksts, row, column):
        label = ttk.Label(self.root, text=inp_teksts)
        label.grid(row=row, column=column, padx=5, pady=5, sticky=tk.W)

        inp_nosaukums = f"{inp_teksts.strip(':').lower().replace(' ', '_')}_var"
        ievade = ttk.Entry(self.root, textvariable=getattr(self, inp_nosaukums))
        ievade.grid(row=row, column=column + 1, padx=5, pady=5, sticky=tk.W)

    def datuma_ievade(self, inp_teksts, row, column):
        label = ttk.Label(self.root, text=inp_teksts)
        label.grid(row=row, column=column, padx=5, pady=5, sticky=tk.W)

        kalendara_ievade = DateEntry(self.root, textvariable=self.izp_dat_var, date_pattern="y-mm-dd")
        kalendara_ievade.grid(row=row, column=column + 1, padx=5, pady=5, sticky=tk.W)

    def parada_pazin(self, zina, duration=ILGUMS):
        self.pazinojums.config(text=zina, foreground="green")
        self.root.after(duration, lambda: self.pazinojums.config(text=""))

    def atjauno_treeview(self):
        for item in self.uzd_treeview.get_children():
            self.uzd_treeview.delete(item)

        for index, row in self.uzd_dati.iterrows():
            uzd_dati = (row['Nosaukums'], row['Apraksts'], row['Izpildes Datums'], row['Statuss'])
            self.uzd_treeview.insert('', tk.END, values=uzd_dati, tags=('Statuss',))

    def handle_treeview_click(self, event):
        if not self.uzd_treeview.selection():
            return

        item_id = self.uzd_treeview.selection()[0]
        kolonna = self.uzd_treeview.identify_column(event.x)

        if kolonna == '#4':
            pass
        else:
            self.izv_uzd = item_id

    # Atjaunot atlasīto uzdevumu ar jauno statusu
    def atjauno_izv_uzd(self, name, new_status):
        if name in self.uzd_dati['Nosaukums'].values:
            self.uzd_dati.loc[self.uzd_dati['Nosaukums'] == name, 'Statuss'] = new_status
            self.uzd_dati.to_csv(self.DATI, index=False)
            self.atjauno_treeview_filtretu(self.uzd_dati)  # Update with the current data
            self.parada_pazin(f"Uzdevuma '{name}' statuss atjaunots.", duration=self.ILGUMS)
        else:
            self.parada_pazin(f"Uzdevums '{name}' nav atrasts.", duration=self.ILGUMS)

    def atjauno_statusu(self):
        if self.izv_uzd is not None:
            izv_rinda = self.izv_uzd
            values = self.uzd_treeview.item(izv_rinda, 'values')
            current_statuss = values[3]

            popup = tk.Toplevel(self.root)
            popup.title("Atajunot Statusu")

            ttk.Label(popup, text=f"Šobrīdējais statuss: {current_statuss}").pack(pady=5)

            izv_statuss = tk.StringVar()
            for option in ['Nav sākts', 'Progresā', 'Aizturēts', 'Nepabeigts', 'Pabeigts']:
                ttk.Radiobutton(popup, text=option, variable=izv_statuss, value=option).pack()

            apst_poga = ttk.Button(popup, text="Apstiprināt", command=lambda: self.apst_statusu(izv_statuss.get(), popup))
            apst_poga.pack(pady=10)

    def apst_statusu(self, new_status, popup):
        if self.izv_uzd is not None:
            izv_rinda = self.izv_uzd
            values = self.uzd_treeview.item(izv_rinda, 'values')
            atjaunojamais_uzd = values[0]

            if atjaunojamais_uzd in self.uzd_dati['Nosaukums'].values:
                self.atjauno_izv_uzd(atjaunojamais_uzd, new_status)
                self.izv_uzd = None
                popup.destroy()
            else:
                self.parada_pazin(f"uzdevums '{atjaunojamais_uzd}' nav atrasts.", duration=self.ILGUMS)

    # Izdzēst izvēlēto uzdevumu
    def izdzest_uzd(self):
        if self.izv_uzd is not None:
            izv_rinda = self.izv_uzd
            values = self.uzd_treeview.item(izv_rinda, 'values')
            uzd_name = values[0]

            if uzd_name in self.uzd_dati['Nosaukums'].values:
                self.uzd_dati = self.uzd_dati[self.uzd_dati['Nosaukums'] != uzd_name]
                self.uzd_dati.to_csv(self.DATI, index=False)
                self.atjauno_treeview_filtretu(self.uzd_dati)  # Atjauno ar esošajiem datiem
                self.izv_uzd = None
                self.parada_pazin(f"Uzdevums izdzēsts: {uzd_name}", duration=self.ILGUMS)
            else:
                self.parada_pazin(f"Uzdevums '{uzd_name}' nav atrasts.", duration=self.ILGUMS)

    def save_uzd(self):
        sdn_datums = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        nosaukums = self.nosaukums_var.get()
        apraksts = self.apraksts_var.get()
        izp_dat = self.izp_dat_var.get()

        if nosaukums and apraksts and izp_dat:
            new_uzd = pd.DataFrame({'Izveides Datums': [sdn_datums], 'Nosaukums': [nosaukums], 'Apraksts': [apraksts],
                                     'Izpildes Datums': [izp_dat], 'Statuss': ['Nav sākts']})
            self.uzd_dati = pd.concat([self.uzd_dati, new_uzd], ignore_index=True)
            self.uzd_dati.to_csv(self.DATI, index=False)

            self.atjauno_treeview()

            self.nosaukums_var.set('')
            self.apraksts_var.set('')
            self.izp_dat_var.set('')

            self.parada_pazin("Uzdevums saglabāts!", duration=self.ILGUMS)
        else:
            self.parada_pazin("Lūdzu aizpildīt visus laukus pirms saglabašanas.", duration=self.ILGUMS)

    def filtru_popup(self):
        popup = tk.Toplevel(self.root)
        popup.title("Filtrēt/kārtot uzdevumus")

        ttk.Label(popup, text="Kārtot pēc:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        kart_opc = ['Nekā', 'Nosaukums', 'Izpildes Datums', 'Statuss']
        kart_izv = ttk.Combobox(popup, textvariable=self.kart_var, values=kart_opc)
        kart_izv.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(popup, text="Kārtošanas secība:").grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
        kart_sec_opc = ['Augoša', 'Dilstoša']
        kart_sec_izv = ttk.Combobox(popup, textvariable=self.kart_sec_var, values=kart_sec_opc)
        kart_sec_izv.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)

        ttk.Label(popup, text="Filtrēt:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        filtru_opc = ['Visus', 'Nav sākts', 'Progresā', 'Aizturēts', 'Nepabeigts', 'Pabeigts']
        filtru_izv = ttk.Combobox(popup, textvariable=self.filtra_var, values=filtru_opc)
        filtru_izv.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Button(popup, text="Apstiprināt", command=lambda: self.pielietot_filtrus(popup, self.kart_var.get(), self.kart_sec_var.get(), self.filtra_var.get())).grid(row=2, column=0, columnspan=4, pady=10)

    def pielietot_filtrus(self, popup, kartot, kartot_sec, filtrs):
        current_kart = self.kart_var.get()
        current_kart_sec = self.kart_sec_var.get()
        current_filtrs = self.filtra_var.get()

        filtretie_dati = self.uzd_dati.copy()

        if kartot and kartot != 'Nekā':
            augosa_sec = (kartot_sec == 'Augoša')
            filtretie_dati.sort_values(by=[kartot], inplace=True, ascending=augosa_sec)

        if filtrs != 'Visus':
            filtretie_dati = filtretie_dati[filtretie_dati['Statuss'] == filtrs]

        self.atjauno_treeview_filtretu(filtretie_dati)

        self.kart_var.set(current_kart)
        self.kart_sec_var.set(current_kart_sec)
        self.filtra_var.set(current_filtrs)

        popup.destroy()


    def atjauno_treeview_filtretu(self, filtretie_dati):
        for item in self.uzd_treeview.get_children():
            self.uzd_treeview.delete(item)

        for index, row in filtretie_dati.iterrows():
            uzd_dati = (row['Nosaukums'], row['Apraksts'], row['Izpildes Datums'], row['Statuss'])
            self.uzd_treeview.insert('', tk.END, values=uzd_dati, tags=('Statuss',))

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("810x480")
    root.configure(bg="#5E4352")
    app = TaskManagerApp(root)
    root.mainloop()
