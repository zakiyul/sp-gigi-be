from django.db import models

class Gejala(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama
    
class Penyakit(models.Model):
    nama = models.CharField(max_length=255)
    definisi = models.TextField()
    solusi = models.TextField()
    dokter = models.TextField()
    gambar = models.ImageField(upload_to='penyakit/', null=True)

    def __str__(self):
        return self.nama
    
class BasisPengetahuan(models.Model):
    kode_gejala = models.ForeignKey(Gejala, on_delete=models.CASCADE)
    kode_penyakit = models.ForeignKey(Penyakit, on_delete=models.CASCADE)
    bobot = models.FloatField()

class DsRules(models.Model):
    id_gejala = models.ForeignKey(Gejala, on_delete=models.CASCADE)
    id_penyakit = models.ForeignKey(Penyakit, on_delete=models.CASCADE)
    bobot = models.FloatField()

class Riwayat(models.Model):
    nama = models.CharField(max_length=200)
    tgl = models.DateTimeField()
    result_cf = models.TextField()
    result_tb = models.TextField()
    result_ds = models.TextField()

    def __str__(self):
        return self.nama
