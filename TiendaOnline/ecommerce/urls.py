from django.contrib import admin
from django.urls import path
from ecommerce.views import *
from django.contrib.auth.views import LogoutView




urlpatterns = [
    path('inicio/', incio, name="Inicio"),
    path('mouses/', mouses, name="Mouses"),
    path('teclados/', teclados, name="Teclados"),
    path('monitores/', monitores, name="Monitores"),
    path('auriculares/', auriculares, name="Auriculares"),
    path('sillas_gamer/', silas_gamer, name="sillasGamer"),
    path('mouse_formulario/', mouse_formulario, name="mouseFormulario"),
    path('articulo_agregado/', articulo_agregado, name="articuloAgregado"),
    path('teclado_formulario/', teclado_formulario, name="tecladoFormulario"),
    path('monitores_formulario/', monitores_formulario, name="monitoresFormulario"),
    path('auriculares_formulario/', auriculares_formulario, name="auricularesFormulario"),
    path('sillasgamer_formulario/', sillasgamer_formulario, name="sillasGamerFormulario"),
    path('lista_monitores/', listaMonitores, name="listaMonitores"),
    path('elimina_monitor/<int:id>', eliminaMonitor, name="eliminaMonitor"),
    path('editar_monitor/<int:id>', editarMonitor, name="editarMonitor"),
    path('lista_mouses/', listaMouses, name="listaMouses"),
    path('elimina_mouse/<int:id>', eliminaMouse, name="eliminaMouse"),
    path('editar_mouse/<int:id>', editarMouse, name="editarMouse"),
    path('lista_auriculares/', listaAuriculares, name="listaAuriculares"),
    path('elimina_auriculares/<int:id>', eliminaAuricular, name="eliminaAuriculares"),
    path('editar_auriculares/<int:id>', editarAuricular, name="editarAuriculares"),
    path('lista_teclados/', listaTeclados, name="listaTeclados"),
    path('elimina_teclados/<int:id>', eliminaTeclado, name="eliminaTeclado"),
    path('editar_teclados/<int:id>', editarTeclado, name="editaTeclado"),
    path('lista_sillas/', listaSillas, name="listaSillas"),
    path('elimina_sillas/<int:id>', eliminaSillas, name="eliminaSillas"),
    path('editar_sillas/<int:id>', editarSillas, name="editaSillas"),
    path('lista_mouse/', MouseList.as_view(), name="listaMouses"),
    path('detalle_mouse/<pk>', MouseDetail.as_view(), name="detalleMouses"),
    path('crea_mouse/', MouseCreate.as_view(), name="creaMouses"),
    path('actualiza_mouse/<pk>', MouseUpdate.as_view(), name="actualizaMouses"),
    path('elimina_mouses/<pk>', MouseDelete.as_view(), name="eliminaMouses"),
    path('list_teclados/', TecladoList.as_view(), name="listaTeclados"),
    path('detalle_teclados/<pk>', TecladoDetail.as_view(), name="detalleTeclados"),
    path('crea_teclados/', TecladoCreate.as_view(), name="creaTeclados"),
    path('actualiza_teclados/<pk>', TecladoUpdate.as_view(), name="actualizaTeclados"),
    path('elimina_teclado/<pk>', TecladoDelete.as_view(), name="eliminaTeclados"),
    path('monitores_list/', MonitoresList.as_view(), name="listaMonitores"),
    path('detalle_monitores/<pk>', MonitoresDetail.as_view(), name="detalleMonitores"),
    path('crea_monitores/', MonitoresCreate.as_view(), name="creaMonitores"),
    path('actualiza_monitores/<pk>', MonitoresUpdate.as_view(), name="actualizaMonitores"),
    path('elimina_monitores/<pk>', MonitoresDelete.as_view(), name="eliminaMonitores"),
    path('auriculares_list/', AuricularesList.as_view(), name="listaAuriculares"),
    path('detalle_auriculares/<pk>', AuricularesDetail.as_view(), name="detalleAuriculares"),
    path('crea_auriculares/', AuricularesCreate.as_view(), name="creaAuriculares"),
    path('actualiza_auriculares/<pk>', AuricularesUpdate.as_view(), name="actualizaAuriculares"),
    path('eliminar_auriculares/<pk>', AuricularesDelete.as_view(), name="eliminarAuriculares"),
    path('sillasGamer_list/', SillasGamerList.as_view(), name="listaSillasGamer"),
    path('detalle_sillasGamer/<pk>', SillasGamerDetail.as_view(), name="detalleSillasGamer"),
    path('crea_sillasGamer/', SillasGamerCreate.as_view(), name="creaSillasGamer"),
    path('actualiza_sillasGamer/<pk>', SillasGamerUpdate.as_view(), name="actualizaSillasGamer"),
    path('eliminar_sillasGamer/<pk>', SillasGamerDelete.as_view(), name="eliminaSillasGamer"),
    path('login/', login_request, name="Login"),
    path('register/', register, name="Register"),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='Logout'),





   
]
    



