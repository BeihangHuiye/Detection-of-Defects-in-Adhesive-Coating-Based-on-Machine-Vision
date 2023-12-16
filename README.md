《Detection of Defects in Adhesive Coating Based on Machine Vision》

The integrity of adhesive coating between propellant and insulation rubber significantly affects the stability of the functional interface and the service reliability of solid engines. The high aspect ratio and unstable lighting condition of the engine make it very difficult to inspect the coating integrity with the naked eye. More and more research is focused on using machine vision to detect defects. Limited by the size of the dataset, the current machine vision accuracy can not reach very high, and only limited to one application scenario. It is challenging to adapt to other scenarios of defect detection. In this paper, a machine vision detection method for lining spraying process adhesive coating defects is proposed, which realizes the accurate identification of defects in the coating integrity. The deflection compensation of the detection device and the adaptability design between the camera and the lens are fully considered, and a transfer learning model based on residual network is built with TensorFlow to achieve high-precision classification and recognition of defects. The model is trained by incrementally reducing the freezing layer of the model and the learning rate several times. Results show that the recognition accuracy can reach 100% on the training dataset and 96.15% on the validation. This vision method provides a fast and accurate method for engine liner coating defect detection, and it is about to be used in real industrial sites. 

---

The classification model is actually a very simple one for transfer learning. Great for newbies to get started. The framework used is Tensorflow 2.6.

It is also appreciated that the dataset cannot be made public as it may involve some sensitive issues.

---
