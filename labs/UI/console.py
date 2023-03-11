import domain.listMods as listing

def help_list():
    print("List of functions: "
          "\n ->> show_list :: {shows the list}"
          "\n ->> add :: {add a number to the end of the list} "
          "\n ->> insert :: {add a number at a given position of the list} "
          "\n ->> remove_number :: {removes a number from a given positon in the list} "
          "\n ->> remove_interval :: {removes a numbers in a given interval included in the list} "
          "\n ->> replace :: {replaces a number from a given position from the list} "
          "\n ->> prime :: {gets all the prime numbers from a given position to another from the list} "
          "\n ->> odd :: {gets all the odd numbers from a given position to another from the list} "
          "\n ->> sum :: {gets the sum of all the numbers from a given position to another from the list} "
          "\n ->> gcd :: {gets the greates common divisor of all the numbers from a given position to another from the list} "
          "\n ->> max :: {gets the biggest number of all the numbers from a given position to another from the list} "
          "\n ->> filter_prime :: {keeps only the prime numbers in the list} "
          "\n ->> filter_negative :: {keeps only the negative numbers in the list} "
          "\n ->> undo :: {undos the last oparation that modified the list, can be done multiple times, till it gets to the initial state of the list}"
          "\n ->> help :: {writes the list of functions}")

def coma():
      comm = input("\nInput command: ")
      if comm == "show_list":
            listing.lPrint()
      elif comm == "add":
            listing.save()
            listing.my_list = listing.utilities.add(listing.my_list, float(input("   Input value >>> ")))[:]
      elif comm == "insert":
            listing.save()
            listing.my_list = listing.utilities.insert(listing.my_list, int(input("   Input position >>> ")), float(input("   Input value >>> ")))[:]
      elif comm == "remove_number":
            listing.save()
            listing.my_list = listing.utilities.remove_element(listing.my_list, int(input("   Input position >>> ")))[:]
      elif comm == "remove_interval":
            listing.save()
            listing.my_list = listing.utilities.remove_interval(listing.my_list, int(input("   Input starting position >>> ")), int(input("   Input end position >>> ")))[:]
      elif comm == "replace":
            listing.save()
            listing.my_list = listing.utilities.replace(listing.my_list, int(input("   Input old value >>> ")), int(input("   Input new value >>> ")))[:]
      elif comm == "prime":
            print(listing.utilities.prime(listing.my_list, int(input("   Input starting position >>> ")), int(input("   Input end position >>> "))))
      elif comm == "odd":
            print(listing.utilities.odd(listing.my_list, int(input("   Input starting position >>> ")), int(input("   Input end position >>> "))))
      elif comm == "sum":
            print(listing.utilities.sequence_sum(listing.my_list, int(input("   Input starting position >>> ")), int(input("   Input end position >>> "))))
      elif comm == "gcd":
            print(listing.utilities.sequence_gcd(listing.my_list, int(input("   Input starting position >>> ")), int(input("   Input end position >>> "))))
      elif comm == "max":
            print(listing.utilities.sequence_max(listing.my_list, int(input("   Input starting position >>> ")), int(input("   Input end position >>> "))))
      elif comm == "filter_prime":
            listing.save()
            listing.my_list = listing.utilities.filter_prime(listing.my_list)[:]
      elif comm == "filter_negative":
            listing.save()
            listing.my_list = listing.utilities.filter_negative(listing.my_list)[:]
      elif comm == "undo":
            listing.undo()
      else:
            print("::Invalid input::")
      coma()


