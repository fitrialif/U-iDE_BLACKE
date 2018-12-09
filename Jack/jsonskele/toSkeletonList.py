import math
def toSkeletonList(parts):
   
    skeleton = []

    #bones where the previous endpoint is not squential
    boneExceptions= {'15':'0','16':'0',
                     '17':'15',
                     '18':'16',
                     '5':'1','8':'1',
                     '12':'8',
                     '24':'11','22':'11',
                     '21':'14','19':'14'}
    
    #initial value of previous bone
    previousBone = 0
    for keyVal in xrange(1,len(parts)):
        #need to convert to string to match with dict keys
        strKey = str(keyVal)
        if strKey not in boneExceptions:
            previousBone = str(keyVal-1)
            pass

        else:
            #need to know which value it matches with and the set the previous bone accordingly
            # print ("key " + strKey + " was found in boneExceptions")        
            previousBone = boneExceptions[strKey]
            # print ("previousBone set to " + previousBone)
            pass

        #before calculating the angle, ensure that the bone has a valid position
        if parts[strKey][1] == -5.0 or parts[previousBone][1] == -5.0:
            print "bone not found, setting confidence to 0"
            angle = 0
            pass
        else:
            #calculate the angle
            angle =  math.atan((parts[strKey][1] - parts[previousBone][1])
                              /(parts[strKey][0] - parts[previousBone][0]))
            # print ("angle of bone [" +strKey+ "] wrt bone[" +previousBone +"] is " + str(angle) )
            
       
        skeleton.append([angle, parts[strKey][2] ])
        pass

 
    print ("skeleton v2")

    for bone in skeleton:
        print bone

    return skeleton
    

def jankSkely(parts):
    # I am so sorry for the existence of this function
    # it is a sin against the programming gods
    print ""
    print ("skeleton v1")
    #first get the angle of the neck w.r.t the body 
    skeleton = []
    angle =  math.atan((parts['1'][1] - parts['0'][1])/(parts['1'][0] - parts['0'][0]))
    print ("angle neck wrt body               = " +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))

    angle =  math.atan((parts['15'][1] - parts['0'][1])/(parts['15'][0] - parts['0'][0]))
    print ("right eye wrt neck                = " +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))

    angle =  math.atan((parts['17'][1] - parts['15'][1])/(parts['17'][0] - parts['15'][0]))
    print ("right ear wrt right eye           = " +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))

    angle =  math.atan((parts['16'][1] - parts['0'][1])/(parts['16'][0] - parts['0'][0]))
    print ("left eye wrt neck                 = " +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))

    angle =  math.atan((parts['18'][1] - parts['16'][1])/(parts['18'][0] - parts['16'][0]))
    print ("left ear wrt left eye             = " +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))

    # right shoulder w.r.t body
    angle = math.atan((parts['2'][1] - parts['1'][1])/parts['2'][0] - parts['1'][0])
    print ("angle R shoulder wrt body         = " +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))

    # right elbow wrt right shoulder

    angle = math.atan((parts['3'][1] - parts['2'][1])/parts['3'][0] - parts['2'][0])
    print ("angle r elbow wrt r shoulder      = " +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))

    # right wrist wrt right elbow
    angle = math.atan((parts['4'][1] - parts['3'][1])/parts['4'][0] - parts['3'][0])
    print ("right wrist wrt right elbow       = " +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))

    # left shoulder wrt body
    angle = math.atan((parts['5'][1] - parts['1'][1])/parts['5'][0] - parts['1'][0])
    print ("left shoulder wrt body            =" +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))

    angle = math.atan((parts['6'][1] - parts['5'][1])/parts['6'][0] - parts['5'][0])
    print ("left elbow wrt left  shoulder     = " +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))

    angle = math.atan((parts['7'][1] - parts['6'][1])/parts['7'][0] - parts['6'][0])
    print ("left wrist wrt left  elbow        = " +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))

    angle = math.atan((parts['8'][1] - parts['1'][1])/parts['8'][0] - parts['1'][0])
    print ("pelvis wrt body                   = " +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))

    angle = math.atan((parts['9'][1] - parts['8'][1])/parts['9'][0] - parts['8'][0])
    print ("right hip wrt pelvis              = " +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))

    angle = math.atan((parts['10'][1] - parts['9'][1])/parts['10'][0] - parts['9'][0])
    print ("right knee wrt right hip          = " +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))

    angle = math.atan((parts['11'][1] - parts['10'][1])/parts['11'][0] - parts['10'][0])
    print ("right ankle wrt right knee        = " +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))

    angle = math.atan((parts['24'][1] - parts['11'][1])/parts['24'][0] - parts['11'][0])
    print ("right heel wrt right  ankle       = " +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))

    angle = math.atan((parts['22'][1] - parts['11'][1])/parts['22'][0] - parts['11'][0])
    print ("right big toe wrt right ankle     = " +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))

    angle = math.atan((parts['23'][1] - parts['22'][1])/parts['23'][0] - parts['22'][0])
    print ("right small toe wrt right big toe = " +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))

    angle = math.atan((parts['12'][1] - parts['8'][1])/parts['12'][0] - parts['8'][0])
    print ("left hip wrt pelvis               = " +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))

    angle = math.atan((parts['13'][1] - parts['12'][1])/parts['13'][0] - parts['12'][0])
    print ("left knee wrt left hip            = " +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))

    angle = math.atan((parts['14'][1] - parts['13'][1])/parts['14'][0] - parts['13'][0])
    print ("left ankle wrt left knee          = " +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))

    angle = math.atan((parts['21'][1] - parts['14'][1])/parts['21'][0] - parts['14'][0])
    print ("left heel wrt left ankle          = " +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))

    angle = math.atan((parts['19'][1] - parts['14'][1])/parts['19'][0] - parts['14'][0])
    print ("left big toe wrt left ankle       = " +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))

    angle = math.atan((parts['20'][1] - parts['19'][1])/parts['20'][0] - parts['19'][0])
    print ("left small toe wrt left big toe   = " +str(angle))
    skeleton.append(angle)
    # print ("in degrees                        = " + str(angle*(180/math.pi)))
    

    for bone in skeleton:
        print bone

    return skeleton
    
