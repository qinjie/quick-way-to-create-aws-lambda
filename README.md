# Quick Way to Create an AWS Lambda Function



This is a quick guide on how to package an AWS lambda function with required libraries. 



1. Create a folder for all files in the lambda function, e.g.`my_lambda`, and cd into it.

   ```bash
   mkdir my_lambda
   cd my_lambda
   ```

2. Create files for the lambda function.

   ```bash
   touch lambda_function.py
   touch requirements.txt
   ```

3. In `lambda_function.py`, create a function `lambda_handler` and implement code.

   ```python
   import requests
   
   def lambda_handler(event, context):
       response =  requests.get('https://www.yahoo.com')
       return str(response)
       
   ```

4. In `requirements.txt`, specify libraries used by the lambda function.

   ```text
   requests
   ```

5. Lambda requires all libraries to be install in the same folder as the lambda function. Install the libraries the same folder using `pip`.

   ```bash
   pip install -r requirements.txt -t .
   ```
   
6. Create a zip file with all files in the current folder. Place the zip file, e.g.`lambda.zip`, outside the folder. 

   ```bash
   zip -r ../lambda.zip .
   ```

7. Examine the zip file created by listing files in the zip file. 

   ```bash
   unzip -l ../lambda.zip
   ```

8. In AWS Console, create a Python lambda function and upload the zip.
9. Test the lambda function.

