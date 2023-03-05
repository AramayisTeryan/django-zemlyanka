from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Header, Head, HeadCarusel, Video, Menu, MenuAbout, Event, EventTwoImage, EventFoot, HomeFoot, HomeRevers, StoryHeader, Kitchen, KitchenBody, Team, TeamImage, Newsletter, StoryFoot, StoryRevers, MenuHeader, MenuHead, Breakfast, BreakfastImage, Lunch, LunchImage, Dinner, DinnerImage, MenuFoot, MenuRevers, UpdateHeader, UpdateHead, UpdatUpdate, UpdateImage, New, NewImage, UpdateFoot, UpdateRevers, ContactHeader, ContactHead, Message, ContactFoot, ContactRevers, DetailHeader, DetailHead, DetailBody, DetailComment, DetailNew, DetailNewImage, DetailNewsletter, DetailFoot, DetailRevers

# Create your views here.

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        header = Header.objects.all()
        head = Head.objects.all()
        headcarusel = HeadCarusel.objects.all()
        video = Video.objects.all()
        menu = Menu.objects.all()
        menuabout = MenuAbout.objects.all()
        event = Event.objects.all()
        eventtwoimage = EventTwoImage.objects.all()
        eventfoot = EventFoot.objects.all()
        homefoot = HomeFoot.objects.all()
        homerevers = HomeRevers.objects.all()
        return render(request, self.template_name, {'header':header, 'head':head, 'headcarusel':headcarusel, 'video':video, 'menu':menu, 'menuabout':menuabout, 'event':event, 'eventtwoimage':eventtwoimage, 'eventfoot':eventfoot, 'homefoot':homefoot, 'homerevers':homerevers})



class StoryListView(ListView):
    template_name = 'about.html'

    def get(self, request):
        storyheader = StoryHeader.objects.all()
        kitchen = Kitchen.objects.all()
        kitchenbody = KitchenBody.objects.all()
        team = Team.objects.all()
        teamimage = TeamImage.objects.all()
        newsletter = Newsletter.objects.all()
        storyfoot = StoryFoot.objects.all()
        storyrevers = StoryRevers.objects.all()
        return render(request, self.template_name, {'storyheader':storyheader, 'kitchen':kitchen, 'kitchenbody':kitchenbody, 'team':team, 'teamimage':teamimage, 'newsletter':newsletter, 'storyfoot':storyfoot, 'storyrevers':storyrevers})



class MenuListView(ListView):
    template_name = 'menu.html'

    def get(self, request):
        menuheader = MenuHeader.objects.all()
        menuhead = MenuHead.objects.all()
        breakfast = Breakfast.objects.all()
        breakfastimage = BreakfastImage.objects.all()
        lunch = Lunch.objects.all()
        lunchimage = LunchImage.objects.all()
        dinner = Dinner.objects.all()
        dinnerimage = DinnerImage.objects.all()
        menufoot = MenuFoot.objects.all()
        menurevers = MenuRevers.objects.all()
        return render(request, self.template_name, {'menuheader':menuheader, 'menuhead':menuhead, 'breakfast':breakfast, 'breakfastimage':breakfastimage, 'lunch':lunch, 'lunchimage':lunchimage, 'dinner':dinner, 'dinnerimage':dinnerimage, 'menufoot':menufoot, 'menurevers':menurevers})



class UpdateListView(ListView):
    template_name = 'news.html'

    def get(self, request):
        updateheader = UpdateHeader.objects.all()
        updatehead = UpdateHead.objects.all()
        updateupdate = UpdatUpdate.objects.all()
        updateimage = UpdateImage.objects.all()
        new = New.objects.all()
        newimage = NewImage.objects.all()
        updatefoot = UpdateFoot.objects.all()
        updaterevers = UpdateRevers.objects.all()
        return render(request, self.template_name, {'updateheader':updateheader, 'updatehead':updatehead, 'updateupdate':updateupdate, 'updateimage':updateimage, 'new':new, 'newimage':newimage, 'updatefoot':updatefoot, 'updaterevers':updaterevers})



class ContactListView(ListView):
    template_name = 'contact.html'

    def get(self, request):
        contactheader = ContactHeader.objects.all()
        contacthead = ContactHead.objects.all()
        message = Message.objects.all()
        contactfoot = ContactFoot.objects.all()
        contactrevers = ContactRevers.objects.all()
        return render(request, self.template_name, {'contactheader':contactheader, 'contacthead':contacthead, 'message':message, 'contactfoot':contactfoot, 'contactrevers':contactrevers})



class DetailListView(ListView):
    template_name = 'news-detail.html'

    def get(self, request):
        detailheader = DetailHeader.objects.all()
        detailhead = DetailHead.objects.all()
        detailbody = DetailBody.objects.all()
        detailcomment = DetailComment.objects.all()
        detailnew = DetailNew.objects.all()
        detailnewimage = DetailNewImage.objects.all()
        detailnewsletter = DetailNewsletter.objects.all()
        detailfoot = DetailFoot.objects.all()
        detailrevers = DetailRevers.objects.all()
        return render(request, self.template_name, {'detailheader':detailheader, 'detailhead':detailhead, 'detailbody':detailbody, 'detailcomment':detailcomment, 'detailnew':detailnew, 'detailnewimage':detailnewimage, 'detailnewsletter':detailnewsletter, 'detailfoot':detailfoot, 'detailrevers': detailrevers})

