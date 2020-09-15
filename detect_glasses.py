#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import json
import config as config

__region=config.Region
__accessID=config.AccessID
__secretKey=config.AccessKey

client=boto3.client('rekognition',region_name=__region, aws_access_key_id=__accessID, aws_secret_access_key=__secretKey)

def get_attrib(attribute, faceDetail):
    cf = faceDetail[attribute]['Confidence']
    val = faceDetail[attribute]['Value']

    if cf>50:
        print(attribute,val)
        return cf,val
    else:
        return 0,None

def get_emotion(faceDetail):
    cf = faceDetail['Emotions'][0]['Confidence']
    val = faceDetail['Emotions'][0]['Type']
    if cf>50:
        print('Emotion',val,cf)
        return cf,val
    else:
        return 0,None

def get_age(faceDetail):
    low = faceDetail['AgeRange']['Low'] 
    high = faceDetail['AgeRange']['High']
    print('age',low,high)
    return low, high

def detect_faces(photo):
    
    with open(photo,'rb') as s_img:
        s_bytes = s_img.read()

    response = client.detect_faces(Image={'Bytes':s_bytes}, Attributes=['ALL'])

    print('Detected faces for ' + photo)    

    for faceDetail in response['FaceDetails']:
        
        get_emotion(faceDetail)
        get_age(faceDetail)
        get_attrib('Eyeglasses',faceDetail)
        get_attrib('Gender',faceDetail)
        get_attrib('Mustache',faceDetail)
        get_attrib('Sunglasses',faceDetail)
        get_attrib('Beard',faceDetail)

    return len(response['FaceDetails'])

def get_details(photo):
    with open(photo,'rb') as s_img:
        s_bytes = s_img.read()

    response = client.detect_faces(Image={'Bytes':s_bytes}, Attributes=['ALL'])

    print('Detected faces for ' + photo)    

    data_dict = {}
    for faceDetail in response['FaceDetails']:
        emotion = get_emotion(faceDetail)[1]
        data_dict['Emotion'] = emotion

        m,n= get_age(faceDetail)
        data_dict['Age']=(m+n)/2

        eyeglasses = get_attrib('Eyeglasses',faceDetail)[1]
        data_dict['Eyeglasses'] = eyeglasses

        gender = get_attrib('Gender',faceDetail)[1]
        data_dict['Gender'] = gender

        data_dict['Mustache'] = get_attrib('Mustache',faceDetail)[1]
        data_dict['Sunglasses'] = get_attrib('Sunglasses',faceDetail)[1]
        data_dict['Beard'] = get_attrib('Beard',faceDetail)[1]
    return data_dict

def main():
    photo='photo- 14 947 90108377-be9c29b29330.jfif'
    # face_count=detect_faces(photo)
    # print("Faces detected: " + str(face_count))
    details = get_details(photo)
    print(details)

if __name__ == "__main__":
    main()