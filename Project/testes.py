from controller.sgbd_controller import SgbdController
from controller.framework_controller import FrameworkController
from controller.backend_controller import BackendController
from controller.squad_controller import SquadController
from dao.squad_db import SquadDB

# ok = SgbdController()
# okok = FrameworkController()
# okokok = BackendController()
# okokokok = SquadController()

# print(okok.listar_todos()) # ok
# print(ok.listar_todos()) # ok
# print(okokok.listar_todos()) # ok
# print(okokokok.listar_todos()) # error(command SELECT denied) ?????

test1 = SgbdController()
for i in test1.listar_todos():
    print(i)
print(test1.buscar_por_id(1))
from model.sgbd import Sgbd
ok = Sgbd()

# ok.ID = 3
# ok.NOME = 'TA ERRADO'
test1.deletar(4)
for i in test1.listar_todos():
    print(i)



# test2 = FrameworkController()
# test3 = BackendController()
# test4 = SquadController()

