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

teste = SquadController()
a = teste.listar_todos()
for i in a:
    print(i)
