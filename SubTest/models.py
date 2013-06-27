from django.db import models


# Create your models here.

class SubTestResult(models.Model):
    
    orgName = models.CharField(max_length=50)
    candName = models.CharField(max_length=50)
	# path = models.CharField(max_length=100)
    # distortion = models.CharField(max_length=2,choices = DIST_TYPE)
    groupName = models.IntegerField()
	
    def __unicode__(self):
        return self.orgName + "_to_" + self.candName +"_with_"+ str(self.rank)

class RankRecord(models.Model):
    Record = models.CharField(max_length=80)

    def __unicode__(self):
        return self.Record


