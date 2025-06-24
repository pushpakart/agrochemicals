from django.db import models

class Chemical(models.Model):
    TYPE_CHOICES = [
        ('PST', 'Pesticide (कीटकनाशक)'),
        ('FNG', 'Fungicide (फफूंदनाशक)'),
        ('HRB', 'Herbicide (तणनाशक)'),
    ]
    
    TOXICITY_CHOICES = [
        ('H', 'High (उच्च)'),
        ('M', 'Medium (मध्यम)'),
        ('L', 'Low (कमी)'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Chemical Name (रसायनाचे नाव)")
    chemical_type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    appearance = models.TextField(verbose_name="Appearance (देखावा)")
    toxicity = models.CharField(max_length=1, choices=TOXICITY_CHOICES)
    trade_names = models.TextField(verbose_name="Trade Names (ब्रँड नावे)")
    suitable_crops = models.TextField(verbose_name="Suitable Crops (योग्य पिके)")
    quantity_per_hectare = models.CharField(max_length=50, verbose_name="Quantity per Hectare (प्रति हेक्टर प्रमाण)")
    quantity_of_water = models.CharField(max_length=50, verbose_name="Quantity of Water (पाण्याचे प्रमाण)")
    usage_notes = models.TextField(verbose_name="Usage Notes (वापर सूचना)")
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock Quantity (स्टॉक प्रमाण)")
    
    def __str__(self):
        return f"{self.name} ({self.get_chemical_type_display()})"
