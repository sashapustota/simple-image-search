<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h1 align="center">Cultural Data Science 2023</h1> 
  <h2 align="center">Assignment 1</h2> 
  <h3 align="center">Visual Analytics</h3> 


  <p align="center">
    Aleksandrs Baskakovs
  </p>
</p>


<!-- Assignment instructions -->
## Assignment instructions

For this assignment, you'll be using ```OpenCV``` to design a simple image search algorithm.

The dataset is a collection of over 1000 images of flowers, sampled from 17 different species. The dataset comes from the Visual Geometry Group at the University of Oxford, and full details of the data can be found [here](https://www.robots.ox.ac.uk/~vgg/data/flowers/17/).

For this exercise, you should write some code which does the following:

- Define a particular image that you want to work with
- For that image
  - Extract the colour histogram using ```OpenCV```
- Extract colour histograms for all of the **other* images in the data
- Compare the histogram of our chosen image to all of the other histograms 
  - For this, use the ```cv2.compareHist()``` function with the ```cv2.HISTCMP_CHISQR``` metric
- Find the five images which are most simlar to the target image
  - Save a CSV file to the folder called ```out```, showing the five most similar images and the distance metric:

|Filename|Distance|
|---|---|
|target|0.0|
|filename1|---|
|filename2|---|

<!-- ABOUT THE PROJECT -->
## About the project
This repository contains a script that compares images via their colour histograms. The script is designed to work with the [Oxford Flowers 17](https://www.robots.ox.ac.uk/~vgg/data/flowers/17/) dataset. The script extracts the colour histogram for a target image and compares it to the histograms of all other images in the dataset. The script then saves a CSV file to the folder called ```out```, showing the five most similar images and the distance metric.

<!-- Data -->
## Data
The [Oxford Flowers 17](https://www.robots.ox.ac.uk/~vgg/data/flowers/17/) dataset consists of 1360 images of flowers, sampled from 17 different species. The dataset comes from the Visual Geometry Group at the University of Oxford. Make sure to download and unzip the dataset in the ```data``` folder before using the script.

<!-- USAGE -->
## Usage
To use the code you need to adopt the following steps.

**NOTE:** There may be slight variations depending on the terminal and operating system you use. The following example is designed to work using the Visual Studio Code version 1.76.0 (Universal). The terminal code should therefore work using a unix-based bash. The avoid potential package conflicts, the ```setup.sh``` bash files contains the steps necesarry to create a virtual environment for the project. The code has been thoroughly tested and verified to work on a Mac machine running macOS Ventura 13.1. However, it should also be compatible with other Unix-based systems such as Linux. If you encounter any issues or have questions regarding compatibility on other platforms, please let me know.

1. Clone repository
2. Run ``setup.sh``
3. Run the script ```main.py```

### Clone repository

Clone repository using the following lines in the unix-based bash:

```bash
git clone https://github.com/sashapustota/simple-image-search
cd simple-image-search
```

### Run ```setup.sh```

The ``setup.sh`` script is used to automate the installation of project dependencies and configuration of the environment. By running this script, you ensure consistent setup across different environments and simplify the process of getting the project up and running.

The script performs the following steps:

1. Creates a virtual environment for the project
2. Activates the virtual environment
3. Installs the required packages
4. Deactivates the virtual environment

### Run ```main.py```

Before running the script, activate the virtual environment by running the following line in the terminal:

```bash
source ./simple-image-search-venv/bin/activate
```

After activating the virtual environment, run the script ```main.py``` by running the following line in the terminal:

```bash
python3 src/main.py --image <your image>
```

Make sure to replace ```<your image>``` with the name of the image you want to compare. Make sure to include the file extension. For example, if you want to compare the image ```image_0420.jpg```, run the following line in the terminal:

```bash
python3 src/main.py --image image_0420.jpg
```

The ```main.py``` script perform the following steps:

1. Extracts the colour histogram for the target image
2. Extracts the colour histograms for all other images in the dataset
3. Compares the histogram of the target image to all other histograms
4. Prints the five most similar images and the distance metric
5. Saves a CSV file to the folder called ```out```, showing the five most similar images and the distance metric

Finally, deactivate the environment.

```bash
deactivate
```

<!-- RESULTS -->
## Results
Top five similar images and their respective distances are saved in the ```out``` folder in a form of a ```csv``` file. The results are also printed in the terminal.

<!-- REPOSITORY STRUCTURE -->
## Repository structure
This repository has the following structure:
```
│   README.md
│   requirements.txt
│   setup.sh
│
├──data
│
├──out
│
└──src
      main.py

```
<!-- REPRODUCIBILITY -->
## Reproducibility
When using the script to find the five most similar images to ```image_0420.jpg```, the following results are obtained:

```
Most similar images:
            Filename    Distance
1123  image_0399.jpg  3380272.43
553   image_0282.jpg  3346722.74
826   image_1191.jpg  2694367.46
642   image_0054.jpg  2092524.11
532   image_0679.jpg  2050130.46
```