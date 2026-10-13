from django.db import models


class Editorial(models.Model):
	nombre = models.CharField(max_length=150)
	pais = models.CharField(max_length=100)
	ciudad = models.CharField(max_length=100)
	telefono = models.CharField(max_length=30)
	presupuesto = models.DecimalField(max_digits=12, decimal_places=2)

	class Meta:
		ordering = ["nombre"]
		verbose_name = "editorial"
		verbose_name_plural = "editoriales"

	def __str__(self):
		return self.nombre


class Libro(models.Model):
	titulo = models.CharField(max_length=200)
	autor = models.CharField(max_length=150)
	isbn = models.CharField(max_length=20, unique=True)
	anio_publicacion = models.PositiveSmallIntegerField()
	precio = models.DecimalField(max_digits=10, decimal_places=2)
	editorial = models.ForeignKey(
		Editorial,
		on_delete=models.CASCADE,
		related_name="libros",
	)

	class Meta:
		ordering = ["titulo"]
		verbose_name = "libro"
		verbose_name_plural = "libros"

	def __str__(self):
		return self.titulo
