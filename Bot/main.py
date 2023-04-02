
from Booking.booking import Booking

#context manager: __Exit__ teardown 
# with Booking(teardown=True) as bot:
with Booking() as bot:
    bot.land_first_page()
    print('Exiting')

# inst = Booking()
# inst.land_first_page()