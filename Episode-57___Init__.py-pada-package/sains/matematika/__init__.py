# percobaan apabila di dalam package terdapat subpackage lagi yaitu matematika

from . import basic
from . import scientific

from .basic import tambah, kali # melakukan chaining import
from .scientific import pangkat # untuk melompati file scientific sehingga pemanggilannya tidak perlu mendefinisikan scientifi pada subpackage matematika