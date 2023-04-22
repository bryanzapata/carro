from appUsuarios.models import Usuario

class Carro(models.Model):
    ESTADO_PROD = (
        ('activo', 'activo'),
        ('comprado', 'comprado'),
        ('anulado', 'anulado'),
)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=False)
    cantidad = models.IntegerField(null=False, default= 1)
    valUnit = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO_PROD, default='activo')