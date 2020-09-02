"""
ISCG5421 - Learning logging

Kris Pritchard / @krisrp
Sep 2020

"""

import logging
# set logging level
logging.basicConfig(level=logging.CRITICAL)

logging.debug('debug')  # 5
logging.info('info')  # 4
logging.warning('warning')  # 3
logging.error('error')  # 2
logging.critical('critical')  # 1


class BankAccount:
    """
    checkbalance - debug
    withdraw - info
    hacked - critical
    """
    def checkbalance(self):
        """checks the user balance"""
        logging.debug('Checked user balance')

    def withdraw(self):
        """withdraws money"""
        logging.info('withdraw money')

    def hacked(self):
        """account has been hacked"""
        logging.critical('account was hacked')

    
