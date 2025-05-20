from Contact import Contact


class Interface: 
    def __init__(self, phonebook):
        """ INIZIALIZZA L'INTERFACCIA UTENTE """
        self.phonebook = phonebook #oggetto della classe 'Contact'
        self.stato = False 

    
    def start(self): 
        """ L'UTENTE AVVIA L'INTERFACCIA """
        self.stato = True 
        print("Benvenuto nella tua Rubrica Telefonica!")
        while self.stato: 
            self._displayMenu()
            choice = input("Scegli un'opzione (1-7): ")
            self._choice(choice)


    def _displayMenu(self): 
        """ FUNZIONE PER VISUALIZZARE IL MENU PRINCIPALE """
        print("\nMENU' PRINCIPALE\n")
        print("1- Visualizza Contatti")
        print("2- Aggiungi contatto")
        print("3- Ricerca contatto")
        print("4- Elimina contatto")
        print("5- Modifica Contatto")
        print("6- Esci")

    
    def _choice(self, choice): 
        if choice == "1": 
            self._displayContacts()
        elif choice == "2": 
            self._addContact()
        elif choice == "3": 
            self._searchContact()
        elif choice == "4": 
            self._deleteContact()
        elif choice == "5": 
            self._editContact()
        elif choice == "6": 
            self._exit()
        else: 
            print("Scelta non valida, riprova")


    def _displayContacts(self): 
        """ FUNZIONE PER VISUALIZZARE TUTTI I CONTATTI """
        print("\n --- I TUOI CONTATTI --- \n")

        contacts = self.phonebook.getContacts()
        if not contacts: 
            print("La rubrica e' vuota.")
        else: 
            for i, contatto in enumerate(contacts, 1): 
                email_info = f", {contatto.email}" if contatto.email else "" # Gestione spacchettamento email
                print(f"{i}. {contatto.name} {contatto.surname}: {contatto.phone}, {email_info}")



    def _addContact(self): 
        """ Aggiungi un contatto alla rubrica """
        print("\n--- INSERISCI I DATI DEL CONTATTO: ----\n")
        name = input("Nome: ")
        surname = input("Cognome: ")
        phone = input("Telefono: ")        
        email = input("Email (opzionale): ")

        new_contact = Contact(name, surname, phone, email)

        self.phonebook.addContact(new_contact)

        print(f"\nIl contatto {name} {surname} e' stato aggiunto con successo!")


    def _searchContact(self): 
        """ FUNZIONE PER CERCARE UN CONTATTO, SOLO PER NOME E COGNOME """
        print("\n --- CERCA CONTATTO --- \n")

        campo = input("Inserisci nome o cognome: \n")

        results = self.phonebook.searchContact(campo)

        if not results: 
            print("La rubrica e' vuota.")
        else: 
            print("Contatti trovati: \n")
            for i, contatto in enumerate(results, 1): 
                email_info = f", {contatto.email}" if contatto.email else "" 
                print(f"{i}, {contatto.name} {contatto.surname}: {contatto.phone}, {email_info}")


    def _deleteContact(self): 
        """ FUNZIONE PER ELIMINARE UN CONTATTO """
        print("\n --- ELIMINA CONTATTO --- \n")

        # LOGICA -> CERCO + ELIMINO (+ gestione di contatti con lo stesso nome e cognome)

        c = input("Inserisci nome o cognome del contatto da eliminare: \n")
        results = self.phonebook.searchContact(c)

        if not results: 
            print("Nessun contatto trovato.")
            return
        
        # Gestione + Contatti trovati: 
        if len(results) > 1: 
            print("\nTrovati più contatti: \n")
            for i, contatto in enumerate(results, 1): 
                email_info = f", {contatto.email}" if contatto.email else "" 
                print(f"{i}, {contatto.name} {contatto.surname}: {contatto.phone}, {email_info}")


            contact_index = int(input("\nInserisci il numero (indice) del contatto da eliminare: "))

            contact_to_delete = results[contact_index]
        else: 
            contact_to_delete = results[0]

        # Conferma eliminazione: 
        conferma = input(f"Sei sicuro di voler eliminare il contatto {contact_to_delete.name} {contact_to_delete.surname}? [si/no]\n")
        if conferma == "si": 
            if self.phonebook.deleteContact(contact_to_delete): 
                print("\nContatto eliminato con successo!")
            else: 
                print("\nErrore nell'eliminazione del contatto.\n")
        else: 
            print("\nEliminazione annullata.")


    def _editContact(self): 
        """ FUNZIONE PER MODIFICARE UN CONTATTO """ 
        print("\n --- MODIFICA CONTATTO --- \n")

        # Stessa logica usata per l'eliminazione

        c = input("Inserisci nome o cognome del contatto da modificare: \n")
        results = self.phonebook.searchContact(c)

        if not results: 
            print("Nessun contatto trovato.")
            return
        
        # Gestione + Contatti trovati: 
        if len(results) > 1: 
            print("\nTrovati più contatti: \n")
            for i, contatto in enumerate(results, 1): 
                email_info = f", {contatto.email}" if contatto.email else "" 
                print(f"{i}, {contatto.name} {contatto.surname}: {contatto.phone}, {email_info}")


            try:
                contact_index = int(input("\nInserisci il numero (indice) del contatto da modificare: ")) - 1
                contact_to_edit = results[contact_index]
            except (ValueError, IndexError):
                print("Indice non valido.")
                return
        else: 
            contact_to_edit = results[0]

        print(f"\n MODIFICA DEL CONTATTO {contact_to_edit.name} {contact_to_edit.surname}\n")
        scelta = input("Che campo vuoi eliminare? [name / surname / phone / email]\n").strip().lower()

        if scelta == "name" or scelta == "surname" or scelta == "phone" or scelta == "email":
            new_value = input(f"\nImposta il nuovo valore per il campo {scelta}: ")

            if self.phonebook.updateContact(contact_to_edit, scelta, new_value):
                print(f"\nCampo {scelta} aggiornato con successo!\n")
            else: 
                print("\nImpossibile aggiornare il contatto.\n")
        else: 
            print("\nCampo non valido.")
            return 




    def _exit(self): 
        """ FUNZIONE PER USCIRE DALL' APPLICAZIONE """
        self.stato = False
        print("\nUscita dalla rubrica.")