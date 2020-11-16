statment01 = statment.objects.first()












class ParentModel(models.Model):
	statement1 = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
	parent = models.ForeignKey(ParentModel)
	statement1 = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
parent.childmodel_set.all()
