from django.db import models

class post(models.Model):

    author_choices = [ ('Dr. Jane Starfield', 'Dr. Jane Starfield'),  ('John Doe', 'John Doe'), ('Mark Thompson', 'Mark Thompson'),
                       ('Rachel Eco', 'Rachel Eco'), ('Dr. Emma Stone', 'Dr. Emma Stone'), ('Laura Peace', 'Laura Peace')]   
    tag_choices = [ ('History', 'History'), ('Environment', 'Environment'), ('Cooking', 'Cooking'),
                       ('Programming', 'Programming'), ('Marketing', 'Marketing'), ('Astronomy','Astronomy')]
    title = models.CharField(max_length=200)
    content = models.TextField()
    author= models.CharField(max_length=30, choices=author_choices,default='John Doe')
    tag = models.CharField(max_length=30, choices=tag_choices,default='History')

 
    def __str__(self):
        return self.title
