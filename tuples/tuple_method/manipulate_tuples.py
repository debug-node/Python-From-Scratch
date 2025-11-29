countries = ("india","china","russia","pakistan","japan")
temp = list(countries)      # MANIPULATE TUPLE TO LIST
temp.append("nepal")        # ADD NEW ITEMS
temp.pop(4)                 # REMOVE ITEMS OF GIVEN INDEX
temp[4]="bhutan"            # CHANGE ITEMS OF GIVEN INDEX
print(temp)
countries = tuple(temp)     # LIST TO TUPLE
print(countries)