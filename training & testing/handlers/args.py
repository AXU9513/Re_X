import argparse
import sys
import os

def get_args():
    ar = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    ar.add_argument('-n', '--name', type = str, default =  "model", help = "Please training name - for save folder")
    ar.add_argument('-m', '--model', type = str, default =  "mynet",help = "Please enter model type - unet,mynet,resnet50")
    ar.add_argument('-i', '--input_folder', type = str, default="../data", help = "Please enter image location")
    ar.add_argument('-o', '--output_folder', type = str, default="../results/", help = "Please enter model save location")
    ar.add_argument('-p', '--patch_size', type = int, default=200, help = "Please enter model patch size")
    ar.add_argument('-g','--gpu', type = int, default=0, help = "Please enter GPU to use")
    ar.add_argument('-b','--batch_size', type = int, default=32, help = "Please enter model batch size")
    ar.add_argument('--no_depth', action='store_true', help = "Whether to use depth or not")
    ar.add_argument('--augment', action='store_true', help = "Whether to augment data")
    ar.add_argument('--iter_load', action='store_true',help="Option to define whether to load images iteratively to minimize memory")
    ar.add_argument('-l','--labels', action='append', help="Option to select specific training labels \nOTHER = 0\nTREE = 1\nBUILDING = 2\nCAR = 3\nVEG = 4\nGROUND = 5")
    ar.add_argument('--cont', action='store_true', help='Option defining whether to continue existing model')
    ar.add_argument('-c', '--city_name', type = str, default="chicago", help = "Please enter city name to test")

    args = ar.parse_args()
    label = args.labels
    if label:
        label = list(map(int, label)).sort()
        if not label[0] == 0:
            label = [0]+label
        print("Using labels: "+','.join(map(str,label)))    
    args.label = label

    #----Train Result Paths---
    args.output_folder += args.name
    if os.path.exists(args.output_folder):
        if not args.cont:
            print("Training path already exists")
            #sys.exit(0)
            pass
    else:
        if args.cont:
            print("Model does not exist")
            print(args.output_folder)
            sys.exit(0)
        os.makedirs(args.output_folder)

    return args