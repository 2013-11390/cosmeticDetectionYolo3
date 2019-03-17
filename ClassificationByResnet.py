from omnis.application.image_processing.image_classification.resnet50 import ResNet50
import sys

def classify_img(data_path):
	cnn = ResNet50(model_path='Image_Classification.h5')

	prediction_result = cnn.predict(data_path = data_path)

	print('predict labels')
	print(prediction_result)


if __name__ == '__main__':
	if len(sys.argv) is 2 :
		classify_img(sys.argv[1])