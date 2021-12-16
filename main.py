import requests
import time


def getData(URL,params):
    r = requests.get(url=URL, params=params)
    data = r.json()
    return data

def validation(object,list_object_keys):
    isCorrect=True
    for ok in list_object_keys:
        vk=validationKey(object,ok)
        if(vk==False):
            isCorrect=False
    return isCorrect

def validationKey(obj, object_key):
    # For keys validation

    v = object_key["key"] in obj
    if(v==True):
        if(object_key["child"]!=False):
            return validationKey(obj[object_key["key"]],object_key["child"])
        else:
            return True

    else:
        return False




def createKeys():
    list=[]
    object_key={}

    object_key["key"]="is_answered"
    object_key["child"] = False
    list.append(object_key.copy())

    object_key["key"]="view_count"
    object_key["child"] = False
    list.append(object_key.copy())

    object_key["key"] = "creation_date"
    object_key["child"] = False
    list.append(object_key.copy())


    object_key_child = {}
    object_key_child["key"]="reputation"
    object_key_child["child"] = False

    object_key["key"] = "owner"
    object_key["child"] = object_key_child
    list.append(object_key.copy())

    return list


def main():
    URL = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
    data=getData(URL,{})
    items=data["items"]

    #Objects declaration
    lower_views={}
    lower_views["index"]=-1
    lower_views["data"]={}
    lower_views["score"]=len(items)*items[0]["view_count"]+1 if len(items)>0 else 0

    lower_creation_date={}
    lower_creation_date["index"]=-1
    lower_creation_date["data"]={}
    lower_creation_date["date"]=time.time()

    most_creation_date={}
    most_creation_date["index"]=-1
    most_creation_date["data"]={}
    most_creation_date["date"]=0

    most_owner_reputation={}
    most_owner_reputation["index"]=-1
    most_owner_reputation["data"]={}
    most_owner_reputation["reputation"]=0

    answered = 0
    nonanswered = 0
    object_keys_list=createKeys()

    for i in range(len(items)):
        item=items[i]

        isCorrect=validation(item,object_keys_list)


        if(isCorrect==True):
            #Answered score
            if(item["is_answered"]):
                answered=answered+1
            else:
                nonanswered=nonanswered+1

            #Lower views validation
            if(lower_views["score"]>item["view_count"]):
                lower_views["index"]=i
                lower_views["score"]=item["view_count"]
                lower_views["data"] = item

            #Lower creation date validation
            if(lower_creation_date["date"]>item["creation_date"]):
                lower_creation_date["index"]=i
                lower_creation_date["date"] = item["creation_date"]
                lower_creation_date["data"]=item



            #Most creation date validation
            if (most_creation_date["date"] < item["creation_date"]):
                most_creation_date["index"] = i
                most_creation_date["date"] = item["creation_date"]
                most_creation_date["data"] = item


            #Most reputation Validation
            owner=item["owner"]
            if(most_owner_reputation["reputation"]<owner["reputation"]):
                most_owner_reputation["index"] = i
                most_owner_reputation["reputation"] = owner["reputation"]
                most_owner_reputation["data"] = item


        else:
            print("El item que sigue no tiene las llaves suficientes")
            print(item)


    #2
    print("Respuestas contestadas: "+str(answered))
    print("Respuestas no contestadas: " + str(nonanswered))

    #3
    print("Respuesta con menor numero de vistas: ")
    print(lower_views)

    # 4
    print("Respuesta mas vieja: ")
    print(lower_creation_date)
    print("Respuesta mas actual: ")
    print(most_creation_date)

    # 5
    print("Respuesta con mayor reputation: ")
    print(most_owner_reputation)

main()

