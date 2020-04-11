# Identifying Malaria Parasites from Malaria

Top: A random selection of positive patches. Bottom: A random selection of negative patches. 
![](https://github.com/MicaTeo/MalariaDetection2018/blob/master/wanted/some_samples_0_1.png)

---

Sample detection output on the test image. Blue squares indicate patches which were correctly classified as containing parasites. Red squares indicate false positive and whie squares indicates false negatives.
Test image 1               |  Test image 2
:-------------------------:|:-------------------------:
![](https://github.com/MicaTeo/MalariaDetection2018/blob/master/wanted/plasmodium-0054.jpg)  |  ![](https://github.com/MicaTeo/MalariaDetection2018/blob/master/wanted/plasmodium-0255.jpg)

**Data:**

2703 blood smear images with bounding boxes of 50,255 malaria parasites.

http://air.ug/downloads/plasmodium-images.zip


**To run this code:**

./build.sh

python evaluatedetection.py

**Reference:**

J.A. Quinn, A. Andama, I. Munabi, F.N. Kiwanuka. Automated Blood Smear Analysis
for Mobile Malaria Diagnosis. Chapter in Mobile Point-of-Care 
Monitors and Diagnostic Device Design, eds. W. Karlen and K. Iniewski, 
CRC Press. 2014

http://cit.mak.ac.ug/staff/jquinn/papers/AutomatedMalariaDiagnosisChapter.pdf



