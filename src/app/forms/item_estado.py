from django import forms
from app.models import Item, CambioEstado, EstadoItem

class ItemUpdateEstadoForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['estado']

    def __init__(self, *args, **kwargs):
        super(ItemUpdateEstadoForm, self).__init__(*args, **kwargs)

        # Datos del Item
        tipo_item = self.instance.tipo
        estado_actual = self.instance.estado

        # Estados posibles
        estados_posibles = []
        cambios = CambioEstado.objects.filter(tipoitem=tipo_item, origen=estado_actual)
        for c in cambios:
            estados_posibles.append(c.destino.id)
        
        self.fields['estado'].queryset = EstadoItem.objects.filter(id__in=estados_posibles)
        #self.fields['estado'].queryset = EstadoItem.objects.all()
