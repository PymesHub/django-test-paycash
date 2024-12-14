from django.db import models
import uuid

class GenreCatalogModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class CivilStateCatalogModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class OcupationCatalogModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class RiskCatalogModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class StatusPLDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class AdressModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.CharField(max_length=255)
    zip_code = models.IntegerField(max_length=5)
    state = models.CharField(max_length=255)

class PersonModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=15)
    genre = models.ForeignKey(GenreCatalogModel, on_delete=models.SET_NULL, null=True)
    civil_state = models.ForeignKey(CivilStateCatalogModel, on_delete=models.SET_NULL, null=True)
    ocupation = models.ForeignKey(OcupationCatalogModel, on_delete=models.SET_NULL, null=True)
    is_high_risk = models.BooleanField(defafault=False)
    address = models.ForeignKey(AdressModel, on_delete=models.SET_NULL, null=True)
    status_pld = models.ForeignKey(StatusPLDModel, on_delete=models.SET_NULL, null=True)

class Documentation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    frontal_ine = models.URLField()
    background_ine = models.URLField()
    person = models.OneToOneField(PersonModel, on_delete=models.CASCADE)