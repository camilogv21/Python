import config

# Importe sus modulos y paquetes
import banco

import extra.iota
import extra.good.alpha

from extra import iota
from extra.iota import FunI as yy
from extra.good.best import sigma
from extra.good.best import tau
from extra.good import beta
from extra.good.beta import FunB

from extra.ugly.omega import *
from extra.ugly import omega, psi

if __name__ == "__main__":

    usuario1 = banco.Banco()
    usuario1.crearCuenta()
    print(usuario1)

    print( extra.iota.FunI() )
    print( extra.good.alpha.FunA() )
    print( iota.FunI() )
    print( sigma.FunS() )
    print( beta.FunB() )
    print( FunB() )
    print( omega.FunO() )
    print( psi.FunP() )
    print( tau.FunT() )
