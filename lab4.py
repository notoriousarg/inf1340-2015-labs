#!/usr/bin/env python3

""" Graded Lab #4 for Inf1340, Fall 2015

    This program computes federal and provincial sales tax.
    Assume that the provincial sales tax is 5 percent and
    the federal sales tax is 2.5 percent. It displays the
    amount of the purchase, the provincial sales tax, the
    federal sales tax, the total tax, and the total of the
    sale.
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Rewrite this code to use global constants, local variables and functions
# Output the text to a file instead of printing it

Provincial_tax = .05
Federal_tax = 0.25


def bill_of_sale(purchase):
    # print ("Amount of purchase: {0:.2f}".format(purchase))
    # print ("Provincial tax: {0:.2f}".format(purchase * .05))
    #print ("Federal tax: {0:.2f}".format(purchase * .025))
    #print ("Total tax: {0:.2f}".format(purchase * .075))
    #print ("Total sale: {0:.2f}".format(purchase * 1.075))



    def amount_of_purchase(purchase):
        return ("Amount of purchase: {0:.2f}".format(purchase))

    def provincial_tax(purchase):
        return ("Provincial tax: {0:.2f}".format(purchase * Provincial_tax))

    def federal_tax(purchase):
        return ("Federal tax: {0:.2f}".format(purchase * Federal_tax))

    def total_tax(purchase):
        return ("Total tax: {0:.2f}".format(purchase * (Provincial_tax + Federal_tax)))

    def total_sale(purchase):
        return ("Total sale: {0:.2f}".format(purchase * (1 + Provincial_tax + Federal_tax)))

    file_name = "lab4.txt"

    with open(file_name, 'w') as output_file:
        output_file.write(amount_of_purchase(purchase) + "\n")
        output_file.write(provincial_tax(purchase) + "\n")
        output_file.write(federal_tax(purchase) + "\n")
        output_file.write(total_tax(purchase) + "\n")
        output_file.write(total_sale(purchase) + "\n")


bill_of_sale(50)

# def total_tax(purchase):
# provincial_tax_amount = purchase * Provincial_tax
#federal_tax_amount = purchase * Federal_tax
#total_tax_amount = provincial_tax_amount + federal_tax_amount

#def total_sale(purchase):
#purchase + total_tax_amount


#with open(file_name, 'w') as output_file:






#Amount of purchase = {0:.2f}".format(purchase))

