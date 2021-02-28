from .index import IndexView
from .dashboard import DashboardView
from .created import CreatedView
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
    EstadoItemDetailView,
    EstadoItemUpdateView,
    EstadoItemDeleteView
)
from .tipo_item import (
    TipoItemListView,
    TipoItemCreateView,
    TipoItemDetailView,
    TipoItemUpdateView,
    TipoItemDeleteView
)
from .cambio_estado import CambioEstadoCreatePopupView