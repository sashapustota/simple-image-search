import os
import cv2
import pandas as pd
import warnings
import argparse
warnings.simplefilter(action='ignore', category=FutureWarning)

# Define path to folder
path = os.path.join(os.getcwd(),"data", "flowers")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str, required=True, help="Name of the image file in the data folder")
    args = parser.parse_args()
    return args

# Make a function that gets the histogram of a target image
def get_target_hist(image):
    image_target = cv2.imread(os.path.join(path, image))
    hist_target = cv2.calcHist([image_target], [0,1,2], None, [256,256,256], [0,256, 0,256, 0,256])
    hist_target = cv2.normalize(hist_target, hist_target, 0, 1.0, cv2.NORM_MINMAX)
    return hist_target

# Now we make a function that will compare histograms of all images in a directory to our target histogram
def compare_histograms(hist_target):
    
    # Create an empty dataframe
    df = pd.DataFrame(columns=["Filename", "Distance"])

    # Making a list of image names
    list_of_images = os.listdir(path)

    # Making it a bit robust by only selecting .jpg files
    list_of_images = [x for x in list_of_images if x.endswith(".jpg")]

    for image in list_of_images:
        # Read in the image
        img = cv2.imread(os.path.join(path, image))
        # Calculate the histogram
        hist = cv2.calcHist([img], [0,1,2], None, [256,256,256], [0,256, 0,256, 0,256])
        # Normalise it
        hist = cv2.normalize(hist, hist, 0, 1.0, cv2.NORM_MINMAX)
        # Calculate the similarity
        similarity = round(cv2.compareHist(hist_target, hist, cv2.HISTCMP_CHISQR), 2)
        # And add it to a dataframe
        df = df.append({"Filename": image, "Distance": similarity}, ignore_index=True)
    
    # Sort the dataframe by similarity in descending order
    df = df.sort_values(by="Distance", ascending=False)

    print("Most similar images:")
    print(df.head(5))

    # Filter all but first 5 rows
    df = df.head(5)

    # And save it as CSV in "out" folder
    df.to_csv(os.path.join(os.getcwd(),"out", "similar_images.csv"), index=False)

def main():
    # Get the arguments
    args = parse_args()
    # Get the target histogram
    hist_target = get_target_hist(args.image)
    # Compare the histograms
    compare_histograms(hist_target)


if __name__== "__main__":
    main()