# =====================
# =====================
# copy/paste the code in this box here to any test
# it allows you to have the test in the /tests/ folder but import
# things above it.  The last line also loads up the MagicMock object
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from unittest.mock import MagicMock
# =====================
# =====================
sys.modules['time'] = MagicMock()

from TimerHelper import TimerHelper