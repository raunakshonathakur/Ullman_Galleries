activate_this= 'absolute_path_here/advancement_queue/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"absolute_path_here/advancement_queue/")
# from app import app
from app import app as application
