
"""
28th march 2020
Author: Abhishek singh
topics:- inheritance,super(),multiple inheritance, overridding,mixin class
"""

class ContactList(list):
    def search(self, name):
        ''' return thr contacts which contaian search values into their name '''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts
    
class Contact:
    all_contacts = ContactList()

    def __init__(self, name , email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)



# c1 = Contact("abhi", "abc@gmail.com") #test data
# c2 = Contact("shek", "gmail@gmail.com") #test data

# print([c.name for c in Contact.all_contacts.search('z')]) #test data


"""class Friend(Contact):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


#this we we are using duplicate code in friend class as we have this in parent Contact class
# so whats the fun of using inheritance if we cannot call the name and email from the parent class??
  #in order to do so we need  super() function which allows us to call the codes from parent class directly into the 
  # chile class 
"""



