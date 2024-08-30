from .alert_user import AlertUser
from .di_cmd import OnCmd
from .on_update import OnUpdate



class Decorators(
    AlertUser,
    OnCmd,
    OnUpdate
):
    pass
