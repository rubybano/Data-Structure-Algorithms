# -*- coding: utf-8 -*-
"""insertnewnode.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fQJnZQeHDAix6zwGU1ndNjPbtFAZR0Id
"""

#node class
class node:
  def__init__(self,data):
    self.data=data
    self.next=None

#creating linked list class
class Linkedlist:
  def__init__(self):
    self.start=None
#Function to insert new node at last
  def insertlast(self,value):
    newNode=node(value)
    if (self.start==Node):
      self.start=newNode
    else:
      temp=self.start
      while temp.next!=None:
        temp=temp.next
      temp.next=newNode

