from UserInterface import Interface
from Phonebook import PhoneBook


def main(): 
    #Creo una nuova rubrica
    phonebook = PhoneBook()

    json_file = "contacts.json"

    # CARICO PRIMA I CONTATTI, E POI AVVIO L'INTERFACCIA:
    print("Carico i contatti della tua rubrica...") 
    if phonebook.loadContactsFromFile(json_file):
        print(f"\nTrovato {len(phonebook.getContacts())} contatti.\n")
    else:
        print("Avvio con una rubrica vuota.") 

    
    # AVVIA L'INTERFACCIA: 
    interface = Interface(phonebook)
    interface.start()


    # SALVO I CONTATTI PRIMA DI USCIRE: 
    print("\nSalvataggio contatti...")
    if phonebook.saveContactsInFile(json_file): 
        print("\nContatti salvati con successo!")
    else: 
        print("\nErrore nel salvataggio.")



if __name__ == "__main__": 
    main()
