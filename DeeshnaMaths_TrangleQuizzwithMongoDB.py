import random
j=1
while j <= 10:
    FinalResult = ""
    XY =random.randint(1, 10)
    XZ =random.randint(1, 10)
    YZ =random.randint(1, 10)
    XYZAngle =random.randint(1, 120)
    XZYAngle =random.randint(1, round((180-XYZAngle)/2))
    YZXAngle = 180-XYZAngle-XZYAngle
    print("Side XY =" + str(XY))
    print("Side XZ =" + str(XZ))
    print("Side YZ =" + str(YZ))
    print("Side XYZAngle =" + str(XYZAngle))
    print("Side XZYAngle =" + str(XZYAngle))
    print("Side YZXAngle =" + str(YZXAngle))
    i=0
    DeeshnaAnswerAngle = input("What type of triangle is this - Acute Angle Triangle - '1', Obtuse Angle Triangle '2', Right Angle Triangle '3'?")
    DeeshnaAnswerSides = input("What type of triangle Side is this - Equilateral Triangle - '1', Isosceles Triangle '2', Scalene Triangle '3'?")
    iSide = 0
    if XY==XZ==YZ:
        iSide = 1 #Equilateral Triangle
    else:
        if XY==XZ or XY==YZ or XZ == YZ:
            iSide = 2 #Isosceles Triangle
        else:
            iSide =3 #Scalene Triangle
    iAngle = 0
    if XYZAngle < 90 and XZYAngle < 90 and YZXAngle < 90:
        iAngle = 1 #Acute Angle
    else:
        if XYZAngle>90 or XZYAngle>90 or YZXAngle>90:
            iAngle = 2 # obtuse angle triangle
        else:
            if XYZAngle == 90 or XZYAngle == 90 or YZXAngle == 90:
                iAngle = 3 #Right Angle

    if int(DeeshnaAnswerAngle) == iAngle:
        print("Congratulations, you are right for Triangle Angle Question")
    else:
        print("Sorry, you are wrong for Triangle Angle Question")
    if int(DeeshnaAnswerSides) == iSide:
        print("Congratulations, you are right for Triangle Side Question")
    else:
        print("Sorry, you are wrong for Triangle Side Question")
    i += 1
    print("Your Total Point is ***" + str(i) + "***" )
    #FinalResultTriangleFullName = {
    #   "13" : "Equilateral Rightangle Triangle",
    #  "11" : "Equilateral AcuteAngle Triangle",
    # "12" : "Equilateral ObtuseAngle Triangle",
    #   "21": "Isosceles AcuteAngleAngle Triangle",
    #   "22": "Isosceles ObtuseAngle Triangle",
    #   "23": "Isosceles RightAngle Triangle",
    #   "31": "Scalene AcuteAngle Triangle",
    #   "32": "Scalene ObtuseAngle Triangle",
    #   "33": "Scalene Rightangle Triangle",
    # }
    FinalResult = str(iSide) + str(iAngle)
   # print(FinalResultTriangleFullName[FinalResult])
    #Adding String for Database Connection
    from pymongo.mongo_client import MongoClient
    from pymongo.server_api import ServerApi
    uri = "mongodb+srv://deevasbohra_db_user:Microsoft~123456@cluster0.2qsnd79.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['DeeshnaTriangleDB']
    collection = db['Triangles']
    Triangles = collection.find_one({"ResultKey" : FinalResult})
    print(Triangles["OutcomeResult"])
    confirmation = input("Do you want to continue? (Y/N) ")
    if confirmation == "Y" or confirmation == "y":
        continue
    else:
        exit()
j += 1
