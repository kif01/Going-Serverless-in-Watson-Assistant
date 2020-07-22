#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys, json
import pandas as pd
import types
from botocore.client import Config
import ibm_boto3

def main(dict):
    print (dict['action'])
    
    res = ""
    
    # if user is asking about bank account
    if (dict['action']=="account"):
        res= getAccount(dict)
        return res
    
    # if user is asking about the services/plans  
    else:
        entity = 'unknown'
        if 'entity' in dict:
            entity = dict['entity']
        else:
            entity = 'unknown'
        res = getEntityDescriptionFromCSV(entity, dict)
    return { 'response': res }
    
  
# Check if account is personal or buisness
def getAccount(dict):
    response={"result":""}
    if dict['accountID'] == 11111111 and dict['OTP'] == 123:
        response["result"]="Welcome Mike Hudson\nAccount No:11111111"
        
        
      
    elif dict['accountID'] == 22222222 and dict['OTP'] == 456 :
        response["result"] = "Welcome Veronica Gomez\nAccount No:22222222"
   
         
    else:
        response["result"] = "Incorrect credentials"
     
    return  response


#Read Data from excel file  
def getEntityDescriptionFromCSV(entity, dict):
    # @hidden_cell
    # The following code accesses a file in your IBM Cloud Object Storage. It includes your credentials.
    # You might want to remove those credentials before you share the notebook.
    client = ibm_boto3.client(service_name='s3',
    ibm_api_key_id= dict['api_key'],
    ibm_service_instance_id= dict['service_instance_id'],
    config=Config(signature_version='oauth'),
    endpoint_url= dict['endpoint_url'])
    
    body = client.get_object(Bucket= dict['bucket_name'],Key=dict ['file_name'])['Body']
    if not hasattr(body, "__iter__"): body.__iter__ = types.MethodType( __iter__, body )
    
    df_data_1 = pd.read_csv(body, encoding = "ISO-8859-1")
    
    entity = entity.lower()
    
    row = df_data_1.query('entity == @entity')[['description']]
    reponse = ''
    idx = row.index
    try:
        idx = idx[0]
        response = df_data_1.iloc[idx, 1] + ''
    except IndexError:
        response = 'Sorry cannot find a definition in my knowledge base'
    
    return response

