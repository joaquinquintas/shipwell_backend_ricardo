import sys
import os

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(base_dir, 'core'))
sys.path.insert(0, os.path.join(base_dir, 'infrastructure'))
