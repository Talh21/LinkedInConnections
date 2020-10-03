from Bot.withdraw import *
from Bot.add_connections import *

if __name__ == '__main__':
    intro()
    withdraw_or_adding = input("""Do you want to add connections or withdraw invites? 
1) Add connections
2) Withdraw invites
Choice: """)

    while is_choice_is_valid(withdraw_or_adding) is False:
        withdraw_or_adding = input("""Not a valid option. Please Try again:\n
1) Add connections
2) Withdraw invites
Choice: """)

    if withdraw_or_adding == "1":
        Bot = LinkedInAdd()
        Bot.main()
    else:
        Bot = LinkedInWithdraw()
        Bot.main()
