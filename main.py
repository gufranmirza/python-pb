#! /usr/bin/python

import addressbook_pb2
import sys

address_book = addressbook_pb2.AddressBook()

# Person 1
person1 = address_book.people.add()
person1.id = 1001
person1.name ="John Doe"
person1.email = "jdoe@example.com"
phone_number1 = person1.phones.add()
phone_number1.number = "12345-67890"
phone_number1.type = addressbook_pb2.Person.PhoneType.WORK

# Person 2
person2 = address_book.people.add()
person2.id = 1002
person2.name ="Alex"
person2.email = "alex@example.com"
phone_number2 = person2.phones.add()
phone_number2.number = "100122-5889"
phone_number2.type = addressbook_pb2.Person.PhoneType.WORK

# let's stringity our Address object so
# that we can use it transfer the data across services
data = address_book.SerializeToString()

# printing out our raw protobuf object
print "Raw data: ", data


# let's go the other way and parse
# our raw protobuf object we can modify
# and use
address_book = addressbook_pb2.AddressBook()
address_book.ParseFromString(data)


for person in address_book.people:
    print "==========================="
    print "Person ID:", person.id
    print "Name:", person.name
    print "E-mail:", person.email

    for phone_number in person.phones:
      if phone_number.type == addressbook_pb2.Person.PhoneType.MOBILE:
        print "Mobile phone #: ",
      elif phone_number.type == addressbook_pb2.Person.PhoneType.HOME:
        print "Home phone #: ",
      elif phone_number.type == addressbook_pb2.Person.PhoneType.WORK:
        print "Work phone #: ",
      print phone_number.number
