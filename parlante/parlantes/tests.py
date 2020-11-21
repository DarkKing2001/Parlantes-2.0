from django.test import TestCase

# Create your tests here.

import unittest
from parlantes.models import Parlante


class testParlante(unittest.TestCase):

    def test_crear_objeto(self):
        parlante = Parlante.objects.create(codigo='1',
                                           nombre='CD',
                                           tipo='bazucas',
                                           foto=''
                                          )
        parlante.save()

        self.assertTrue(parlante,True)

    def test_buscar_parlante(self):
        parlante = Parlante.objects.get(codigo='1')
        self.assertEquals(parlante.nombre, 'CD')

    def test_eliminar_parlante(self):
        parlante = Parlante.objects.get(codigo='1')
        parlante.delete()
        self.assertTrue(parlante, False)
