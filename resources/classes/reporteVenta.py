from handler import *
from databases import *
from .. import funct

class ReporteVenta(Handler):
    def get(self, page_name=""):
    	paises = ['Chulito', 'Republica Dominicana', 'Guatemala', 'Inglaterra', 'Panama', 'Puerto Plata', 'India', 'Fresa', 'Tomate']
    	paises.sort()
        if not self.user:
            self.redirect('/login')
        else:
            self.render('reporte.html', user=self.user, paises=paises)