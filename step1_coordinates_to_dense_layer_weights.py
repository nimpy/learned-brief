"""
Generating weights for the dense layer of the neural network that should perform binary pixel tests as described in BRIEF paper. 

The weights are generated based on the list of pixel coordinates counted from the patch centre (so in range [-23..24]). 

The lists of pixel coordinates are taken from OpenCV Github repo files:
https://github.com/opencv/opencv_contrib/blob/4.3.0/modules/xfeatures2d/src/generated_16.i
https://github.com/opencv/opencv_contrib/blob/4.3.0/modules/xfeatures2d/src/generated_32.i
https://github.com/opencv/opencv_contrib/blob/4.3.0/modules/xfeatures2d/src/generated_64.i

The coordinates are extracted from those files and are under:
./opencv_test_points/generated_X.txt
where X can be 16, 32, or 64. These represent different versions of BRIEF taking X bytes.
The number of keypoints in the files is X * 8 * 2 (8 because it's bytes, and 2 because it's pairs of keypoints).

"""

import numpy as np


def generate_and_save_dense_layer_weights():

	brief_patch_size = 48  # PATCH_SIZE variable hard-coded into OpenCV BRIEF (see OpenCV repo)
	centre_coord_offset = 23  # hard-coded into OpenCV BRIEF, around the half of the PATCH_SIZE as defined there

	brief_version = 64  # either 16, 32, or 64

	# properties of the fully-connected layer
	input_dimension = brief_patch_size * brief_patch_size
	output_dimension = brief_version * 8

	file = open('./opencv_test_points/generated_' + str(brief_version) + '.txt', 'r') 

	x_coord = 0
	y_coord = 0

	output_count = 0
	total_count = 0

	weights = np.zeros((input_dimension, output_dimension), dtype = np.float32)

	while True:
		line = file.readline()
		if not line: 
			break
		
		x_coord_prev = x_coord
		y_coord_prev = y_coord
		
		x_coord = int(line[1: line.find(",")])
		y_coord = int(line[line.find(",") + 1: -2])

		if total_count % 2 == 1:

			index1 = np.ravel_multi_index((x_coord_prev + centre_coord_offset, y_coord_prev + centre_coord_offset), (brief_patch_size, brief_patch_size))
			index2 = np.ravel_multi_index((x_coord + centre_coord_offset, y_coord + centre_coord_offset), (brief_patch_size, brief_patch_size))

			weights[index1, output_count] = -1
			weights[index2, output_count] = 1

			output_count += 1

		total_count += 1
		
	assert output_count == output_dimension, "The descriptor size should be " + str(output_dimension)

	np.save('./weights/weights_dense_' + str(brief_version) + '.npy', weights)

	file.close()
	
	return weights


if __name__ == '__main__':
	
	generate_and_save_dense_layer_weights()

