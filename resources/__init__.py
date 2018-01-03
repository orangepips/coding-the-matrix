"""
This has been setup to get around solver.py and indepdence.py's import statements looking for modules in the root
directory. To instead allow all these files to live in the "resources" module instead.
"""

import sys
import resources.GF2
import resources.mat
import resources.matutil
import resources.vec
import resources.vecutil

sys.modules['GF2'] = resources.GF2
sys.modules['mat'] = resources.mat
sys.modules['matutil'] = resources.matutil
sys.modules['vec'] = resources.vec
sys.modules['vecutil'] = resources.vecutil