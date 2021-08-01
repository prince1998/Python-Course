# Write a Python script to concatenate following dictionaries to create a new one. 

def concatenate_dictionaries(dic1,dic2,dic3):
    dic_result = {}
    for d in (dic1, dic2, dic3): 
        dic_result.update(d)
    return dic_result

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic_result = concatenate_dictionaries(dic1,dic2,dic3)
print(f"Concatenated dictionary: {dic_result}")