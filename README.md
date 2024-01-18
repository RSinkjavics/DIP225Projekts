# DIP225Projekts
## Ievads
### Ievads
Mūsu projekts koncentrējas uz uzdevumu pārvaldības lietotnes izstrādi, izmantojot Python programmēšanas valodu. Šī lietotne izmanto Tkinter, lai izveidotu lietotājam draudzīgu saskarni, integrē būtiskas funkcijas ar pandas datu manipulēšanai un uzglabāšanai CSV failā, kā arī esam iekļāvuši smtplib bibliotēku ikdienas uzdevumu e-pasta ziņojumu sūtīšanai un uzdevumu progressa ziņai.
### Mērķis
Mūsu uzdevumu pārvaldības lietotnes projekta galvenais mērķis ir izveidot daudzpusīgu un intuitīvu rīku, kas vienkāršo ikdienas uzdevumu pārvaldīšanas sarežģītību.
### Apraksts
Projekts ietver uzdevumu pārvaldības lietojumprogrammu un e-pasta paziņojumu sistēmu. Uzdevumu pārvaldības lietojumprogramma ļauj lietotājiem nemanāmi izveidot, atjaunināt un pārvaldīt savus uzdevumus, izmantojot intuitīvu grafisko lietotāja interfeisu (GUI). Uzdevumi tiek pastāvīgi glabāti CSV failā, nodrošinot datu integritāti un pieejamību sesijās.
E-pasta paziņojumu sistēma automatizē atgādināšanas procesu lietotājiem par gaidāmajiem uzdevumiem un nodrošina progresa ziņojumus ar iepriekš noteiktiem intervāliem. Izmantojot smtplib bibliotēku, sistēma izveido drošu savienojumu ar SMTP serveri, lai nosūtītu e-pastus. Turklāt pandu bibliotēka tiek izmantota efektīvai datu apstrādei, ļaujot ģenerēt ieskatamus progresa ziņojumus, pamatojoties uz uzdevuma statusu un pabeigšanu.
E-pasta paziņojuma failus ir domāts palaists izmantojot "Task Scheduler" applikāciju, kas Windows datoros ir jau instalēta, uzstādot, ka tie darbojos noteiktos laikos/intervālos.
## Programmsistēmas projektējums
### Uzdevumu analīze:
1. Lietotāja interfeisa dizains ar Tkinter:
    - Izstrādāt un izveidot lietojumprogrammas galveno logu, izmantojot Tkinter.
    - Ieviest pogas un ievades laukus uzdevumu pievienošanai, rediģēšanai un dzēšanai.
    - Nodrošāt estētiski pievilcīgu dizainu.
2. Uzdevumu datu pārvaldība ar Pandas:
    - Izveidot funkcionalitāti uzdevumu datu glabāšanai un izgūšanai CSV failā/no tā.
    - Ieviest funkcionalitāti, lai pievienotu, rediģētu un dzēstu uzdevumus, izmantojot pandas.
3. Smtplib integrācija e-pasta nosūtīšanai:
    - Konfigurēt smtplib bibliotēku, lai izveidotu savienojumu ar e-pasta serveri.
    - Izveidot funkciju ikdienas uzdevumu kopsavilkumu ģenerēšanai.
    - Integrēt e-pasta funkcionalitāti, lai lietotājiem nosūtītu uzdevumu kopsavilkumus.
4. Testēšana un Atkļūdošana:
    - Veikt rūpīgu katras funkcionalitātes pārbaudi, lai nodrošinātu pareizu darbību.
    - Atkļūdojiet visas problēmas vai kļūdas, kas rodas testēšanas laikā.
5. Dokumentācija:
    - Kompilēt README failu ar projekta dokumentāciju.
### Pielietotās bibliotekas
- tkinter
    - Tkinter ir standarta Python bibliotēka grafisko lietotāja interfeisu (GUI) izveidei. 
    - Šajā kodā tas tiek izmantots, lai izveidotu galveno lietojumprogrammas logu, pogas, "labels" un citus GUI elementus.
- tkcalendar 
    - Šī bibliotēka nodrošina datuma ievades logrīku tkinter lietojumprogrammām. Tas ļauj lietotājiem viegli ievadīt un atlasīt datumus. 
    - Šajā kodā tas tiek izmantots, lai izveidotu datuma ievades lauku uzdevumu 'Izpildes Datums'.
- pandas 
    - Pandas ir jaudīga datu apstrādes un analīzes bibliotēka. 
    - Šajā kodā tas tiek izmantots tabulu datu apstrādei. Konkrēti, tas nolasa/raksta datus uz/no CSV faila, pārvalda DataFrame uzdevumu datiem un veic dažādas datu manipulācijas.
- datetime
    - Datuma un laika modulis nodrošina funkcijas darbam ar datumiem un laikiem. 
    - Šajā kodā tas tiek izmantots, lai iegūtu pašreizējo datumu un laiku, formatētu to un veiktu ar datumu saistītus aprēķinus.
- OS
    - OS moduli izmanto, lai veiktu no operētājsistēmas atkarīgas darbības, piemēram, pārbaudītu, vai fails pastāv. 
    - Šajā kodā tas tiek izmantots, lai pārbaudītu, vai fails pastāv (CSV fails), pirms mēģināt to nolasīt. Tas palīdz apstrādāt ar failiem saistītas darbības.
- smtplib
    - smtplib ir bibliotēka, kas definē SMTP (Simple Mail Transfer Protocol) klienta sesijas objektu. To izmanto e-pasta ziņojumu sūtīšanai, izmantojot SMTP protokolu. 
    - Šajā kodā tas tiek izmantots, lai izveidotu savienojumu ar SMTP serveri un nosūtītu e-pastus.
- email.mime.text
    - Šis e-pasta pakotnes modulis tiek izmantots, lai e-pastam izveidotu MIME (multipurpose Internet Mail Extensions) teksta daļu. Tas ļauj formatēt e-pasta pamattekstu kā vienkāršu tekstu.
- email.mime.multipart 
    - Šo e-pasta pakotnes moduli izmanto, lai izveidotu MIME vairāku daļu ziņojumu. Tas ļauj e-pastam pievienot vairākas daļas (tekstu, attēlus utt.). 
    - Šajā kodā tas tiek izmantots, lai pievienotu vienkārša teksta daļu, kas izveidota ar MIMEText.
### Koda funkcijas
1. main.py
    - __innit__
        - Šī metoda inicializē uzdevuma pārvaldnieka logu izmantojot Tkinter un veic šādus uzdevumus:
            - Loga konfigurācija:
                - Iestata norādīto logu kā instances atribūtu.
                - Iestata saknes loga nosaukumu "Uzdevumu pārvaldnieks".
            - Datu inicializācija:
                - Izsauc datu_inicializesana metodi, lai inicializētu uzdevuma datus. Ja CSV fails (data.csv) pastāv, tas ielādē datus; pretējā gadījumā tas izveido tukšu DataFrame.
            - GUI iestatīšana:
                - Izsauc saskarnes_izveide metodi, lai iestatītu grafisko lietotāja interfeisu, ieskaitot ievades laukus, pogas un Treeview logrīku uzdevumu attēlošanai.
            - Uzdevumu saraksta atjauninājums:
                - Izsauc atjauno_treeview metodi, lai atjauninātu uzdevumu sarakstu Treeview logrīkā.
            - Mainīgā inicializācija:
                - Inicializē gadījumu mainīgos:
                    - izv_uzd: attēlo pašlaik atlasīto uzdevumu.
                    - kart_var: Tkinter StringVar, kas pārstāv uzdevumu saraksta kārtošanas opciju, inicializēts uz 'Nekā' (nav).
                    - kart_sec_var: Tkinter StringVar, kas attēlo kārtošanas secību, inicializēts uz "Augoša" (augošā secībā).
                    - filtra_var: Tkinter StringVar, kas apzīmē filtrēšanas opciju, inicializēts uz "Visus" (visi uzdevumi).

    - datu_inicializesana
        - Šī metode inicializē lietojumprogrammas uzdevuma datus.
            - Metode pārbauda, ​​vai pastāv CSV fails, kurā ir uzdevuma dati. Ja tas pastāv, tas ielādē datus DataFrame (uzd_dati). Ja nē, tas izveido tukšu DataFrame ar iepriekš definētiem kolonnu nosaukumiem, kas kalpo kā sākotnējā struktūra uzdevuma datiem.
    - saskarnes_izveide
        - Šī metode iestata lietojumprogrammas Task Manager grafisko lietotāja interfeisu un veic šādus uzdevumus:
            - Inicializē mainīgos priekšs uzdevuma nosaukuma, apraksta un datuma ievades.
            - Izsauc metodes (ievades_lauki, datuma_ievade), lai izveidotu ievades laukus.
            - Izveido uzdevuma saglabāšanas pogu un saista ar save_uzd metodi.
            - Izveido Treeview logrīku, lai attēlotu uzdevumu sarakstu ar noteiktām kolonnām.
            - Saista hand_treeview_click metodi ar peles kreisās pogas atlaišanu Treeview, ļaujot lietotājam atlasīt uzdevumus.
            - Izveido pogu atlasīto uzdevumu statusa atjaunināšanai un saista to ar atjauno_statusu metodi.
            - Izveido pogu atlasīto uzdevumu dzēšanai un saista to ar izdzest_uzd metodi.
            - Izveido pogu uzdevumu filtrēšanai un kārtošanai un saista to ar filtru_popup metodi.
            - Izveido "label" ziņojumu parādīšanai lietotājam.
            - Ievieto ziņojuma "label" noteiktā GUI vietā.
    - ievades_lauki
        - Šī metode izveido lietotāja ievadei "label" un ievades lauku.
            - Metode dinamiski izveido "label" un ievades lauku lietotāja ievadei, pamatojoties uz sniegto tekstu. "Label" apraksta ievades mērķi, un ievades lauks ļauj lietotājam ievadīt atbilstošus datus.
    - datuma_ievade
        - Šī metode lietotāja ievadei izveido "label" un datuma ievades lauku.
            - Metode dinamiski izveido "label" un datuma ievades lauku lietotāja ievadei. "Label" apraksta ievades mērķi, un datuma ievades lauks ļauj lietotājam izvēlēties datumu, izmantojot logrīku "DateEntry" no tkcalendar.
    - parada_pazin
        - Šī metode lietotājam GUI parāda ziņojumu.
            - Metode atjaunina ziņojuma "label" ar doto ziņojumu un krāsu. Tas arī ieplāno ziņojuma notīrīšanu pēc noteikta laika.
    - atjauno_treeview
        - Šī metode atjaunina Treeview logrīku ar jaunākajiem uzdevuma datiem.
            - Metode notīra esošo Treeview logrīka saturu un aizpilda to ar jaunākajiem uzdevuma datiem no DataFrame (self.uzd_dati). Katra uzdevuma informācija tiek parādīta jaunā koka skatījuma rindā. Notīrīšana un aizpildīšana notiek ar "for" cikliem, notīrīšanas gadijumā iet cauri visām Treeview rindām, bet aizpildīšanā iet cauri visiem ierakstiem uzd_dati.
    - handle_treeview_click
        - Šī metode apstrādā Treeview logrīka klikšķa notikumu.
            - Metode tiek aktivizēta, kad lietotājs Treeview logrīkā noklikšķina uz rindas. Tas identificē atlasīto vienumu un, ja klikšķis nebija uz kolonnas Statuss, saglabā atlasītās preces ID mainīgajā self.izv_uzd vēlākai lietošanai.
    - atjauno_izv_uzd
        - Šī metode atjaunina atlasītā uzdevuma statusu ar jaunu statusu, veic šādus uzdevumus:
            - Pārbauda, ​​vai DataFrame kolonnā 'Nosaukums' ir izvēlētā uzdevuma nosaukums, ja uzdevuma nosaukums nav atrasts, tiek parādīts kļūdas ziņojums, kas norāda, ka uzdevums nav atrasts.
            - Ja uzdevuma nosaukums tiek atrasts, atjaunina DataFrame kolonnu 'Statuss' ar jauno statusu (new_status). Izmanto loc metodi, lai atrastu konkrēto rindu, kurā atbilst uzdevuma nosaukums.
            - Ieraksta atjaunināto DataFrame CSV failā.
            - Izsauc atjauno_treeview_filtretu metodi, lai atjauninātu Treeview logrīku ar pašreizējiem datiem, ņemot vērā visus lietotos filtrus vai kārtošanu.
            - Parāda lietotājam ziņojumu, kas norāda, ka uzdevuma statuss ir atjaunināts. Ziņojums tiek rādīts uz noteiktu laiku.
    - atjauno_statusu
        - Šī metode tiek izsaukta, ja lietotājs vēlas atjaunināt atlasītā uzdevuma statusu, veic šādus uzdevumus:
            - Pārbauda, ​​vai it atlasīts kāds uzdevums.
            - Iegūst atlasītā uzdevuma ID no Treeview logrīka.
            - Iegūst atlasītā uzdevuma vērtības no Treeview logrīka.
            - No vērtībām izvelk atlasītā uzdevuma pašreizējo statusu.
            - Izveido jaunu augstākā līmeņa logu statusa atjaunināšanai.
                - Parāda uzdevuma esošo statusu.
                - Parāda izvēlni ar statusu opcijām.
                - Ievieto apstiprināšanas pogu, kura izsauc apst_statusu.
    - apst_statusu
        - Šī metode tiek izsaukta, kad lietotājs apstiprina jaunā statusa atlasi, veic šadus uzdevumsu:
            - Pārbauda, ​​vai ir atlasīts uzdevums (saglabāts self.izv_uzd), ja uzdevuma nosaukums nav atrasts, tiek parādīts kļūdas ziņojums, kas norāda, ka uzdevums nav atrasts.
            - Iegūst atlasītā uzdevuma vērtības no Treeview logrīka.
            - Izvelk no vērtībām atlasītā uzdevuma nosaukumu.
            - Pārbauda, ​​vai DataFrame (self.uzd_dati) kolonnā 'Nosaukums' ir atlasītais uzdevuma nosaukums.
            - Izsauc atjauno_izv_uzd metodi, lai atjauninātu atlasītā uzdevuma statusu ar jauno statusu.
            - atiestata atribūtu, kurā tiek saglabāts atlasītais uzdevums, uz "none".
            - iznīcina (aizver) jaunā statusa izvēles logu.
    - izdzest_uzd
        - Šī metode tiek izsaukta, ja lietotājs vēlas dzēst atlasīto uzdevumu, veic sādus uzdevumus:
            - Pārbauda, ​​vai ir atlasīts uzdevums (saglabāts self.izv_uzd).
            - Iegūst atlasītā uzdevuma ID no Treeview logrīka.
            - Iegūst atlasītā uzdevuma vērtības no Treeview logrīka.
            - No vērtībām izvelk atlasītā uzdevuma nosaukumu.
            - Pārbauda, ​​vai DataFrame (self.uzd_dati) kolonnā 'Nosaukums' ir atlasītais uzdevuma nosaukums, ja atlasītais uzdevums nav atrasts, lietotājam tiek parādīts kļūdas ziņojums.
            - Izdzēš atlasīto uzdevumu no DataFrame, izveidojot jaunu DataFrame.
            - Ieraksta atjaunināto DataFrame CSV failā, ko norāda self.DATI.
            - Izsauc atjauno_treeview_filtretu metodi, lai atjauninātu Treeview logrīku ar pašreizējiem datiem, ņemot vērā visus lietotos filtrus vai kārtošanu.
            - atiestata atribūtu, kurā tiek saglabāts atlasītais uzdevums, uz "none".
            - Parāda lietotājam ziņojumu, kas norāda, ka uzdevums ir dzēsts. Ziņojums tiek rādīts uz noteiktu laiku.
    - save_uzd
        - Šī metode tiek izsaukta, ja lietotājs vēlas saglabāt jaunu uzdevumu, veic šādus uzdevumus:
            - Iegūst pašreizējo datumu un laiku norādītajā formātā.
            - Iegūst vērtības no nosaukuma_var, apraksts_var, izp_dat_var,  kuros ir lietotāja ievadītie uzdevuma dati.
            - Pārbauda, ​​vai ir aizpildīti visi nepieciešamie lauki (uzdevuma nosaukums, apraksts un termiņš), ja kāds no obligātajiem laukiem nav aizpildīts, lietotājam tiek parādīts kļūdas ziņojums.
            - Izveido jaunu DataFrame (new_uzd) ar informāciju par jauno uzdevumu, izveides datumu, nosaukumu, aprakstu, termiņu un sākotnējo statusu 'Nav sākas'.
            - Savieno esošos uzdevuma datus (self.uzd_dati) ar jaunā uzdevuma (new_uzd) datiem. Parametrs ignore_index=True nodrošina DataFrame indeksa atiestatīšanu.
            - Ieraksta atjaunināto DataFrame CSV failā.
            - Izsauc atjauno_treeview metodi, lai atjauninātu Treeview logrīku ar pašreizējiem datiem.
            - Maina uzdevuma nosaukumam, aprakstam un termiņam mainīgo vērtības uz tukšām virknēm.
            - Parāda lietotājam ziņojumu, kas norāda, ka uzdevums ir saglabāts. Ziņojums tiek rādīts uz noteiktu laiku.
    - filtru_popup
        - Šī metode tiek izsaukta, ja lietotājs vēlas atvērt logu filtrēšanas un kārtošanas opcijām, veic šādus uzdevumus:
            - Izveido jaunu augstākā līmeņa logu filtrēšanas un kārtošanas opcijām.
            - Iestata loga nosaukumu uz "Filtrēt/kārtot uzdevumus".
            - Definē pieejamās kārtošanas, kārtošanas secības un filtrēšanas opcijas.
            - Izveido un ievieto nolaižamo izvēlni (Combobox) kārtošanas un filtrēšanas atlasei.
            - Logam pievieno pogu, lai apstiprinātu atlasīto filtru un kārtošanas opcijas. Noklikšķinot uz šīs pogas, tiek izsaukta metode pielietot_filtrus.
    - pielietot_filtrus
        - Šī metode tiek izsaukta, kad lietotājs noklikšķina uz pogas "Apstiprināt" filtra un kārtošanas logā, veic šādus uzdevumus:
            - Pirms izmaiņu piemērošanas, iegūst pašreizējās kārtošanas kritēriju vērtības, kārtošanas secību un filtru.
            - Izveido sākotnējo DataFrame (self.uzd_dati) kopiju, lai lietotu filtrus un kārtotu, nemainot sākotnējos datus.
            - Pārbauda, ​​vai ir atlasīts kārtošanas kritērijs un tas nav iestatīts uz 'Nekā'.
                - Nosaka, vai kārtošanas secība ir augoša, pamatojoties uz lietotāja atlasi.
                - Kārto kopēto DataFrame, pamatojoties uz atlasītajiem kārtošanas kritērijiem un secību.
            - Pārbauda, ​​vai ir atlasīts cits filtra kritērijs, nevis 'Visus'.
                - Filtrē DataFrame, lai iekļautu tikai uzdevumus ar atlasīto statusu.
            - Izsauc atjauno_treeview_filtretu metodi, lai atjauninātu Treeview logrīku ar filtrētajiem un sakārtotajiem datiem.
            - Aizver filtru un kārtošanas logu.
    - atjauno_treeview_filtretu
        - Šī metode tiek izsaukta, lai atjauninātu Treeview logrīku ar filtrētiem un sakārtotiem uzdevuma datiem, veic šādus uzdevumus:
            - Ar "for" ciklu iet cauri visiem Treeview ierakstiem.
                - Izdzēš katru ierakstu
            - Ar "for" ciklu iet cauri visām DataFrame rindām.
                - Iegūst uzdevuma datus (nosaukums, apraksts, termiņš, statuss) no pašreizējās rindas DataFrame.
                - Treeview ievieto jaunu vienumu ar iegūtajiem uzdevuma datiem.
    - beigu "if __name__ == "__main__":"
        - Pārbauda, ​​vai skripts tiek palaists tieši (nav importēts kā modulis).
        - Izveido galveno Tkinter logu (sakni) uzdevumu pārvaldības lietojumprogrammai.
        - Definē galvenā loga sākotnējo izmēru uz 838 pikseļu platumu un 398 pikseļu augstumu.
        - Konfigurē galvenā loga fona krāsu gaiši pelēkā krāsā (#e6e6e6).
        - Izveido klases TaskManagerApp gadījumu, kā argumentu nododot galveno Tkinter logu.
        - Sāk Tkinter ciklu, kas ļauj lietojumprogrammai reaģēt uz lietotāja mijiedarbību. Šī rinda būtībā palaiž lietojumprogrammu, un programma turpinās darboties, līdz lietotājs aizver galveno logu.
2. emailScript.py
    - __innit__
        - Šī ir klases inicializācijas metode (konstruktors).
        - Inicializē instances mainīgos (SMTP_PORTS, E_PASTA_PAROLE, SMTP_SERVERIS, E_PASTA_ADRESE) ar dotajām vērtībām
    - sutit_uzd_epastu
        - Šī metode sūta atgādinājuma e-pasta ziņojumu par šodien ieplānotajiem uzdevumiem, veic šādus uzdevumus:
            - Iegūst pašreizējo datumu formātā "GGGG-MM-DD" un saglabā to mainīgajā sodien.
            - Izsauc metodi iegut_uzd_no_csv, lai izgūtu šodienas uzdevumus no CSV faila.
            - Pārbauda, ​​vai šodien ir uzdevumi.
                - Iestata e-pasta tematu kā 'Uzdevumu Atgādinājums'.
                - Inicializē e-pasta saturu ar galveni, kas norāda šodienas datumu.
                - Izveido virkni ar uzdevuma informāciju, tostarp nosaukumu, aprakstu un statusu, katram izgūtajam uzdevumam.
                - Iegūst adresāta e-pasta adresi.
                - Izsauc metodi sutit_epastu, lai nosūtītu e-pasta ziņojumu ar norādīto tēmu, saturu un adresātu.
    - sutit_epastu
        - Šī metode nosūta e-pasta ziņojumu ar norādīto tēmu, saturu un adresātu, veic šādus uzdevumus:
            - Definē mēģinājuma bloku, lai apstrādātu iespējamos izņēmumus e-pasta sūtīšanas procesā.
                - Izveido SMTP servera savienojumu, izmantojot norādīto SMTP servera adresi un portu.
                - Uzsāk drošu savienojumu ar serveri, izmantojot TLS.
                - Piesakās e-pasta serverī ar norādīto e-pasta adresi un paroli.
                - Izveido MIMEMultipart gadījumu, lai izveidotu e-pasta ziņojumu.
                - Iestata e-pasta 'From' adresi.
                - Iestata e-pasta "To" adresi uz adresāta e-pasta adresi.
                - Iestata e-pasta tēmu.
                - E-pasta ziņojumam pievieno "plain" teksta saturu.
                - Nosūta e-pastu, izmantojot sendmail metodi, norādot sūtītāju, adresātu un e-pasta ziņojumu kā virkni.
                - Izdrukā veiksmes ziņojumu konsolei.
            - Uztver visus izņēmumus, kas varētu rasties e-pasta sūtīšanas procesa laikā.
                - Izdrukā kļūdas ziņojumu un konkrēto notikušo izņēmumu.
    - iegut_uzd_no_csv
        - Šī metode izgūst uzdevumus no CSV faila, veic šādus uzdevumus:
            - Norāda CSV faila nosaukumu ("data.csv"), kas satur uzdevuma datus.
            - Pārbauda, ​​vai norādītajā ceļā pastāv CSV fails, ja CSV fails neeksistē, izdrukā kļūdas ziņojumu, kas norāda, ka CSV fails nav atrasts un atgriež tukšu sarakstu, jo nav izgūstamu uzdevumu.
                - Ja fails pastāv, nolasa CSV failu Pandas DataFrame ar nosaukumu uzdevuma_dati.
                - Iegūst pašreizējo datumu formātā "GGGG-MM-DD" un saglabā to mainīgajā sodien.
                - Filtrē šodienas uzdevumus, kas nav atzīmēti kā 'Pabeigts'.
                - Atgriež šodienas uzdevumu sarakstu.
    - beigu "if __name__ == "__main__":"
        - Izveido klases UzdAtgEpastsSutitajs instanci.
        - Konstruktors (__init__ metode) tiek izsaukts ar sniegto e-pasta un SMTP servera informāciju.
        - Izsauc metodi sutit_uzd_epastu izveidotajā UzdAtgEpastsSutitajs klases instancē.
3. emailScriptWeekly.py
    - Visas metodes ir gandrīz vienādas kā "emailScript.py", izņemot iegut_uzd_no_csv.
    - iegut_uzd_no_csv
        - Šī metode izgūst uzdevumus no CSV faila, veic šādus uzdevumus:
            - Norāda CSV faila faila nosaukumu.
            - Pārbauda, ​​vai CSV fails pastāv.
            - Nolasa CSV failu Pandas DataFrame.
            - Pārvērš kolonnu "Izpildes Datums" datuma un laika formātā.
            - Aprēķina perioda sākuma datumu
            - Filtrē uzdevumus norādītajā periodā.
            - Apkopo uzdevumus pēc statusa, aprēķinot skaitu un apvienotos nosaukumus.
            - Izveido sarakstu, kas satur katra statusa statusu, skaitu un uzdevumu nosaukumu.
            - Atgriež sarakstu ar uzdevumiem, kas attēlo uzdevumu kopsavilkumus norādītajā periodā, vai tukšu sarakstu, ja CSV fails nav atrasts.
### Testēšana
- Lietotnes testēšanu veicām aktīvi, strādājot pie tās izstrādes. Pirms veicām izmaiņas un saglabāju tās, mēs pārbaudīju, vai viss darbojas kā iepriekš. Šīs pārbaudes palīdzēja novērst jebkādas kļūdas un saglabāt lietotnes stabilitāti.
- Vērts minēt, ka lietotne nav testēta ar lielu datu apjomu, tādēļ nav zināms vai neradīsies nekādi veikstpējas tracuējumu aplikācijā.
## Izmantotās literatūras un datu avotu saraksts
- https://realpython.com/python-send-email/
- https://www.geeksforgeeks.org/python-gui-tkinter/
- https://www.youtube.com/watch?v=Cv3FsAUDyos&t=1525s
- https://www.jcchouinard.com/python-automation-using-task-scheduler/

