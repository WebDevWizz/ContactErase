class Contact: 
    def __init__(self, name, surname, phone, email=""): # Email non obbligatoria
        """ Costruttore per inizializzare un nuovo contatto"""
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email


    def __str__(self):
        """ Conversione in stringa del contatto """
        return f"{self.name} {self.surname}: {self.phone}" + (f", {self.email}" if self.email else "")