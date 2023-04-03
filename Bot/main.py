
from Booking.booking import Booking

#context manager: __Exit__ teardown 
# with Booking(teardown=True) as bot:
with Booking(teardown=False) as bot:
    bot.land_first_page()
    bot.change_currency()
    bot.selectPlaceToGo('New York')
    # print('Exiting')

# inst = Booking()
# inst.land_first_page()