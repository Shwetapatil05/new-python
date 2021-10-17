#--------------------------------------------------------------------------------------------
# Description : Comparison between Pass Statement and continue statement
# About       : Pass has no functionality. But it is syntactically correct.
#--------------------------------------------------------------------------------------------

y = [1,2,4,5];
for i in y:
  if(i is 2):
    print(i);
    pass;
  if(i is 2):
    print("Outside Pass statement",i);

for i in y:
  if(i is 4):
    print(i);
    continue;
  if(i is 4):
    print("Outside Pass statement",i);
