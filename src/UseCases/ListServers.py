from os import system
from Utils import print_table

def list_servers(serverController):
  system('clear')
  print_table(serverController.list_servers())