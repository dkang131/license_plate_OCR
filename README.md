# License Plate Recognition using OCR (Optical Character Recognition)

[Dataset](https://www.kaggle.com/datasets/nickyazdani/license-plate-text-recognition-dataset)

Author : [Darren Kang Wan Chee](https://www.linkedin.com/in/darren-kang-wan-chee/)

This project aims to recognize the character of a certain license plate using EasyOCR and Tesseract OCR

The initial step is to drop the first column of the CSV file containing labels since the first column stores the index.

The process can be done using the following syntax
```python
import pandas as pd

label_df = pd.read_csv(# YOUR CSV FILE PATH)
print(label_df.head())

label_df = label_df.drop(label_df.columns[0], axis=1)
print(label_df.head())

# You can then save it to replace the original CSV file for future usage (OPTIONAL)

label_df.to_csv(# WHERE YOU WANT TO SAVE THE NEW FILE, index=False)

# remember to set index as False

```

The Tesseract OCR is done with both Non-Sharpened Images and Sharpened Images

The EasyOCR is done with Binarization and Denoised Images

**_Note: The result of each OCR is not shown on the code because it causes a rendering problem_**

## Project Summary
### Tesseract with Non-Sharpened Images
Tesseract Accuracy: 0.008

Run Time: 49m 17.6s
### Tesseract with Sharpened Images
Tesseract Accuracy: 0.00165

Run Time: 48m 24.2s
### EasyOCR with Binarization and Denoised Images
OCR Accuracy: 0.05295

Run Time: 67m 21.3s

The result of this project is far from perfect because of the accuracy is very low.

Please feel free to discuss with me through [email](darrenkang03@gmail.com) if you know how to improve the quality of the OCR

