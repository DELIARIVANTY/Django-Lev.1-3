import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django
django.setup()

#fake Pop Script
import random
from second_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker
topics = ["Social", "Search", "marketplace", "News", "Games"]

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    
    for entry in range(N):
        
        #get
        top = add_topic()
        
        #create
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        
        #create
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        
        #create a fake access
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]
        
if __name__=="__main__":
    print("populating script...")
    populate(20)
    print("populating complete!")
    


