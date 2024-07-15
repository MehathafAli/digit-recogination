async function predict() {
  const fileInput = document.getElementById('imageUpload');
  const resultDiv = document.getElementById('result');

  if (fileInput.files.length === 0) {
      resultDiv.textContent = 'Please upload an image.';
      return;
  }

  const formData = new FormData();
  formData.append('file', fileInput.files[0]);

  resultDiv.textContent = 'Predicting...';

  try {
      const response = await fetch('/predict', {
          method: 'POST',
          body: formData
      });
      const data = await response.json();
      resultDiv.textContent = 'Predicted Digit: ' + data.prediction;
  } catch (error) {
      resultDiv.textContent = 'Error: ' + error.message;
  }
}
