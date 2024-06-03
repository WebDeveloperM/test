from django.db import models

# Create your models here.



class Vacancy(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Employee(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="employee")
    pnfl = models.CharField(max_length=50)
    add_date = models.DateField(auto_now_add=True)





