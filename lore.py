from ast import Break
from tkinter import*


class lore():
    def __init__(self) -> None:
        super().__init__()
        self.game=False
        self.drugi_akt=False
        self.trzeci_atk=False
        self.game1=False
        self.kop=False
        self.ryczerz=False
        self.stoliki=True
        self.fina=True
        self.sklep=True
        self.pong_W=False
        self.pong_L=False
        self.ff=True
    def zero(self):
        print('*'*200 )
        print("\nBudzisz się z bolącą głową i 5 złotymi monetami w kieszeni")
        print("Powoli mroczki przed twoimi oczami zaczynają znikać i odzyskujesz kontrolę nad swoim ciałem, więc postanawiasz wstać i rozejrzeć się dookoła\n")
        print('*'*200 )

    def one(self,gracz):
        s=True
        while s:
            print("\nRozmasowując własną głowę, dostrzegasz swoje trzy możliwe opcje:\nA. Wejść do jaskini po twojej lewej z lekko migającym światełkiem na końcu\nB. Podejść do mężczyzny w czerwonych ubraniach podrzucającego piłeczkę od ping ponga\nC. Podejść do klifu\n")
            x=input()
            if x.lower()=='a':
                print('*'*200 )
                print(" Wchodząc w głąb jaskini dostrzegasz co stanowi źródło światła, święcący kot.\nStworzenie jednak po dostrzeżeniu cie chowa się od razu do mniejszej nory do której wiesz że się nie zmieścisz.\nZirytowanx tupasz mocno nogą, a stalaktyt spada ci na głowę\n")        
                gracz.hp-=1
                print(f"życie {gracz.hp}")
            elif x.lower()=='b':
                print('*'*200 )
                print("\nWItaj przyjacielu, jak się trzymasz?")
                print("ty - Gdzie jestem?")
                print('*'*200 )
                print(" \n”Hmmm Myślę, że miejsce to można nazwać tym co wy ludzie znacie jako czyściec.\nMusisz tutaj się sprawdzić w dziedzinie jaką wybrałeś sobie jako swoją filozofię za życia by dostać się do raju.”-Mężczyzna chowa piłkę do kieszeni.\n")
                print('*'*200 )
                while True:
                    print("W międzyczasie może zainteresuję cię mały zakład w papier, kamień, nożyce?”\n")
                    print("A. Możemy zagrać ")
                    if gracz.int>=2:
                            print("B. Chwila ja zginąłem? W jaki sposób????")
                    x=input()
                    if x.lower()=='b'and gracz.int>=2:
                        print('*'*200 )
                        print("\n ”Haha czy to ważne? Pewnie starx, brzydkx i samotnx jak wszyscy inni.\nI co najgorsze niezdecydowanx, a w tym miejscu to cecha która przyniesie ci zagładę.\nRadzę ci zostać tutaj i pomyśleć nad swoją przeszłością.”\n")
                    elif x.lower()=='a':
                        print('*'*200 )
                        print("\n“Wspaniale! Jak mniemam zasady już znasz.”\nMężczyzna wyciąga swoją rękę i zaczyna odliczać: “trzy, czte-RY!” instynktownie wybierasz:")
                        break
                    else:
                        print('Wybierz poprawną akcję')
                while True:
                    x=input("A. Papier\nB. Kamień\nC. Nożyce\n")
                    if x.lower()=='a':
                        print("\nSpoglądasz na dłoń mężczyzny z wyciągniętymi palcami: wskazującym i środkowym. Nożyce. “Hah nieźle”.\nZrezygnowanx dajesz mu jedną ze swoich monet.\n")
                        if gracz.int>=1:
                            print("Gdyby tylko istniało jakieś racjonalne wyjaśnienie dlaczego każdy wybór mężczyzny jest praktycznie komputerowo wykalkulowany.\nZ rozbolałą od porażki głową odchodzisz.\n")
                        gracz.coins-=1
                        print(f"stan konat {gracz.coins}")
                        break
                    elif x.lower()=='b':
                        print("\nSpoglądasz na dłoń mężczyzny otwrta w powitalnym geście. Papier. . “Hah nieźle”.\nZrezygnowanx dajesz mu jedną ze swoich monet.\n")
                        if gracz.int>=1:
                            print("\nGdyby tylko istniało jakieś racjonalne wyjaśnienie dlaczego każdy wybór mężczyzny jest praktycznie komputerowo wykalkulowany.\nZ rozbolałą od porażki głową odchodzisz.\n")
                        gracz.coins-=1
                        print(f"stan konat {gracz.coins}")
                        break
                    elif x.lower()=='c':
                        print("\nSpoglądasz na złożoną a pięść. dłoń mężczyzny. Kamień. . “Hah nieźle”.\nZrezygnowanx dajesz mu jedną ze swoich monet.\n")
                        if gracz.int>=1:
                            print("\nGdyby tylko istniało jakieś racjonalne wyjaśnienie dlaczego każdy wybór mężczyzny jest praktycznie komputerowo wykalkulowany.\nZ rozbolałą od porażki głową odchodzisz.\n")
                        gracz.coins-=1
                        print(f"stan konat {gracz.coins}")
                        break
                    else:
                        print('Wybierz poprawną akcję')
            elif x.lower()=='c':
                print('*'*200 )
                print("\nPodchodzisz do klifu i spoglądasz w dół.\nGęste chmury skrywające podłoże każą Ci sądzić, że znajdujesz się bardzo wysoko.\nDo głowy przychodzą Ci wyłącznie dwie opcje\n")
                print("A.Skocz\nB. Bezpiecznie Odsuń się od krawędzi\n\n")
                x=input()
                if x.lower()=='a':
                    self.drugi_akt=True
                    s=False
                elif x.lower()=='b':
                    print("\nZ rozbolała od wysokości głową wolnym krokiem odchodzisz od klifu do miejsca w którym się obudziłeś\n")
                else:
                    print('Wybierz poprawną akcję')
            else:
                print('Wybierz poprawną akcję')

    def two(self,gracz):
        print('*'*200 )
        print("Budzisz się z uczuciem przetrzepywania kieszeni.\nOtwierasz oczy i dostrzegasz młodszego człowieka klękającego nad tobą.\nZauważa on twoje przebudzenie i szykuje się do odskoku.\n")
        x=input("A.Uderz go\nB. Zrób fikołka\n")
        if x.lower()=='a':
            print('*'*200 )
            if gracz.sila>=2:
                print("\nUderzenie posyła złodziejaszka na ziemię. Nieprzytomnego.\nCzujesz się nieswojo.\nOdniosłeś wrażenie, że dawno tego w życiu nie robiłeś i poczułeś się z tymn ieswojo.\nTo co jednak przykuło twoją uwagę to sakiewka obwiązana wokół pasa bezbronnego młodzieńca.\n")
                x=input("A. Zabierz ją\nB. Odejdź\n")
                if x.lower()=='a':
                    print("W sakiewce znajdujesz 6 monet i klucz, postanawiasz jednak nie ryzykować i nie budzić niedoszłego złodzieja z pytaniem co otwiera.\n")
                    gracz.coins+=6
                    gracz.equipment.append("klucz")
                    print(f"stan pieniędzy {gracz.coins}\t stan ekwipunku {gracz.equipment}")
                    self.trzeci_atk=True
                    print('.'*200 )
                    print("\nRuszasz w dalszą drogę wydeptaną ścieżką aż docierasz do miasta.")
                    print("Znajdujesz się w centrum małego miasteczka z czterema budynkami")
                    print("Postanawiasz wejść do jednego z nich.\n")
                elif x.lower()=='b':
                    print("Dobre uczucie roznosi się po twoim ciele kiedy postanawiasz zignorować cenny przedmiot,\nktóry znacznie mógłby zwiększyć twoje szanse na przeżycie w tymzupełnie nieznajomym Ci miejscu")
                    self.trzeci_atk=True
                    print('.'*200 )
                    print("\nRuszasz w dalszą drogę wydeptaną ścieżką aż docierasz do miasta.")
                    print("Znajdujesz się w centrum małego miasteczka z czterema budynkami")
                    print("Postanawiasz wejść do jednego z nich.\n")
                else:
                    print('Wybierz poprawną akcję')
            else:
                print("Z diabelską szybkością wstajesz na własne nogi , składasz dłoń w pięść, zamachujesz się i... wykonujesz cios")
                print("Twoja ręka mija się z celem o centymetry a impet uderzenia niesie cały ciężar ciała do przodu i nieoczekiwanie twój bark spotyka się z glebą")
                print("Oprócz głośnego śmiechu swojego oprawcy słyszysz wyłącznie dudnienie jego oddalających się kroków")
                print("Gdy wstajesz zauważasz, że zabrał on wszystkie twoje pieniądze")
                gracz.coins=0
                gracz.hp-=1
                print(f"stan pieniędzy {gracz.coins}\t stan życia {gracz.hp}")
                self.trzeci_atk=True
                print('.'*200 )
                print("\nRuszasz w dalszą drogę wydeptaną ścieżką aż docierasz do miasta.")
                print("Znajdujesz się w centrum małego miasteczka z czterema budynkami")
                print("Postanawiasz wejść do jednego z nich.\n")
        elif x.lower()=='b':
            while True:
                print('*'*200 )
                print("\nSkładasz się w kłębek i rzucasz się do tyłu")
                print("Zaskoczony złodziej upuszcza część twoich monet na ziemię")
                print("Patrzy na Ciebię z otwartymi oczami, zupełnie jakby czekał na twój następny ruch.\nJeśli on tutaj jest, daje to szansę na to, że w okolicy jest jakaś domieszka cywilizacji.\nPostanawiasz spróbować:\n")
                x=input("A. ”kim jesteś?”\nB. “skąd jesteś?”\nC. “jaki jest sens życia?”\n\n")
                if x.upper()=="A":
                    print("Nieznajomy się zaśmiał “Czekaj może jeszcze swój dowód Ci dam.”")
                    break
                elif x.upper()=="B":
                    print("“Tak długo tu jestem, już nie pamiętam. Powodzenia dziwaku w twojej podróży dokądkolwiek zmierzasz.””")
                    break
                elif x.upper()=="C":
                    print("“Co za róźnica skoro obaj nie żyjemy”")
                    break
                else:
                    print('Wybierz poprawną akcję')
            print("Chłopak odbiega z szybkością jaka tobie sprawiłaby ból.\nPostanawiasz pozbierać leżące na ziemi monety(3) i darować sobie pościg")
            gracz.coins+=3
            print(f"stan pieniędzy {gracz.coins}")
            self.trzeci_atk=True
            print('.'*200 )
            print("\nRuszasz w dalszą drogę wydeptaną ścieżką aż docierasz do miasta.")
            print("Znajdujesz się w centrum małego miasteczka z czterema budynkami")
            print("Postanawiasz wejść do jednego z nich.\n")
        else:
            print('Wybierz poprawną akcję')

    def three(self,gracz):
        s=True
        while s:
            x=input("A.Wejdź do tawerny\nB.Wejdź do sklepu\nC.Wejdź do Ratusza\nD.Wejdź do kopalni\n\n")
            if x.lower()=="a":
                p=True
                print('*'*200 )
                print('Otwierając drzwi do tawerny spotykasz się ze spojrzeniem tamtejszych tubylców i gospodarza.\n')
                while p:
                    print('.'*200 )
                    x=input("A. Podejdź do gospodarza \nB.Podejdź do stolików\nC.Wyjdź z tawerny\n\n")
                    if x.lower()=='a':
                        while True:
                            print("A. “Informacje jak się stad wydostać \nB.Wyjdź z tawerny")
                            if gracz.equipment.count("piwo")==0 and gracz.coins>=5:
                                print("C.“Coś do picia”\n")
                            x=input()
                            if x.lower()=='a':
                                print("“Mogę ci dać tylko podpowiedź do 2 liczby- jest sumą pierwszej i trzeciej”")
                                break
                            elif x.lower()=='b':
                                
                                break
                            elif x.lower()=='c' and gracz.equipment.count("piwo")==0 and gracz.coins>=5:
                                print("“Proszę")
                                gracz.coins-=5
                                gracz.equipment.append("piwo")
                                gracz.hp=3
                                print(f"monety :{gracz.coins} ekwipunek: {gracz.equipment} Hp: {gracz.hp}")
                                
                                break
                            else:
                                print('Wybierz poprawną akcję')  
                    elif x.lower()=='b':
                        if self.stoliki:
                            s=True
                            while s:
                                print('*'*200 )
                                print("Twoją uwagę przykuwa grupka osób siedząca kącie.\n“ej podejdź tu!” woła jeden z nich\n")
                                print("\nA.“Czego chcecie?”\nB. Wybiegnij z baru")
                                for i in gracz.equipment:
                                    if i=="joker":
                                        print("C.“proszę” dajesz kartę\n")
                                        break
                                x=input()
                                if x.lower()=="a":
                                    print("“\n“Hej młodx mam bojowe zadanie dla Ciebie”.\nPodchodzisz zainteresowany do grupki mężczyzn.\nJeden z nich rzuca Ci sakiewkę.\n“wywalili nasze sklepu więc bądź tak miły i kup nam jokera”")
                                    x=input("\nA.“Jokera ?”\nB.“co będę miał w zamian”?\n(dowolna akcja). Wyjdź powoli z baru\n")
                                    if x.lower()=="a":
                                        print("“Taką kartę do gry, brakuje nam jej w talii. Leć już lepiej” Zaintrygowany wychodzisz z tawerny\n")
                                        p=False
                                        s=False
                                    elif x.lower()=='b':
                                        print("“Mam pewne urządzenie które pomoże Ci się dostać do miejsca którego szukasz”.\nZaintrygowany wychodzisz z tawerny\n")
                                        p=False
                                    else:
                                        p=False 
                                        s=False
                                elif x.lower()=="b":
                                    p=False 
                                    s=False
                                elif x.lower()=='c' and gracz.equipment.count("joker")>0:
                                    gracz.equipment.remove("joker")
                                    gracz.equipment.append("łom")
                                    print("“Dobrze się spisałeś. Tu masz łom, przyda Ci się” ")
                                    print(f"ekwipunek : {gracz.equipment}")
                                    self.stoliki=False
                                    s=False
                                else:
                                    print("nie poprawna akcja")
                        elif not self.stoliki:
                            print(" “chłopaki wydają się bardzo zaangażowani w grę więc wolisz im nie przeszkadzać”")
                            p=False
                    elif x.lower()=='c':
                            p=False
            elif x.lower()=='b':
                if self.sklep:
                    print('.'*200 )
                    p=True
                    print("“Witam witam i o zdrowie pytam”. \nSłowa wesołego mężczyzny witają cię w chwili gdy zamykasz za sobą drzwi.\nW czym mogę pomóc przemiłej klienteli?” \n")
                    while p:        
                        x=input("A.”Muszę się stąd wydostać” \nB. “Potargujmy się”\nC. “Pokaż mi swoje towary”\nD. Wyjdź ze sklepu \n")  
                        if x.lower()=='a':
                            if gracz.equipment.count("joker") and gracz.equipment.count("król") and gracz.equipment.count("dama"):
                                print('.'*200 )
                                print("\nJestem prosty człowiek i dotrzymuje obietnic.\nSkrzyni pilnuje strażnik,\nmusisz go jakoś ominąć, i gdy to zrobisz na przeszkodzie stoi Ci tylko kod do skrzyni.\nSłyszałem, że zaczyna się on na cyfrę 3.\nTylko tyle mi na ten temat wiadomo.\nNo nic ja zmykam bo wyprzedałem swój asortyment.\nPowodzenia nieznajomx!\n")
                                gracz.equipment.remove("joker")
                                gracz.equipment.remove("dama")
                                gracz.equipment.remove("król")
                                print(f"ekwipunek= {gracz.equipment}")
                            else:
                                print("\nLegenda krąży o drzwiach ukrytych w skrzyni, za którymi sam diabeł mroczne czary czyni.\nMożna tam wejść jednak najodważniejsi się boją, Każdy zajęty drogą swoją.\nJeśli na wyjściu Ci tak bardzo zależy, moja skromna osoba z czegoś ci się zwierzy.\nKup wszystkie karty, to Ci zrobić trzeba,a twój kupiec Ci powie jak dostać się do nieba!\n")
                        elif x.lower()=='b':
                            print("“\nAh tak a czemuż to miałbym się targować?\nMój wspaniały sklep funkcjonuje tu od niepamiętnych czasów!\nTyle gości z całych zaświatów przychodzi tu po moje wspaniałe karty.\nJeszcze dzisiaj wywalałem grupę nicponi, co wdarła się i prawie całą talie skompletowali zanim ich pogoniłem!\nWięc ponawiam pytanie: Czemu miałbym się targować?”\n")
                            print("A. Ummm bo jestem biedny? \nB. Może i faktycznie nie warto się targować")
                            if gracz.int>=2:
                                print("C.“Skoro nie trzeba jeść i pić pieniądze tu nie są Ci potrzebne.\nZaświaty są całkiem ładnym miejscem -idź pozwiedzać!” \n")
                            x=input()
                            if x.lower()=='a':
                                print("\n“Każdy tutaj jest biedny! mało komu się chce pracować w zaświatach.\nTe Karty to wszystko co mam, a pieniądze potrzebne mi są na podróż którą planowałem od  dawna.\nWybacz ale Wóz albo przewóz”\n")
                            elif x.lower()=='b':
                                print("\n“Choć mam trochę czasu na zapasie, nie marnuj już go” ")
                            elif x.lower()=='c' and gracz.int>=2:
                                print("\n“Hmmm faktycznie nie myślałem o tym w ten sposób.\nZresztą i tak nie wiązałem swojej przyszłości z kupiectwem.\nOd zawsze wolałem poezję.\nDzięki dziwny nieznajomy! Weź moje pozostałe karty i zrób z nimi co zechcesz!\nA byłbym zapomniał! Pierwsza cyfra do skrzyni to 3!”")
                                gracz.equipment.append("joker")
                                gracz.equipment.append("dama")
                                gracz.equipment.append("król")
                                print(f"ekwipunek= {gracz.equipment}")
                                self.sklep=False
                                p=False
                        elif x.lower()=="c":
                            while True:
                                print('.'*200 )
                                print("\n“W moim kramiku, kart ja mam bez liku!\nZ królem karo, będziesz myślał jak kasparov!\nZ damą tarczą, będziesz bił jak chłopi walczą!\nNo a z kartą żartownisia, zdrówka doda jeszcze dzisiaj!\nWięc niech nie stoi tu jak głupi, tylko kupi zaraz kupi!”\n")
                                x=input("A. Poproszę króla karo (3)\nB. Daj mi damę  pik(2)\nC. Wezmę jokera (5)\nD. Może później \n\n")
                                if x.lower()=='a':
                                    gracz.coins-=3
                                    gracz.equipment.append("król")
                                elif x.lower()=='b':
                                    gracz.coins-=2
                                    gracz.equipment.append("dama")
                                elif x.lower()=='c':
                                    gracz.coins-=5
                                    gracz.equipment.append("joker")
                                elif x.lower()=='d':
                                    break
                        elif x.lower()=='d':
                                p=False
                elif self.sklep==False:
                    print('.'*200 )
                    print("\nNa drzwiach wisi wywieszona tabliczka głosząca:\n“wyruszyłem w podróż by znaleźć wenę i ukończyć mój tomik poezji i wtedy zobaczysz mamo jak bardzo się myliłaś!” \n")
            elif x.lower()=='d':
                self.kop=True
                s=False
            elif x.lower()=='c':
                while True:
                    if not self.ryczerz:
                        print('.'*200 )
                        print("W ratuszu znajdujesz strażnika pilnującego skrzyni.\n“Sorry starx nie powinno Cię tu być. Możę lepiej zmykaj stąd”")
                        x=input("A.”Może jednak jakoś się dogadamy?\nB. Wyjdź\nC.Znokautuj rycerza \n")
                        if x.lower()=='a':
                            if gracz.equipment.count("piwo"):
                                gracz.equipment.remove("piwo")
                                print(" “ooo być może przesunę się w zamian za ten trunek”\nRycerz odchodzi z trunkiem w ręku")
                                self.ryczerz=True
                            else:
                                print('.'*200 )
                                print("“hmmm być może mógłbyś mi rzucić tą sakiewkę, chętnie bym wyszedł i się czegoś napił”")
                                x=input("A. Daj mu sakiewkę\nB. Wyjdź\n")
                                if x.lower()=='a':
                                    gracz.coins=0
                                    print("“dziękuję dobrodzeju”")
                                    self.ryczerz=True
                                elif x.lower()=="b":
                                    print("Odwracasz się plecami do rycerza i wychodzisz na przedmieście")
                        elif x.lower()=="b":
                            print("Odwracasz się plecami do rycerza i wychodzisz na przedmieście")
                            break
                        elif x.lower()=='c':
                            if gracz.sila<4:
                                print('.'*200 )
                                print("\nuderzasz Rycerza w jego zbroję ze wszystkich sił.\nSłyszsz głośny brzęk po czym dostrzegasz rycerza patrzącego na Ciebie krzywo.\n“Chyba powinieneś wyjść” mówi stanowczo strażnik. Z pochyloną głową i czerwony ze wstydu opuszczasz ratusz.\n")
                            elif gracz.sila>=4:
                                print('.'*200 )
                                print("Zamykasz oczy i kontrolę oddajesz swoim pierwotnym instynktom.\nSłyszysz głuchy brzęk, niby garnek upadający na podłogę.\nGdy otwierasz 	oczy dostrzegasz leżącego na ziemi rycerza.\nW jego pochwie dostrzegasz wystający miecz")
                                print("A. Weź miecz\nB. Zostaw miecz i podejdź do skrzynki\n")
                                x=input()
                                if x.lower()=="a":
                                    print('.'*200 )
                                    print("ważysz w dłoni oręż gdy nagle czujesz potężny przypływ mocy ogarnia całe twe ciało.\nZ nową energią biegniesz do skrzyni gotów\nprzeciwstawić się czemukolwiek co w niej czeka\n")
                                    print('miecz siegfrieda +5 int +5 siły')
                                    gracz.int+=5
                                    gracz.sila+=5
                                    self.ryczerz=True
                                elif x.lower()=='b':
                                    print('Czujesz się źle z tym co zrobiłeś i z postanowieniem, że nie wyrządzisz więcej krzywdy na tym świecie , podchodzisz do skrzyni')
                                    self.ryczerz=True
                    elif self.ryczerz:
                        print('.'*200 )
                        print("\nPodchodząc do skrzyni wyczuwasz złsą aurę z niej płynącą.\nJuż wiesz, że nie ma odwrotu po jej otwarciu. \n")
                        print("A.Podejdź do skrzyni\n")
                        if gracz.equipment.count("klucz"):
                            print("B.Użyj klucza")
                        if gracz.equipment.count("łom"):
                            print('C.Uzyj łomu')
                        x=input()
                        if x.lower()=='a':
                            print('.'*200 )
                            print("\nPrzysuwasz palec do trzech żeliwnych zębatek i ustawiasz kombinację")
                            x=input("A.Podaj kod\nB.Odsuń sie od skrzyni\n")
                            if x.lower()=='a':
                                x=input()
                                if x=='374':
                                    print('.'*200 )
                                    print("Drewniany schowek otwiera się z hukiem.\nDo pomieszczenia wpada niespotykany wicher a ze skrzyni wypełza silna ręka która w mgnieniu oka chywta cię za włosy.\nDrewniane krzesło leci w twoją stronę a ty niezdolny zrobić unik tracisz przytomność...")
                                    self.fina=True
                                    self.trzeci_atk=False
                                    s=False
                                    break
                                else:
                                    print("Skrzynia ani drgnie.")
                            elif x.lower()=='b':
                                break
                        elif x.lower()=='b' and gracz.equipment.count("klucz"):
                            print("Skradziony klucz pasuje idealnie do zamku i niemalże sam się przekręca")
                            print("Drewniany schowek otwiera się z hukiem")
                            print(" Do pomieszczenia wpada niespotykany wicher a ze skrzyni wypełza silna ręka która w mgnieniu oka chwyta cię za włosy.")
                            print("Drewniane krzesło leci w twoją stronę a ty niezdolny zrobić unik tracisz przytomność... ")
                            self.fina=True
                            self.trzeci_atk=False
                            s=False
                            break
                        elif x.lower()=='c' and gracz.equipment.count("łom"):
                            print("\nZ całych sił próbujesz podważyć wieko skrzyni łomem, ta jednak trzyma się niestrudzenie.\nZiirytowanx zamachujesz się na nią a łom odbija się od niej lądując na twojej twarzy skąd wpada do pobliskiej studzienki.\nPrzeklinasz się w duchu, że to zrobiłeś mimo, że doskonale wiedziałeś, że właśnie tak to się skończy")
                            gracz.equipment.remove('łom')
                            gracz.hp-=1
                            break
    def final(self,gracz):
        a=True
        b=True
        c=True
        d=True
        e=True
        print('.'*100 )
        print("\n\nudzisz się, cały zalanx potem.\nZnajdujesz się w ciemnym, gorącym pomieszczeniu, z jedynym źródłem światła płynącym z ekranu wyświetlającego dwóch gniewnych ludzi z Adamem Sandlerem i Jackiem Nicholsonem w rolach głównych.\nObolały wstajesz i rozglądasz się dookoła.\nNagle czujesz na swoim barku zimną dłoń a zza pleców słyszysz “yo”\n\n")
        x=input("A.Odwróć się \nB.Stój nieruchomo\nC.Zrób fikołka ")
        odp=" \nNagle orientujesz się, że nie jesteś w stanie się ruszyć. \n”Nie bój się dziecko nic Ci nie będzie”-słyszysz głos za swoich pleców. \nNagle czujesz że twoje stopy unoszą się nad ziemią. \nPowoli obracasz się w powietrzu w stronę swojego oprawcy. \n“No chyba, że wieczne cierpienie w piekle nie jest dla Ciebie niczym”-kończy osoba siedząca na tronie. \nTyp siedzący na tronie wygląda na pierwszy rzut oka jak nieudany cosplay shadowa z sonic adventures, ale po chwili przyzwyczajania się twoich gałek ocznych do wszechogarniającej ciemności wygląda bardziej jak zgniły fursuit. \nludzka twarz obrośnięta popielną, baranią sierścia z kilkoma pożółkłymi dodatkami: kły, rogi a nawet niemodny septum był pokryty żółtym nasadem. \n“Nie, żeby coś ale mogę słyszeć twoje myśli” wysycza przez zęby poirytywana, potrącona przez pociąg krzyżówka byka i małpy. \n“Ty mały…” nie słyszysz pozostałych słów bo z hukiem upadasz plackiem na podłogę. \n"
        if x.lower()=='a':
            print('.'*100 )
            print(odp)
        elif x.lower()=='b':
            print('.'*100 )
            print(odp)
        else:
            print('.'*100 )
            print(odp)
        while self.ff:
            print("\nOsoba na tronie patrzy na ciebie z zaciekawieniem\n")
            if a:
                print("A. “kim jesteś do cholery?”")
            if b:
                print("B. “Czy możesz mi wyjaśnić co to za miejsce i co ja tu robię?”")
            if c:
                print("C. “Nie możesz mnie karać za własne myśli, nie moja wina, że wyglądasz jak robaczywy dywan upolowany przez dziadka”")
            if d:
                print("D. Spróbuj zrobić fikołka")
            if e:
                print("E. Zaatakuj stwora")
            x=input("F. “wystarczy” ")
            if x.lower()=='a':
                print('.'*100 )
                print("\n“Naprawdę nie poznajesz mnie?” nagle w ręce stworzenia pojawia się piłeczka od ping ponga. \n“A może teraz?” “Tyle się domyśliłem” -odpowiadasz- \n“Chodziło mi bardziej o nazewnictwo” “Mam wiele imion”-kontynuuje lekko zbity z tropu-“diabeł, belzebub, szatan, Marcin95_apex_twitch, upadły anioł, ale ty możesz mi mówić Krzysiu.”. \nSpoglądasz na diabła za zdziwieniem.\n“Masz racje. Cofam to. \nNie zwracaj się do mnie w ogóle śmiertelniku”\n")
                a=False
            elif x.lower()=='b':
                print('.'*100 )
                print("\n“Na prawdę się jeszcze nie domyśliłeś?\nTypie jesteś w piekle! to tutaj odbędzie się twój ostateczny egzamin który osądzi czy \npowinieneś wstąpić do wrót niebios czy może zostać ze mną w moich skromnych progach!”. \nZa siedzącym na tronie królu podziemia ukazuje się rząd kotłów z gotującą magmą i pływającymi w niej ludźmi. \nWisienką na torcie okazują się jednak wiszące nad nimi ekrany z zapętlonymi komediami adama sandlera oraz wywiadami jamesa cordena. \nz Jednego z kotłów macha Ci Margaret Tchatcher.\nPrzełykasz głośno ślinę, gdy diabeł śmieje się przebiegle")
                b=False
            elif x.lower()=='c':
                print('.'*100 )
                gracz.hp-=1
                print("\nCzujesz tylko jak niewidzialna siła unosi cię na wysokość kilku stóp nad ziemią po czym ciska z ogromną siłą na podłogę. \nSłyszysz charakterystyczny dźwięk dochodzący z twojęgo kręgosłupa i nagle odczuwasz ogromny ból na plecach. \n“Masz coś jeszcze do powiedzenia?” \nKreatura uśmiecha się do ciebie krzywo gdy ty próbujesz nie myśleć o tym jak bardzo musiał być niekochany w dzieciństwie. \nUśmiech znika z twarzy rozmówcy i zastępuję go grymas zła. \n")
                c=False
            elif x.lower()=='d':
                print('.'*100 )
                gracz.hp+=1
                print("\nZ dużym wysiłkiem wstajesz na nogi. \nSzarlatan odruchowo sięga po swój charakterystyczny komicznie wielki widelec. \nTy jednak na przekór bólu i przerażającej aparycji przeciwnika, siadasz na klęczkach, kładziesz dłonie na gorącym kamieniu i wykonujesz przewrót w przód. \nGdy wstajesz z ziemi słyszysz trzask w plecach i czujesz, że nastawiły Ci się poprawnie. \n“wow” diabeł rozluźnia się i odkłada widelec “nieźle”.\nPochwała diabła oraz nastawiony kręgosłup na nowo napełniają cię energią")
                d=False
            elif x.lower()=='e':
                print('.'*100 )
                print('Z krzykiem ruszasz na oponenta gotów go zaatakować.\nJednak twoja furia doprowadziła do chwili nieuwagi i całe przedsięwzięcie zostało zrujnowane przez wystający z podłogi kamień. \nNa nowo słyszysz jak Cierpi twój układ lędźwiowy i zdajesz sobie sprawę z lekcji jaką w tej chwili dostałxś. \nAlbo i nie. \n“Próbowałxś” mówi obojętnie twój niedoszły cel.\n')
                e=False
                gracz.hp-=1
            elif x.lower()=='f':
                print('.'*100 )
                print("\n“Tia, mi też się już zaczynało nudzić”- \nJedno oko diabła błysnęło niebieskim blaskiem gdy w jego ręce zmaterializowała się paletka do gry w tenisa stołowego. \nZ podłogi diabła wysuwa się stół z kilku centymetrową siatka przedzielającą go na \ndwa mniejsze prostokąty a do twojej ręki wbiją się kłująca, żeliwna rakietka tenisowa. \nKolce wbiły się tak głęboko, że nie jesteś w stanie upuścić jej z ręki, a każdy ruch dłonią powoduje duży dyskomfort")
                if gracz.int>= 3:
                    print("“\n już rozumiem!” - krzyczysz nagle - “W poprzednim życiu byłem słynnym tenisistą, \nto była moja filozofia życia i ten sprawdzian ma na celu sprawdzić czy jestem z nią zgodny!”. \n“Jeśli grasz w tenisa tak szybko jak domyślasz się oczywistych rzeczy, \nto nie wróżę Ci spotkania z żadnym bóstwem”")
                print("\n Diabeł pochyla się nad stołem. “zatańczmy\n”")
                self.ff=False
        if gracz.pp>=5:
            self.pong_W=True
            print(" \nTwoja ręka krwawi niemiłosiernie. \nStół znika a pokój wypełniony zostaje nikczemnym śmiechem istoty piekielnej. \n“Chodźcie chłopcy” temu panu już dziękujemy. Widzisz dwójkę chochlików lecących w twoją stronę. \nNagle doznajesz olśnienia. Zdajesz sobie sprawę, z tego, że zmarnowałeś to życie na stawanie się silniejszym\n i inteligentniejszym, ale nie jest jeszcze dla Ciebie za późno. \nDiabeł odwraca się w twoją stronę po przeczytaniu twoich myśli “NIE! ANI MI SIĘ WAŻ!!!”. \nNie słuchasz go jednak gdy spoglądasz na rakietkę w swojej ręce. \nSłyszysz zbliżający się trzepot skrzydeł, ale jest już za późno bo po wzięciu zamachu rakietka ruszyła w kierunku twojej głowy, \na twoje ciało bezwładnie runęło na ziemię. ")
        else:
            self.pong_L=True
            print("\nTwoja ręka krwawi niemiłosiernie. \nStół znika a pokój wypełniony zostaje nikczemnym śmiechem istoty piekielnej.\n “Chodźcie chłopcy” temu panu już dziękujemy. Widzisz dwójkę chochlików lecących w twoją stronę.\n Nagle doznajesz olśnienia. Zdajesz sobie sprawę, z tego, że zmarnowałeś to życie na stawanie się silniejszym i inteligentniejszym, ale nie jest jeszcze dla Ciebie za późno. \nDiabeł odwraca się w twoją stronę po przeczytaniu twoich myśli “NIE! ANI MI SIĘ WAŻ!!!”. \nNie słuchasz go jednak gdy spoglądasz na rakietkę w swojej ręce. \nSłyszysz zbliżający się trzepot skrzydeł, ale jest już za późno bo po wzięciu zamachu rakietka ruszyła w kierunku twojej głowy,\na twoje ciało bezwładnie runęło na ziemię. ")
                    
