from django.db import models

# Create your models here.


class Akun(models.Model):
    user_uid = models.CharField(max_length=50, primary_key=True)
    identifier = models.EmailField()
    providers = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)
    signed_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.identifier

    @property
    def is_authenticated(self):
        return True


class Pengguna(models.Model):
    akun = models.OneToOneField(Akun, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    nama_panggilan = models.CharField(max_length=20)
    nim = models.CharField(max_length=20)
    universitas = models.CharField(max_length=50)
    telepon = models.CharField(max_length=20)

    def __str__(self):
        return self.nama or self.akun.identifier


class Jurnal(models.Model):
    pengguna = models.ForeignKey(Pengguna, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pengguna.nama} - {self.pengguna.akun.identifier}"


class Konselor(models.Model):
    akun = models.OneToOneField(Akun, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    mitra = models.CharField(max_length=50)
    telepon = models.CharField(max_length=20)

    def __str__(self):
        return self.nama


class Konseling(models.Model):
    class Status(models.TextChoices):
        BERHENTI = 'BR', 'Berhenti'
        DISETUJUI = 'DS', 'Disetujui'
        DITUNDA = 'DT', 'Ditunda'

    pengguna = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    konselor = models.ForeignKey(Konselor, on_delete=models.CASCADE)
    waktu = models.DateTimeField()
    persetujuan = models.CharField(max_length=50)
    pertemuan = models.CharField(max_length=50)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.BERHENTI,)

    def __str__(self):
        return f"{self.pengguna.nama} -  {self.konselor.nama}"
