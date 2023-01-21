import random
from datetime import datetime

from django.db.models import Sum
from django.db.models.functions import Coalesce

from core.erp.models import Sale, DetSale

for m in range(0, 6):
    pedids = random.randint(18, 29)
    for d in range(1, pedids):
        vent = Sale()
        vent.cli_id = random.randint(1, 3)
        vent.date_joined = datetime(2020, m + 1, d)
        vent.save()

        food = random.randint(1, 10)

        for i in range(0, food):
            det = DetSale()
            det.sale_id = vent.id
            det.prod_id = random.randint(1, 23)
            det.price = det.prod.pvp
            det.cant = random.randint(1, 4)
            det.subtotal = float(det.price) * det.cant
            det.save()

        vent.subtotal = vent.detsale_set.all().aggregate(r=Coalesce(Sum('subtotal'), 0)).get('r')
        vent.iva = float(vent.subtotal) * 0.12
        vent.total = float(vent.subtotal) + float(vent.iva)
        vent.save()
print('Terminado')
