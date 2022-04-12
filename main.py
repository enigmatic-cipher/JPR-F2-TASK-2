"""
Create a class ContactDetails with the fields email address, mobile number, landline number. All the three fields are of type String. Create an object of the class ContactDetails and print it.
"""

class contactDetails:
  def __init__(self,email,mobile,landline):
    self.email = email
    self.mobile = mobile
    self.landline = landline

  def __str__(self):
    return "Contact Detail: Email address: {}, Mobile Number: {} and Landline: {}".format(self.email, self.mobile, self.landline)

cd = contactDetails("xyg@xyg.com","1234567890","012-1234567")
print(cd)
