from django.db import models

# Create your models here.
class Faculty(models.Model):
    """Model definition for Faculty."""

    name = models.CharField('Faculty Name', max_length=50)


    class Meta:
        """Meta definition for Faculty."""

        verbose_name = 'Faculty'
        verbose_name_plural = 'Facultys'

    def __str__(self):
        """Unicode representation of Faculty."""
        return self.name


class Department(models.Model):
    """Model definition for Department."""

    name = models.CharField('Department Name', max_length=50)

    class Meta:
        """Meta definition for Department."""

        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        """Unicode representation of Department."""
        return self.name

