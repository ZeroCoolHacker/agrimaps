from django.db import models
from django.urls import reverse
# Create your models here.
class Faculty(models.Model):
    """Model definition for Faculty."""

    name = models.CharField('Faculty Name', max_length=50)
    dean = models.CharField('Dean', max_length=50)


    class Meta:
        """Meta definition for Faculty."""

        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'

    def __str__(self):
        """Unicode representation of Faculty."""
        return self.name


class Department(models.Model):
    """Model definition for Department."""
    
    
    faculty     = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name        = models.CharField('Department Name', max_length=50)
    chairman    = models.CharField('Chairman', max_length=50)
    description = models.TextField(default='Enter Description Here')
    cover_photo = models.ImageField('Department Cover Photo', upload_to='departments/', null=True)
    map_url     = models.URLField('Map URL', default='http://localhost')


    class Meta:
        """Meta definition for Department."""

        verbose_name = 'Department'
        verbose_name_plural = 'Departments'


    def get_absolute_url(self):
        return reverse('department', kwargs={'pk': self.pk})

    
    def __str__(self):
        """Unicode representation of Department."""
        return self.name



class vips(models.Model):
    """Model definition for vips."""

    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    image = models.ImageField(upload_to='vips', null=True)
    class Meta:
        """Meta definition for vips."""

        verbose_name = 'vips'
        verbose_name_plural = 'vipss'

    def __str__(self):
        """Unicode representation of vips."""
        return self.name
