from django.db import models

# Create your models here.

class Header(models.Model):
    name = models.CharField('Header name', max_length=50)
    about = models.TextField('Header about')
    about1 = models.TextField('Header about1')
    about2 = models.TextField('Header about2')
    about3 = models.TextField('Header about3')
    about4 = models.TextField('Header about4')
    about5 = models.TextField('Header about5')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Header'
        verbose_name_plural = 'Headers'



class Head(models.Model):
    name = models.CharField('Head name', max_length=50)
    name1 = models.CharField('Head name1', max_length=50)
    about = models.TextField('Head about')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Head'
        verbose_name_plural = 'Heads'

class HeadCarusel(models.Model):
    name = models.CharField('HeadCarusel name', max_length=50)
    name1 = models.CharField('HeadCarusel name1', max_length=50)
    about = models.TextField('HeadCarusel about')
    img = models.ImageField('HeadCarusel image', upload_to='media', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HeadCarusel'
        verbose_name_plural = 'HeadCarusels'



class Video(models.Model):
    video = models.FileField('Video video', upload_to='media', null=True)
    
    def __str__(self):
        return str(self.video)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'



class Menu(models.Model):
    name = models.CharField('Menu name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menues'



class MenuAbout(models.Model):
    name = models.CharField('MenuAbout name', max_length=30)
    name1 = models.CharField('MenuAbout name1', max_length=30)
    about = models.TextField('MenuAbout about')
    about1 = models.TextField('MenuAbout about1')
    about2 = models.TextField('MenuAbout about2')
    img = models.ImageField('MenuAbout image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'MenuAbout'
        verbose_name_plural = 'MenuAbouts'



class Event(models.Model):
    name = models.CharField('Event name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'



class EventTwoImage(models.Model):
    name = models.CharField('EventTwoImage name', max_length=60)
    about = models.TextField('EventTwoImage about')
    img = models.ImageField('EventTwoImage image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'EventsTwoImage'
        verbose_name_plural = 'EventsTwoImages'



class EventFoot(models.Model):
    name = models.CharField('EventFoot name', max_length=50)
    about = models.TextField('EventFoot about')
    about1 = models.TextField('EventFoot about1', null=True, blank=True)
    img = models.ImageField('EventFoot image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'EventFoot'
        verbose_name_plural = 'EventFoots'



class HomeFoot(models.Model):
    name = models.CharField('HomeFoot name', max_length=50)
    name1 = models.CharField('HomeFoot name1', max_length=50)
    name2 = models.CharField('HomeFoot name2', max_length=50)
    name3 = models.CharField('HomeFoot name3', max_length=50)
    name4 = models.CharField('HomeFoot name4', max_length=50)
    about = models.TextField('HomeFoot about')
    about1 = models.TextField('HomeFoot about1')
    about2 = models.TextField('HomeFoot about2')
    about3 = models.TextField('HomeFoot about3')
    about4 = models.TextField('HomeFoot about4')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeFoot'
        verbose_name_plural = 'HomeFoots'



class HomeRevers(models.Model):
    name = models.CharField('HomeRevers name', max_length=50)
    name1 = models.CharField('HomeRevers name1', max_length=50)
    about = models.TextField('HomeRevers about')
    about1 = models.TextField('HomeRevers about1')
    about2 = models.TextField('HomeRevers about2')
    about3 = models.TextField('HomeRevers about3')
    about4 = models.TextField('HomeRevers about4')
    about5 = models.TextField('HomeRevers about5')
    about6 = models.TextField('HomeRevers about6')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeRevers'
        verbose_name_plural = 'HomeReverses'






class StoryHeader(models.Model):
    name = models.CharField('StoryHeader name', max_length=30)
    about = models.TextField('StoryHeader about')
    about1 = models.TextField('StoryHeader about')
    about2 = models.TextField('StoryHeader about')
    about3 = models.TextField('StoryHeader about')
    about4 = models.TextField('StoryHeader about')
    about5 = models.TextField('StoryHeader about')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'StoryHeader'
        verbose_name_plural = 'StoryHeaders'



class Kitchen(models.Model):
    name = models.CharField('Kitchen name', max_length=50)
    about = models.TextField('Kitchen about')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kitchen'
        verbose_name_plural = 'Kitchens'



class KitchenBody(models.Model):
    name = models.CharField('KitchenBody name', max_length=70)
    name1 = models.CharField('KitchenBody name1', max_length=70)
    name2 = models.CharField('KitchenBody name2', max_length=70)
    about = models.TextField('KitchenBody about')
    about1 = models.TextField('KitchenBody about1')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'KitchenBody'
        verbose_name_plural = 'KitchenBodies'

    

class Team(models.Model):
    name = models.CharField('Team name', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'



class TeamImage(models.Model):
    name = models.CharField('TeamImage name', max_length=50)
    about = models.TextField('TeamImage about')
    img = models.ImageField('TeamImage image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TeamImage'
        verbose_name_plural = 'TeamImages'



class Newsletter(models.Model):
    name = models.CharField('Newsletter name', max_length=50)
    name1 = models.CharField('Newsletter name1', max_length=50)
    about = models.TextField('Newsletter about')
    about1 = models.TextField('Newsletter about1')
    img = models.ImageField('Newsletter image', upload_to='media', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'



class StoryFoot(models.Model):
    name = models.CharField('StoryFoot name', max_length=50)
    name1 = models.CharField('StoryFoot name1', max_length=50)
    name2 = models.CharField('StoryFoot name2', max_length=50)
    name3 = models.CharField('StoryFoot name3', max_length=50)
    name4 = models.CharField('StoryFoot name4', max_length=50)
    about = models.TextField('StoryFoot about')
    about1 = models.TextField('StoryFoot about1')
    about2 = models.TextField('StoryFoot about2')
    about3 = models.TextField('StoryFoot about3')
    about4 = models.TextField('StoryFoot about4')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'StoryFoot'
        verbose_name_plural = 'StoryFoots'



class StoryRevers(models.Model):
    name = models.CharField('StoryRevers name', max_length=50)
    name1 = models.CharField('StoryRevers name1', max_length=50)
    about = models.TextField('StoryRevers about')
    about1 = models.TextField('StoryRevers about1')
    about2 = models.TextField('StoryRevers about2')
    about3 = models.TextField('StoryRevers about3')
    about4 = models.TextField('StoryRevers about4')
    about5 = models.TextField('StoryRevers about5')
    about6 = models.TextField('StoryRevers about6')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'StoryRevers'
        verbose_name_plural = 'StoryReverses'



    


class MenuHeader(models.Model):
    name = models.CharField('MenuHeader name', max_length=50)
    about = models.TextField('MenuHeader about')
    about1 = models.TextField('MenuHeader about1')
    about2 = models.TextField('MenuHeader about2')
    about3 = models.TextField('MenuHeader about3')
    about4 = models.TextField('MenuHeader about4')
    about5 = models.TextField('MenuHeader about5')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'MenuHeader'
        verbose_name_plural = 'MenuHeaders'



class MenuHead(models.Model):
    name = models.CharField('MenuHead name', max_length=50)
    about = models.TextField('MenuHead about')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'MenuHead'
        verbose_name_plural = 'MenuHeads'



class Breakfast(models.Model):
    name = models.CharField('Breakfast name', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Breakfast'
        verbose_name_plural = 'Breakfasts'



class BreakfastImage(models.Model):
    name = models.CharField('BreakfastImage name', max_length=30)
    name1 = models.CharField('BreakfastImage name1', max_length=30)
    about = models.TextField('BreakfastImage about')
    about1 = models.TextField('BreakfastImage about1')
    img = models.ImageField('BreakfastImage image', upload_to='media', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'BreakfastImage'
        verbose_name_plural = 'BreakfastImages'



class Lunch(models.Model):
    name = models.CharField('Lunch name', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Lunch'
        verbose_name_plural = 'Lunchs'



class LunchImage(models.Model):
    name = models.CharField('LunchImage name', max_length=50)
    name1 = models.CharField('LunchImage name1', max_length=50)
    about = models.TextField('LunchImage about')
    about1 = models.TextField('LunchImage about1', blank=True)
    about2 = models.TextField('LunchImage about2')
    img = models.ImageField('LunchImage image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'LunchImage'
        verbose_name_plural = 'LunchImages'



class Dinner(models.Model):
    name = models.CharField('Dinner name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Dinner'
        verbose_name_plural = 'Dinners'



class DinnerImage(models.Model):
    name = models.CharField('DinnerImage name', max_length=50)
    name1 = models.CharField('DinnerImage name1', max_length=50)
    about = models.TextField('DinnerImage about')
    about1 = models.TextField('DinnerImage about1')
    img = models.ImageField('DinnerImage image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'DinnerImage'
        verbose_name_plural = 'DinnerImages'



class MenuFoot(models.Model):
    name = models.CharField('MenuFoot name', max_length=50)
    name1 = models.CharField('MenuFoot name1', max_length=50)
    name2 = models.CharField('MenuFoot name2', max_length=50)
    name3 = models.CharField('MenuFoot name3', max_length=50)
    name4 = models.CharField('MenuFoot name4', max_length=50)
    about = models.TextField('MenuFoot about')
    about1 = models.TextField('MenuFoot about1')
    about2 = models.TextField('MenuFoot about2')
    about3 = models.TextField('MenuFoot about3')
    about4 = models.TextField('MenuFoot about4')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'MenuFoot'
        verbose_name_plural = 'MenuFoots'



class MenuRevers(models.Model):
    name = models.CharField('MenuRevers name', max_length=50)
    name1 = models.CharField('MenuRevers name1',max_length=50)
    about = models.TextField('MenuRevers about')
    about1 = models.TextField('MenuRevers about1')
    about2 = models.TextField('MenuRevers about2')
    about3 = models.TextField('MenuRevers about3')
    about4 = models.TextField('MenuRevers about4')
    about5 = models.TextField('MenuRevers about5')
    about6 = models.TextField('MenuRevers about6')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'MenuRevers'
        verbose_name_plural = 'MenuReverses'





class UpdateHeader(models.Model):
    name = models.CharField('UpdateHeader name', max_length=30)
    about = models.TextField('UpdateHeader about')
    about1 = models.TextField('UpdateHeader about1')
    about2 = models.TextField('UpdateHeader about2')
    about3 = models.TextField('UpdateHeader about3')
    about4 = models.TextField('UpdateHeader about4')
    about5 = models.TextField('UpdateHeader about5')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'UpdateHeader'
        verbose_name_plural = 'UpdateHeaders'    



class UpdateHead(models.Model):
    name = models.CharField('UpdateHead name', max_length=50)
    about = models.TextField('UpdateHead about')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'UpdateHead'
        verbose_name_plural = 'UpdateHeads'



class UpdatUpdate(models.Model):
    name = models.CharField('UpdateUpdate name', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'UpdateUpdate'
        verbose_name_plural = 'UpdateUpdates'



class UpdateImage(models.Model):
    name = models.CharField('UpdateImage name', max_length=50)
    about = models.TextField('UpdateImage about')
    img = models.ImageField('UpdateImage image', upload_to="media")

    def __str__(self):
        return self.name

    verbose_name = 'UpdateImage'
    verbose_name_plural = 'UpdateImages'



class New(models.Model):
    name = models.CharField('New name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'



class NewImage(models.Model):
    name = models.CharField('NewImage name', max_length=50)
    about = models.TextField('NewImage about',)
    about1 = models.TextField('NewImage about1')
    img = models.ImageField('NewImage image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'NewImage'
        verbose_name_plural = 'NewImages'



class UpdateFoot(models.Model):
    name = models.CharField('UpdateFoot name', max_length=50)
    name1 = models.CharField('UpdateFoot name1', max_length=50, null=True)
    name2 = models.CharField('UpdateFoot name2', max_length=50, null=True)
    name3 = models.CharField('UpdateFoot name3', max_length=50, null=True)
    name4 = models.CharField('UpdateFoot name4', max_length=50, null=True)
    about = models.TextField('UpdateFoot about')
    about1 = models.TextField('UpdateFoot about1')
    about2 = models.TextField('UpdateFoot about2')
    about3 = models.TextField('UpdateFoot about3')
    about4 = models.TextField('UpdateFoot about4')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'UpdateFoot'
        verbose_name_plural = 'UpdateFoots'



class UpdateRevers(models.Model):
    name = models.CharField('UpdateRevers name', max_length=50)
    name1 = models.CharField('UpdateRevers name1', max_length=50)
    about = models.TextField('UpdateRevers about')
    about1 = models.TextField('UpdateRevers about1')
    about2 = models.TextField('UpdateRevers about2')
    about3 = models.TextField('UpdateRevers about3')
    about4 = models.TextField('UpdateRevers about4')
    about5 = models.TextField('UpdateRevers about5')
    about6 = models.TextField('UpdateRevers about6')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'UpdateRevers'
        verbose_name_plural = 'UpdateReverses'
    





class ContactHeader(models.Model):
    name = models.CharField('ContactHeader name', max_length=50)
    about = models.TextField('ContactHeader about')
    about1 = models.TextField('ContactHeader about1')
    about2 = models.TextField('ContactHeader about2')
    about3 = models.TextField('ContactHeader about3')
    about4 = models.TextField('ContactHeader about4')
    about5 = models.TextField('ContactHeader about5')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ContactHeader'
        verbose_name_plural = 'ContactHeaders'



class ContactHead(models.Model):
    name = models.CharField('ContactHead name', max_length=50)
    about = models.TextField('ContactHead about')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ContactHead'
        verbose_name_plural = 'ContactHeads'



class Message(models.Model):
    name = models.CharField('Message name', max_length=50)
    name1 = models.CharField('Message name1', max_length=50, null=True)
    name2 = models.CharField('Message name2', max_length=50, null=True)
    name3 = models.CharField('Message name3', max_length=50, null=True)
    name4 = models.CharField('Message name4', max_length=50, null=True)
    name5 = models.CharField('Message name5', max_length=50, null=True)
    name6 = models.CharField('Message name6', max_length=50, null=True)
    name7 = models.CharField('Message name7', max_length=50, null=True)
    name8 = models.CharField('Message name8', max_length=50, null=True)
    about = models.TextField('Message about', null=True)
    about1 = models.TextField('Message about1', null=True)
    about2 = models.TextField('Message about2', null=True)
    about3 = models.TextField('Message about3', null=True)   

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'



class ContactFoot(models.Model):
    name = models.CharField('ContactFoot name', max_length=50)
    name1 = models.CharField('ContactFoot name1', max_length=50)
    name2 = models.CharField('ContactFoot name2', max_length=50)
    name3 = models.CharField('ContactFoot name3', max_length=50)
    name4 = models.CharField('ContactFoot name4', max_length=50)
    about = models.TextField('ContactFoot about')
    about1 = models.TextField('ContactFoot about1')
    about2 = models.TextField('ContactFoot about2')
    about3 = models.TextField('ContactFoot about3')
    about4 = models.TextField('ContactFoot about4')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ContactFoot'
        verbose_name_plural = 'ContactFoots'



class ContactRevers(models.Model):
    name = models.CharField('ContactRevers name', max_length=50)
    name1 = models.CharField('ContactRevers name1', max_length=50)
    about = models.TextField('ContactRevers about')
    about1 = models.TextField('ContactRevers about1')
    about2 = models.TextField('ContactRevers about2')
    about3 = models.TextField('ContactRevers about3')
    about4 = models.TextField('ContactRevers about4')
    about5 = models.TextField('ContactRevers about5')
    about6 = models.TextField('ContactRevers about6')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ContactRevers'
        verbose_name_plural = 'ConatactReverses'



class DetailHeader(models.Model):
    name = models.CharField('DetailHeader name', max_length=30)
    about = models.TextField('DetailHeader about')
    about1 = models.TextField('DetailHeader about1')
    about2 = models.TextField('DetailHeader about2')
    about3 = models.TextField('DetailHeader about3')
    about4 = models.TextField('DetailHeader about4')
    about5 = models.TextField('DetailHeader about5')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'DetailHeader'
        verbose_name_plural = 'DetailHeaders'



class DetailHead(models.Model):
    name = models.CharField('DetailHead name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'DetailHead'
        verbose_name_plural = 'DetailHeads'



class DetailBody(models.Model):
    name = models.CharField('DetailBody name', max_length=60)
    name1 = models.CharField('DetailBody name1', max_length=60)
    about = models.TextField('DetailBody about')
    about1 = models.TextField('DetailBody about1')
    about2 = models.TextField('DetailBody about2')
    about3 = models.TextField('DetailBody about3')
    about4 = models.TextField('DetailBody about4')
    about5 = models.TextField('DetailBody about5')
    about6 = models.TextField('DetailBody about6')
    img = models.ImageField('DetailBody image', upload_to='media')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'DetailBody'
        verbose_name_plural = 'DetailBodies'



class DetailComment(models.Model):
    name = models.CharField('DetailComment name', max_length=50)
    name1 = models.CharField('DetailComment name1', max_length=50)
    name2 = models.CharField('DetailComment name2', max_length=50)
    name3 = models.CharField('DetailComment name3', max_length=50)
    about = models.TextField('DetailComment about')
    about1 = models.TextField('DetailComment about1')
    about2 = models.TextField('DetailComment about2')
    about3 = models.TextField('DetailComment about3')
    img = models.ImageField('DetailComment image', upload_to='media')
    img1 = models.ImageField('DetailComment image1', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'DetailComment'
        verbose_name_plural = 'DetailComments'



class DetailNew(models.Model):
    name = models.CharField('DetailNew name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'DetailNew'
        verbose_name_plural = 'DetailNews'



class DetailNewImage(models.Model):
    name = models.CharField('DetailNewImage name', max_length=50, null=True)
    about = models.TextField('DetailNewImage about', null=True)
    about1 = models.TextField('DetailNewImage about1', null=True)
    img = models.ImageField('DetailNewImage image', upload_to='media', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'DetailNewImage'
        verbose_name_plural = 'DetailNewImages'



class DetailNewsletter(models.Model):
    name = models.CharField('DetailNewsletter name', max_length=50)
    name1 = models.CharField('DetailNewsletter name1', max_length=50)
    about = models.TextField('DetailNewsletter about')
    about1 = models.TextField('DetailNewletter about1')
    img = models.ImageField('DetailNewsletter image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'DetailNewsletter'
        verbose_name_plural = 'DetailNewsletters'



class DetailFoot(models.Model):
    name = models.CharField('DetailFoot name', max_length=50)
    name1 = models.CharField('DetailFoot name1', max_length=50)
    name2 = models.CharField('DetailFoot name2', max_length=50)
    name3 = models.CharField('DetailFoot name3', max_length=50)
    name4 = models.CharField('DetailFoot name4', max_length=50)
    about = models.TextField('DetailFoot about')
    about1 = models.TextField('DetailFoot about1')
    about2 = models.TextField('DetailFoot about2')
    about3 = models.TextField('DetailFoot about3')
    about4 = models.TextField('DetailFoot about4')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'DetailFoot'
        verbose_name_plural = 'DetailFoots'



class DetailRevers(models.Model):
    name = models.CharField('DetailRevers name', max_length=50)
    name1 = models.CharField('DetailRevers name1', max_length=50)
    about = models.TextField('DetailRevers about')
    about1 = models.TextField('DetailRevers about1')
    about2 = models.TextField('DetailRevers about2')
    about3 = models.TextField('DetailRevers about3')
    about4 = models.TextField('DetailRevers about4')
    about5 = models.TextField('DetailRevers about5')
    about6 = models.TextField('DetailRevers about6')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'DetailRevers'
        verbose_name_plural = 'DetailReverses'


    