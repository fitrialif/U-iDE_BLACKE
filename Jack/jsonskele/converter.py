import json as j
from toSkeletonList import toSkeletonList

# replace this with the desired file
jsonFolder = 'out/'
jsonFile = jsonFolder+'tpose_01_leg_keypoints_norm.json'

with open(jsonFile) as f:
    keypoints = j.loads(f.read())
print j.dumps(keypoints["part_candidates"], indent=4, separators=(',',':'))

# recreate the skeleton but in terms of angle of bones, rather than posistion
parts = keypoints["part_candidates"][0]  
# print len(parts)
for bone,value in parts.iteritems():
    # print value[]
    if len(value) ==0:
        # indicate that these values are missing
        # -5.0 is not a possible value as all the values are normalized between [-1,1]
        value.append(-5.0)
        value.append(-5.0)
        value.append(0)

skeletonList = toSkeletonList(parts)
