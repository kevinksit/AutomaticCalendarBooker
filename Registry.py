from os import path
import time
import pickle

class Registry:
    def __init__(self):
        if path.exists('registry.pickle'):
            self.registry = pickle.load(open('registry.pickle', 'rb'))
        else:
            self.initialize() 

    def check(self, input_char):
        if input_char in self.registry:
            return True
        else:
            return False

    def getUser(self, input_char):
        return self.registry[input_char]

    def initialize(self, input_char=None):
        self.registry = dict()
        self.save()

    def save(self):
        registry = self.registry
        pickle.dump(registry, open('registry.pickle', 'wb'))

    def add(self, input_char):
        print('ID not recognized, registering new user...')
        time.sleep(0.5)
        username = self.getUsername()
        if username:
            self.update(input_char, username)
        else:
            print('Registry not updated, no new user added')

    def edit(self):
        print('Editing registry')
        print(self.registry)
        input_char = input('Select user number to edit: ')
        is_edit = input('Would you like to edit (1) or remove (0) this user?: ')
        if is_edit == '1':
            username = self.getUsername()
            self.update(input_char, username)
        elif is_edit == '0':
            self.remove(input_char)
        else:
            print('No changes made')
            return

    def update(self, input_char, username):
        self.registry[input_char] = username
        self.save() # update
        print('Registry updated!')

    def remove(self, input_char):
        user = self.registry[input_char]
        self.registry.pop(input_char, 'None')
        print('Removed ' + user + ' from the registry')

    def getUsername(self):
        username = input('Type your name: ')
        return username