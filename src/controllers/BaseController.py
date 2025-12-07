from helpers.config import get_settings, Sittings
import os
import random
import string
 
class BaseController:
    def __init__(self):
        self.app_sittings = get_settings()

        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        
        self.File_dir = os.path.join(self.base_dir, "../assets/Files/")

    def generate_random_string(self, length: int = 12) :
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))