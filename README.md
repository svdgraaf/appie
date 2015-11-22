# appie
Python Library for the (hidden) Ah.nl REST interface

Very much a Work in Progress

# Installation
  pip install appie

# Usage
  import appie

  client = appie.Api(username, password)
  client.add('wi191924')

  print client.list

# Todo
Lots, currently it only supports adding an item, and viewing the current shopping list, there are many more calls available.
