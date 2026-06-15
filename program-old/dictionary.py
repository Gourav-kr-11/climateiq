#key:value pair
#mutable
#unordered
#key single
dict={
  "name":"Gourav",
  "cgpa":9.4,
  "marks":23,
  "subject":["english","hindi"],
  "topics":("grammer","litrature")
}

print(dict)
print(dict["name"])
dict["cgpa"]=7.9

null_dict={}
null_dict["name"]="Ace"
print(null_dict)

student ={
  "name":"rahul kumar",
  "subject" : {
    "phy":97,
    "chem":98

  }
}

print(student["subject"]["chem"])

student.update({"city":"delhi"})
print(student)

# myDict.keys() -> return all keys
# myDict.value() -> return all values
# myDict.items() -> return all (key,value) pairs as tuples
#myDict.get("key")->return the key according to value
#myDict.update(newDict)->inserts the specified items to the diagonal
