from django.db import models
from cryptography.fernet import Fernet
from django.conf import settings
from accounts.models import key


#key = Fernet.generate_key()
#cipher_suite = Fernet(key)
cipher_suite = Fernet(key)
class Complaint(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    encrypted_default_title = cipher_suite.encrypt(b'Default title')
    encrypted_default_description = cipher_suite.encrypt(b'Default Description')
    encrypted_title = models.BinaryField(default=encrypted_default_title)
    encrypted_description = models.BinaryField(default=encrypted_default_description)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def set_encrypted_fields(self, title, description):
        self.encrypted_title = cipher_suite.encrypt(title.encode())
        self.encrypted_description = cipher_suite.encrypt(description.encode())

    def get_decrypted_title(self):
        try:
            return cipher_suite.decrypt(self.encrypted_title).decode()
        except Exception as e:
            return "Error: Unable to decrypt title"

    def get_decrypted_description(self):
        try:
            return cipher_suite.decrypt(self.encrypted_description).decode()
        except Exception as e:
            return "Error: Unable to decrypt description"
  