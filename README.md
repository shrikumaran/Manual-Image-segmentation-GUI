# Manual-Image-segmentation-GUI

### Project period: April 2020- May 2020
### Project under: Origin health, singapore: http://www.originhealth.ai/

### Project motivation: 
- This a minor part in a bigger project with a goal to achive automatic segmentation of fetal ultrasound images.
- This is automated by the use of Deep Learning segmentation methods.
- For this purpose we need to generate dataset to train the segmentation model.
- The dataset consists of the training pairs: input ultrasoud images, segmented labels.
- Input ultrasound images will be provided by the medical centres.
- But the segmented labels are something which we have to generate.
- For this purpose we proposed the idea of using a segmentation tool to manualy segment images.
- Amira avizo-> is a tool available in the market for the same purpose.Avizo is a general-purpose commercial software application for scientific and industrial data visualization and analysis. 
- But this tool provides a lot of extra features and also is not available as opensource but is a paid software.
- Thus to cut down the cost the idea of making a GUI was proposed.

### Project description:
- Used Pytkinter and PyQt to develop 2 versions of the same tool.
- Features:
  - loads images to be segmented.
  - Multiclass manual segmentation can be achived.
  - each class is indicated using different color.
  - Colors have good transperancy, allowing users to view whats under the segmented region.
  - 2 types of brushes to segment: solid brush tool and Lazo brush tool
  - 2 different shapes of brushes: circular and square
  - Histogram of the image can be adjusted
  - Image can be window zoomed and zoomed as a whole too.
  - length between 2 points can be measured for data collection purposes.
  - Comments can be registered regardning the image in the dataset. Helps when it comes to removal of poor images.
  - Smoothening of segmented regions.
  - Removing faulty islands of segments with customized sizes.
  - Undo redo allowed 
  - Checkpoint of the previously segmented image scan be saved so that segmentation of a series of image data can be dine with breaks.
  
- Also the folders has the code to encrypt the data, so that if images have to be sent to the user in a encrypted way, it can be encryted as a numpy file such the the user opens the tool and Image loads by itself and the images need not be present seperately.

-Exe format of the tool available in the folder

This tool is not restricted to ultrasound images alone. This can be used to generate segmented labels for any semantic segmentation project. 
