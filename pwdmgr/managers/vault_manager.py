import os
from config import VAULT, SECRET
from cryptography.fernet import Fernet


class VaultManager:
    def __init__(self):
        self.instance = None
        self.content = []
        self.key = SECRET
        self.fernet = Fernet(self.key)

        self.load_vault()

    def load_vault(self):
        '''Load the vault content'''
        if not os.path.isfile(VAULT):
            print('WARNING: Vault file not found!')
            return

        with open(VAULT, 'r') as handle:
            lines = handle.readlines()

        for line in lines:
            location, encrypted_pwd = line.split(' | ')
            self.content.append((location.strip(), encrypted_pwd.strip().encode()))

    def dump_vault(self):
        '''Save changes to the vault'''
        with open(VAULT, 'w') as handle:
            handle.write(self._get_dump())

    def add_record(self, location, password):
        '''Add new password record to the vault'''
        enc_pwd = self._encrypt_string(password)
        if (location, enc_pwd) not in self.content:
            self.content.append((location, enc_pwd))

    def _get_dump(self):
        '''Prepare the vault data to be dumped to the vault file'''
        output = ''
        for pair in self.content:
            location = pair[0]
            encrypted_pwd = pair[1]
            output += f'{location} | {encrypted_pwd.decode()}\n'
        return output

    def fill_from_app(self, data):
        '''Fill the data from the app'''
        for row in data:
            location = row[0]
            raw_pwd = row[1]
            self.content.append((location, self._encrypt_string(raw_pwd)))

    def get_raw_data(self):
        '''Get the data in raw format'''
        output = []
        for pair in self.content:
            location = pair[0]
            encrypted_pwd = pair[1]
            output.append((location, self._decrypt_string(encrypted_pwd)))
        return output

    # region ENCRYPTION
    def _encrypt_string(self, raw):
        '''Encrypt the given string'''
        encrypted = self.fernet.encrypt(raw.encode())
        return encrypted

    def _decrypt_string(self, encrypted):
        '''Decrypt the given string'''
        return self.fernet.decrypt(encrypted).decode()

    def _generate_new_key(self):
        self.key = Fernet.generate_key()
    # endregion
