from django.test import TestCase

# Create your tests here.

import unittest
from parlantes.models import Parlante


class testParlante(unittest.TestCase):

    def test_crear_objeto(self):
        parlante = Parlante.objects.create(nombre='CD',
                                           tipo='bazucas',
                                           foto=''
                                          )
        parlante.save()

        self.assertTrue(parlante,True)

    def test_buscar_parlante(self):
        parlante = Parlante.objects.get(nombre='Lucifer')
        self.assertEquals(parlante.nombre, 'Lucifer')

    def test_eliminar_parlante(self):
        parlante = Parlante.objects.get(nombre='CD')
        parlante.delete()
        self.assertTrue(parlante, False)
