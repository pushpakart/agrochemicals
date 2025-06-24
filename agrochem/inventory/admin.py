from django.contrib import admin
from .models import Chemical

class ChemicalAdmin(admin.ModelAdmin):
    list_display = ('name', 'chemical_type', 'toxicity', 'stock')
    list_filter = ('chemical_type', 'toxicity')
    search_fields = ('name', 'trade_names')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'chemical_type', 'appearance', 'toxicity')
        }),
        ('Usage Information', {
            'fields': ('trade_names', 'suitable_crops', 'quantity_per_hectare', 
                      'quantity_of_water', 'usage_notes')
        }),
        ('Inventory', {
            'fields': ('stock',)
        }),
    )

admin.site.register(Chemical, ChemicalAdmin)