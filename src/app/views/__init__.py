from .index import IndexView
from .dashboard import DashboardView
from .usuario import (
    UsuarioListView,
    UsuarioCreateView,
    UsuarioDetailView,
    UsuarioUpdateView,
    UsuarioDeleteView,

    UsuarioCreatePopupView
)

from .proyecto import (
    ProyectoListView,
    ProyectoCreateView,
    ProyectoDetailView,
    ProyectoUpdateView,
    ProyectoDeleteView
)

from .estado_item import (
    EstadoItemListView,
    EstadoItemCreateView,
)

from .created import CreatedView