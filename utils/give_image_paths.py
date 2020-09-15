from utils.detect_glasses import get_details
import os
import glob



def suggest_folder(data_dict):
    age_folder={'baby':'baby',
                'young':'young',
                'middle':'middle',
                'old':'old'}

    gen_folder={'Male':'male',
                'Female':'female'}

    emo = data_dict['Emotion']
    age = data_dict['Age']
    eye = data_dict['Eyeglasses']
    gen = data_dict['Gender']
    mus = data_dict['Mustache']
    sun = data_dict['Sunglasses']
    bea = data_dict['Beard']

    if age<5:
        age_gp='baby'
    elif age<18:
        age_gp='young'
    elif age<40:
        age_gp='middle'
    else:
        age_gp='old'

    if gen=='Male':
        gen_gp='Male'
    else:
        gen_gp='Female'

    age_f_name=age_folder[age_gp]
    gen_f_name=gen_folder[gen_gp]

    prefix='static/assets'
    recomm_files=[]

    folder_path=os.path.join(prefix,age_f_name,gen_f_name)
    print(folder_path)

    for filename in glob.iglob(folder_path+'/*.jpg',recursive = True): 
        recomm_files.append(filename)
        # print(filename)

    print(recomm_files)
    return(recomm_files)

def all_files():
    print("\nUsing glob.iglob()")
    file=[] 
    for filename in glob.iglob(prefix+'/**/*.jpg',recursive = True): 
        file.append(filename)
        print(filename)

if __name__ == '__main__':
    name = 'im.jpg'
    data_dict = get_details(name)
    print(data_dict)
    suggest_folder(data_dict)
    # It returns an iterator which will  
    # be printed simultaneously. 
