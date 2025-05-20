import json
from Contact import Contact

# Uso una lista per salvare i contatti
class PhoneBook: 
    def __init__(self):
        self.contacts = [] # Lista inizialmente vuota


    # IMPLEMENTAZIONE OPERAZIONI CRUD (Create, Read, Update, Delete)

    def addContact(self, contact):
        """ AGGIUNGI UN CONTATTO ALLA RUBRICA"""
        self.contacts.append(contact)

    def deleteContact(self, contact):
        """ RIMUOVI UN CONTATTO DALLA RUBRICA """
        if contact in self.contacts: 
            self.contacts.remove(contact)
            return True
        else:
            return False

    def getContacts(self): 
        """ RESTITUISCE TUTTI I CONTATTI """
        return self.contacts
    
    def updateContact(self, contact, campo, valore): 
        """ AGGIORNA UN CONTATTO """

        #Aggiorna un campo qualsiasi del contatto
        if contact in self.contacts: 
            index = self.contacts.index(contact) # Salvo l'indice del contatto che voglio modificare

            #Uso 2 funzioni della libreria Python per vedere se il campo specificato esiste e, in caso, modificarlo: 
            if hasattr(self.contacts[index], campo): 
                setattr(self.contacts[index], campo, valore)
                return True
        
        return False
    

    # Altre funzioni (in base alle specifiche): 
    
    def searchContact(self, campo): # Da specifica, il contatto va cercato tramite nome e cognome
        """ CERCA CONTATTI PER NOME E COGNOME """

        # Aggiorno il termine di ricerca, in modo che sia case-sensitive
        campo = campo.lower()

        results = [] # Lista per i risultati della ricerca

        for contact in self.contacts: 
            # Filtro per nome e cognome: 
            if campo in contact.name.lower() or campo in contact.surname.lower(): 
                results.append(contact)
        
        return results
    

    def saveContactsInFile(self, file): 
        """ SALVA I CONTATTI IN UN FILE JSON """
        # Converto innanzitutto il contatto in un dizionario: 
        
        try: 
            contatti_dict = [] # Ogni contatto è un dizionario; l'insieme dei dizionari li salvo in una lista
            for contact in self.contacts: 
                contact_dict = {
                    "name": contact.name, 
                    "surname": contact.surname,
                    "phone": contact.phone, 
                    "email": contact.email
                }
                contatti_dict.append(contact_dict)

            # Salvo la lista di dizionari nel file JSON; se non esiste, lo crea: 
            with open(file, 'w', encoding='utf-8') as f: 
                json.dump(contatti_dict, f, ensure_ascii=False) # Mantengo anche i caratteri speciali
            
            return True
        except Exception as e: 
            print(f"Errore nel salvataggio: {e}")
            return False


    def loadContactsFromFile(self, file): 
        """ CARICA I CONTATTI DA UN FILE JSON """

        try: 
            with open(file, 'r', encoding="utf-8") as f: 
                contatti_dict = json.load(f)

            # OPERAZIONE INVERSA -> ricreo l'oggetto "Contact" a partire dal dict

            self.contacts = [] # Pulisco la lista dei contatti attuali

            for contact_data in contatti_dict: 
                contatto = Contact(
                    name = contact_data["name"],
                    surname = contact_data["surname"], 
                    phone = contact_data["phone"],
                    email = contact_data.get("email", "")
                )

                self.contacts.append(contatto)
            
            return True

        except FileNotFoundError: # Il file non esiste, e quindi inizio con una rubrica vuota
            self.contacts = []
            return False
        
        except Exception as e: 
            print(f"Errore nel caricamento: {e}")
            self.contacts = []
            return False

