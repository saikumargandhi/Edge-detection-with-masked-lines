# Edge-detection-with-masked-lines
<ol>
  <li>Edges are very important to identify the shape, size and depth of the object.</li>
<li>To detect the edges correctly we need to preprocess the image to remove any blurness and noise, enhance the image by sharpening.</li>
<li>After the preprocessing we can apply the Morphological transformations (Opening,Closing,Erosion,Dilation) based on the image requirements.</li>
<li>Now we apply Canny Edge Detection to identify the edges and color with any bright color which doesn't overlap with the colors present in the image.</li>
<li>Now the identified edges are stacked over the original image.</li>
<li>We have the original image with it's edges drawn over it using only Opencv and Python.</li>
</ol>
