class Movie(models.Model):
    movieid = models.CharField(db_column='MovieID', primary_key=True, max_length=10)  # Field name made lowercase.
    movietitle = models.CharField(db_column='MovieTitle', max_length=30)  # Field name made lowercase.
    releasedate = models.DateField(db_column='ReleaseDate')  # Field name made lowercase.
    genereid = models.CharField(db_column='GenereID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    directorid = models.CharField(db_column='DirectorID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=250)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movie'
