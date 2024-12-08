data = {
  "employees": [
    {
      "firstName": "John",
      "lastName": "Doe"
    },
    {
      "firstName": "Anna",
      "lastName": "Smith"
    },
    {
      "firstName": "Peter",
      "lastName": "Jones"
    }
  ]
}

# print(data.keys())
# print(data.values())
x = data['employees'][1].keys()
y = data['employees'][1].values()
print(x)
print(y)

z =  data['employees'][0]['firstName']
print(z)

a = list(data['employees'][0].keys())[0]
print(a)

