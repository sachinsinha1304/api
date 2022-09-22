from .models import item,Biddings,SoldItems
from datetime import date
from django_cron import CronJobBase, Schedule

# def my_scheduled_job(request):
#     day = date.today()
#     data = item.objects.filter(closingDate = day)
#     for i in data:

#         # getting the object with greatest bid
#         obj = Biddings.objects.filter(itemId = i.id).order_by("-bidd")[:1]

#         # now storing the data in SoldItems table
#         for val in obj:
#             pr = val.bidd
#             cust_id = val.custId

#         s = SoldItems(itemId = i, custId = cust_id, price = pr)
#         s.save()

#         # changing status of item as sold
#         file = item.objects.get(id = i.id)
#         file.status = True
#         file.save()

#         # to removing the bids made on said item
#         Biddings.objects.filter(itemId = i.id).delete()

# def test_job(request):
#     file = open(r"test.txt",'a')
#     file.close()



class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 1 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'api.my_cron_job'    # a unique code
    

    def do(self):
        file = open(r'file.txt','a')
        file.write('i am happy')
        print('hello')
        file.close()
