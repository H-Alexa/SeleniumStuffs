
from Booking.booking import Booking

#context manager: __Exit__ teardown 
# with Booking(teardown=True) as bot:
with Booking(teardown=False) as bot:
    
    bot.land_first_page()
    bot.change_currency()
    bot.selectPlaceToGo('New York')
    bot.selectDate('2023-04-23','2023-05-01')
    bot.select_adults(4)
    bot.submit()
    bot.apply_filtration()
    # print('Exiting')

# inst = Booking()
# inst.land_first_page()