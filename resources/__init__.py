"""
This has been setup to get around solver.py and indepdence.py's import statements looking for modules in the root
directory. To instead allow all these files to live in the "resources" module instead.
"""

import sys
import resources.GF2
import resources.mat
import resources.vec

sys.modules['GF2'] = resources.GF2
sys.modules['mat'] = resources.mat
sys.modules['vec'] = resources.mat