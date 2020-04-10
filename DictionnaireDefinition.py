class DictionnaireOrdonne:
    """ This class will provide all feature of a dict class,
    besides it will provide in addition a sort methode than can be called"""
    
    def __init__(self, dict_ordo = None, **dictionnaire):
        if(dict_ordo == None):
            self._keys = list(dictionnaire.keys())
            self._values = list(dictionnaire.values())
        else:
            self.__dict__= dict(dict_ordo.__dict__)
        # self.dict = dict(zip(self._keys,self._values))
        self.iter_key, self.iter_values = iter(self._keys),iter(self._values)

    def __getitem__(self, key):
        index = self._keys.index(key)
        return self._values[index]

    def __setitem__(self, key, value):
        # self.dict[key]=value # the dictionary handle all alone the exesting or not of the variable
    
        if key in self._keys:
            index = self._keys.index(key)
            self._values[index]=value
        else:
            self._keys.append(key)
            self._values.append(value)
        
    def __delitem__(self, key):
        # del self.dict[key]
        index = self._keys.index(key)
        del self._values[index]
        del self._keys[index]

    def __contains__(self, key):
        return key in self._keys

    def __len__(self):
        return len(self._keys)

    def sort(self):
        dictionnaire =  dict(zip(self._keys,self._values))
        self._keys.sort()
        for i,elt in enumerate(self._keys):
            self._values[i]=dictionnaire[elt]
        return dict(zip(self._keys,self._values))

    def reverse(self):
        dictionnaire =  dict(zip(self._keys,self._values))
        self._keys.sort(reverse=True)
        for i,elt in enumerate(self._keys):
            self._values[i]=dictionnaire[elt]
        return dict(zip(self._keys,self._values))

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iter_key)

    def keys(self):
        return self._keys

    def values(self):
        return self._values
    
    def items(self):
        for key,value in zip(self._keys, self._values):
            yield (key,value)

    def __add__(self, other):
        for key, value in other.items():
            self[key] = value
        return self

    def __str__(self):
        return str(dict(zip(self._keys,self._values)))#str({ self._keys[i]:self._values[i] for i in range(len(self._keys)) })

dict1 = DictionnaireOrdonne()
print(dict1)
dict2 = DictionnaireOrdonne(hinda=26,ayoub=29,taha=10)
dict3 = DictionnaireOrdonne(dict2)
print(dict3["taha"])
dict3["mohamed"] = 20
print(dict3)
#del(dict3["ayoub"])
print("ayoub" in dict2)
print(f" longeur est : {len(dict3)}")
print(dict3.sort())
print(dict3.reverse())
for key,elt in dict3.items():
    print(f"------ element of {key} is {elt}")
print(dict3.keys())
print(dict3.values())
############ TEST addition
dict1["badr"] = 23; dict1["kamilia"] = 34
print (dict3 + dict1)