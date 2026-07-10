#!/usr/bin/python3
def list_division(my_list_1,my_list_2,list_length):
 result=[]
 for i in range(list_length):
  div_result=0
  try:
   val1=my_list_1[i]
   val2=my_list_2[i]
   if not isinstance(val1,(int,float))or not isinstance(val2,(int,float)):
    print("wrong type")
    raise TypeError
   div_result=val1/val2
  except IndexError:
   print("out of range")
  except ZeroDivisionError:
   print("division by 0")
  except TypeError:
   pass
  finally:
   result.append(div_result)
 return result
