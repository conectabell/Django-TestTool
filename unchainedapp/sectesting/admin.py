from django.contrib import admin
from .models import Test, Test_Plano, Cliente, Soft, CommPredef, CommExecuted, Informe


#admin.site.register(Rules, RulesAdmin)
admin.site.register(Cliente)
admin.site.register(Test)
admin.site.register(Test_Plano)
admin.site.register(Soft)
admin.site.register(CommPredef)
admin.site.register(CommExecuted)
admin.site.register(Informe)
