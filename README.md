# neutralbot v.alpha
This bot will take a face image as input, classify it as one of eight emotions; neutral, anger, contempt, disgust, fear, happy, sad and surpise. 
The bot will then attempt to stop the displayed emotions with either pictures, videos, or textual informations. 
### Problems
There were issues training the network to have a decent validation and test accuracy. The best I got with this network is about 75%. For the real-world images, the bot is actually quite terrible at classifying the emotions. Much work will have to be done for sure.
### Data Set
Cohn-Kanade Extended (CK+) Facial Expression dataset. Dataset contains posed and unposed stills of people's faces going through an emotion. 
### Software
Tensorflow, Keras, PIL, cv2 
### Relevant Research Articles
ImageNet Classification with Deep Convolutional Neural Networks by Alex Krizhevsky
### Collaboration
This will be a one-person project. 
### Project Milestones
November 6 - Object scanner is able to identify an object picture against a white or constrasting background. 
![cat](https://user-images.githubusercontent.com/43867207/46512182-2cbaa580-c818-11e8-914e-72db95a77e75.png)
![1](https://user-images.githubusercontent.com/43867207/46512292-b23e5580-c818-11e8-926f-c8a7660f4f84.jpg)
December 4 - Object scanner is able to identify an object and give basic or interesting information to the user. 
![catfact](https://user-images.githubusercontent.com/43867207/46512185-2debd280-c818-11e8-8d4d-947bf4570168.png)

## References
- Kanade, T., Cohn, J. F., & Tian, Y. (2000). Comprehensive database for facial expression analysis. Proceedings of the Fourth IEEE International Conference on Automatic Face and Gesture Recognition (FG'00), Grenoble, France, 46-53.
- Lucey, P., Cohn, J. F., Kanade, T., Saragih, J., Ambadar, Z., & Matthews, I. (2010). The Extended Cohn-Kanade Dataset (CK+): A complete expression dataset for action unit and emotion-specified expression. Proceedings of the Third International Workshop on CVPR for Human Communicative Behavior Analysis (CVPR4HB 2010), San Francisco, USA, 94-101.
