from django.db import models


# Create your models here.


def DownToUp(text):
    headers = {'Content-Type': 'text/plain'}
    data = text.encode('utf-8')
    res = requests.post('https://api.github.com/markdown/raw',
                        headers=headers, data=data)
    return res.text


class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]

    def printText(self):
        return DownToUp(self.text)
