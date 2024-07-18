from django.db import models
import datetime

# Create your models here.


class Akun(models.Model):
    user_uid = models.CharField(max_length=50, primary_key=True)
    identifier = models.EmailField()
    providers = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now=True)
    signed_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.identifier

    @property
    def is_authenticated(self):
        return True


class Pengguna(models.Model):
    akun = models.OneToOneField(Akun, on_delete=models.CASCADE)
    nama = models.CharField(max_length=50)
    nama_panggilan = models.CharField(max_length=20)
    nim = models.CharField(max_length=20)
    universitas = models.CharField(max_length=50)
    telepon = models.CharField(max_length=15, null=True, blank=True)
    foto = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nama or self.akun.identifier


class JurnalBase(models.Model):
    judul = models.CharField(max_length=50)
    pengguna = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    tanggal = models.DateField(default=datetime.date.today)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.pengguna.nama} - {self.pengguna.akun.identifier}"


class JurnalPagi(JurnalBase):
    q1 = models.CharField(max_length=20)
    q2 = models.CharField(max_length=20)
    q3 = models.CharField(max_length=20)
    q4 = models.CharField(max_length=20)


class JurnalSore(JurnalBase):
    q1 = models.CharField(max_length=20)
    q2 = models.CharField(max_length=20)
    q3 = models.CharField(max_length=20)
    q4 = models.CharField(max_length=20)
    q5 = models.CharField(max_length=20)


class Konselor(models.Model):
    akun = models.OneToOneField(Akun, on_delete=models.CASCADE)
    nama = models.CharField(max_length=50)
    nama_panggilan = models.CharField(max_length=20)
    mitra = models.CharField(max_length=50)
    telepon = models.CharField(max_length=20, null=True, blank=True)
    foto = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nama


class Konseling(models.Model):
    class Status(models.TextChoices):
        disetujui = 'disetujui', 'disetujui'
        diproses = 'diproses', 'diproses'
        selesai = 'selesai', 'selesai'
        reschedule = 'reschedule', 'reschedule'

    pengguna = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    konselor = models.ForeignKey(Konselor, on_delete=models.CASCADE)
    jenis = models.CharField(max_length=50)
    tempat = models.CharField(max_length=50)
    tanggal = models.DateField()
    waktu = models.TimeField()
    pesan = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.diproses)

    def __str__(self):
        return f"{self.pengguna.nama} -  {self.konselor.nama}"
