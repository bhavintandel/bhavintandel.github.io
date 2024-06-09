Title: Exploring ML Tools - Amazon Textract
Date: 2024-05-08 22:31
Modified: 2024-05-08 22:31
Category: blogs
Tags: ml
slug: ml-aws-textract

Documents have been part of our lives since very long time, however, its not always so easy to find something in document. With the new advances in machine learning we can actually digitize our document and thus put it to good use.

## Introduction

In this post, we will be exploring Amazon Textract which has the capabilities to extract text and data from documents. It uses Optical Character Recognition(OCR) and augmented AI to detects the document layout and key element from the it. 
Amazon textract has been trained on tens of millions of documents including invoices, contracts, receipts, insurance claims, policy documents, etc.

## Features

* Key-value pair extraction
* Table extraction
* Bounding Box for all the extracted result
* Confidence score for every extracted result
* It can handle multi page document

## Usecase

Following is one of the example of how Textract can be used to process large scale documents using complementary aws services.

* Large scale document processing with Amazon Textract

## Usage

The service can be used directly from aws console or using api in your preferred language like java, python, javascript, etc. We will be using aws python sdk - boto3 to interact with the service.

### Input

It accepts images of format (JPEG/PNG) and PDFs .
For Images, we can perform synchronous or asynchronous call with reading it as bytes or passing s3 location.
To process PDF, only asynchronous call is supported via s3 location.
Initialize the Textract client in python, if you are planning to run extract job on files under s3 bucket then, region_name should be same as the location on data.

![Reciept]({attach}../../../resources/data_science/exploring-ml-tools/aws-textract/assets/IMG_2093.JPG)

#### Detexting text in Image

```python
import boto3
textract_client = boto3.client('textract', region_name='eu-west-1')
# Reading image file
with open('assets/IMG_2093.JPG', 'rb') as f:
    image = f.read()
# Detecting text in Image
img_response_1 = textract_client.detect_document_text(
    Document={
        'Bytes': image
    })
```
The reponse contains lot of information regarding the the analysis. First of all we get DocumentMetadata which has information like page number of the analysis. And we get many Blocks which can be one of the following value 'KEY_VALUE_SET'|'PAGE'|'LINE'|'WORD'|'TABLE'|'CELL'|'SELECTION_ELEMENT'. 

To extract text from the output:

```python
for block in img_response_1['Blocks']:
    if (block['BlockType'] == 'LINE'):
        print(block['Text'])
```

```text
Gate Gourmet Switzerland GmbH
(d/b/a Gate Retail Onboard)
Flight Flight Date 2072 24/05/2017 Sector MUC-LTN 19:25:00
Bar Set 7454
Transaction Type SALE
Transaction Date e:24/05/2017
Transaction Time 10:25 AM
Transaction 5b42b840b1c
Item
Price Oty
Water Still
1.80
3
Coffee Reg
2.50
I
SubTotal
4.30
Net Subtotal (GBP)
4.30
Cash (EUR)
5.50
Terinal 00-02-78-b0-e6-ef 00-00
CUSTOMER COPY
Please retain for Vour records
```

With the above information we also get the actual location of that on a page with Bounding box information. Which can we used to create the indexed search engine of our documents and thus make it searchable on word level.

Following are some example on running Textract on S3 object

```python
# Analyzing text in Image
img_response_2 = textract_client.analyze_document(
    Document={
        'Bytes': image
    },
    FeatureTypes=[
        'TABLES',
    ])
# Asynchronous call to extract text from pdf
asset_bucket = "<bucket_name>"
pdf_prefix = "amazon-textract/assets/pdf/receipt_uber.pdf"
pdf_response_1 = textract_client.start_document_text_detection(
        DocumentLocation={
            'S3Object': {
                'Bucket': asset_bucket,
                'Name': pdf_prefix
            }
        })
job_id_1 = pdf_response_1['JobId']
## check the progress
response = textract_client.get_document_text_detection(
    JobId=job_id
)
if response['JobStatus'] == 'IN_PROGRESS':
    print("Job is still in progress")
else:
    print("Extraction job completed")
    print(response)
```

## Findings

Some key findings are:
* It returns information of bouding box from where the text has been extracted.
* It is not angle invariant, that is, document or image to be analyze must be aligned vertically.

## Pricing

* No upfront cost
* Free tier: 
    * Detecting Text - 1000 pages/month for first 3 months
    * Analyzing Document - 100 pages/month for first 3 months
* Detecting Text: 
    * First 1 Million pages - $0.0015/page - $1.5/1000 pages
    * Over 1 Million pages - $0.0006/page - $0.6/1000 pages

The other details for analyze document api can be found at: https://aws.amazon.com/textract/pricing/

## Bibliography

amazon-textract-serverless-large-scale-document-processing
https://aws.amazon.com/
https://aws.amazon.com/textract/pricing/
