import csv

class Contact():

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook():

    def __init__(self):
        self._contactos = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contactos.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contactos:
            self._print_contact(contact)

    def delete(self, name):
        for idx, contact in enumerate(self._contactos):
            if contact.name.lower() == name.lower():
                del self._contactos[idx]
                self._save()
                break

    def update(self, name, phone, email):
        for contact in self._contactos:
            if contact.name.lower() == name.lower():
                contact.phone = phone
                contact.email = email
                self._save()
                break
        else:
            self._not_found()

    def search(self, name):
        for contact in self._contactos:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def _save(self):
        with open('./src/csv/contactos.csv', 'w', newline='') as f:
            w_writer = csv.writer(f)
            w_writer.writerow( ('name', 'phone', 'email') )

            for contact in self._contactos:
                w_writer.writerow( (contact.name, contact.phone, contact.email) )

    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))

    def _not_found(self):
        print('****************')
        print('¡No encontrado!')
        print('****************')

def run():

    contact_book = ContactBook()
    with open('./src/csv/contactos.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            else:
                contact_book.add(row[0], row[1], row[2])

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            print('añadir contacto')
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el tel del contacto: '))
            email = str(input('Escribe el email del contacto: '))
            contact_book.add(name, phone, email)

        elif command == 'ac':
            name = str(input('Escribe el nombre del contacto que desea actualizar: '))
            phone = str(input('Escribe el telefono desea actualizar: '))
            email = str(input('Escribe el email desea actualizar: '))
            contact_book.update(name, phone, email)

        elif command == 'b':
            name = str(input('Escribe el nombre del contacto que desea buscar: '))
            contact_book.search(name)

        elif command == 'e':
            name = str(input('Escribe el nombre del contacto que desea eliminar: '))
            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print('B I E N V E N I D O     A     L A     A G E N D A')
    run()
