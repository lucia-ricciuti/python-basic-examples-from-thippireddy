# Define the list
countryList = ["Italy", "France", "Germany"]
print(countryList)

# Add a country at the end
countryList.append("Spain")
print(countryList)

# Remove by index
countryList.remove(countryList[0])
print(countryList)

# Add a country in the middle
countryList.insert(1, "Portugal")
print(countryList)

# Define the set
countrySet = {"Italy", "France", "Germany"}
print(countrySet)

# Add a country at the end
countrySet.update(["Spain"])
print(countrySet)

# Remove by index
countrySet.remove("Italy")
print(countrySet)

# Add a country in the middle
# Not possible
