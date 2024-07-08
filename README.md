# Operationalizing Machine Learning
This project on Microsoft Azure demonstrates an end-to-end machine learning deployment using the Bank Marketing Dataset. Initially, the dataset was registered in Azure Machine Learning Studio. AutoML was then employed to train various models on this dataset. 

The best performing model from the AutoML run was deployed and can be consumed via REST endpoints. 

Furthermore, automation was achieved by creating and publishing a pipeline using the Python SDK within a Jupyter Notebook environment. This pipeline streamlined the entire workflow from data preparation through to model training and deployment.

## Architectural Diagram

## Key Steps

### Dataset
Following dataset was used and was uploaded n Azure ML studio so that it can be used by the next AutoML job. 
https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv
![image](https://github.com/saxenam06/Operationalizing-Machine-Learning/assets/83720464/51d3ac6f-309e-4ec8-b68c-843c20ebb326)

### Experiment completed
![image](https://github.com/saxenam06/Operationalizing-Machine-Learning/assets/83720464/560feb81-53d0-4259-b3c5-b95ef0d4b620)

### Best Model
![image](https://github.com/saxenam06/Operationalizing-Machine-Learning/assets/83720464/65d1de7c-7926-4119-b7da-3a6fca62f2ff)

### Deploy the model
Deploy the model using Azure Container instance so that other webservices can interact with the endpoint. Enable authentication so that keys are generated for authentication of other webservices

### Application Insights
Enable Application Insights using the python logs.py in GitBash and retrieve logs from the deployed service. 
![image](https://github.com/saxenam06/Operationalizing-Machine-Learning/assets/83720464/889c8cfe-338f-4e25-adfc-0c2a75156550)

### Logs
![image](https://github.com/saxenam06/Operationalizing-Machine-Learning/assets/83720464/c79efb88-1f94-4cb0-a183-0aebddddbf32)

### Swagger response
*TODO:* Write an overview to your project.
![image](https://github.com/saxenam06/Operationalizing-Machine-Learning/assets/83720464/9eec3072-3ace-4b9e-973c-70038ac44ba3)

![image](https://github.com/saxenam06/Operationalizing-Machine-Learning/assets/83720464/fd94c093-8ebd-404d-85ca-640b9986db1d)

![image](https://github.com/saxenam06/Operationalizing-Machine-Learning/assets/83720464/faf6f2e1-fa16-4a32-96fb-29880c144281)

![image](https://github.com/saxenam06/Operationalizing-Machine-Learning/assets/83720464/c4252d64-99f3-447a-8b39-e8b916ea308d)

![image](https://github.com/saxenam06/Operationalizing-Machine-Learning/assets/83720464/dfef8271-0811-41d1-8512-7e64c8194613)

### Pipeline Created
![image](https://github.com/saxenam06/Operationalizing-Machine-Learning/assets/83720464/61ec976c-7283-45a5-bf9f-15886860b7b3)

## Running Pipeline 
![image](https://github.com/saxenam06/Operationalizing-Machine-Learning/assets/83720464/f202cbfb-2fa5-45cd-8e21-3ac7bbbc8a99)

### Pipeline EndPoint
![image](https://github.com/saxenam06/Operationalizing-Machine-Learning/assets/83720464/a160002d-7c01-4ae7-9e80-ef39d75738fa)

### Pipeline Published with REST Endpoint
![image](https://github.com/saxenam06/Operationalizing-Machine-Learning/assets/83720464/a0a04689-ddbe-42e4-ae43-e564a0db2485)

### Pipeline completed 
![image](https://github.com/saxenam06/Operationalizing-Machine-Learning/assets/83720464/27bde130-5590-47c4-ad3c-ef38f7bd32bc)

## Architectural Diagram
![image](https://github.com/saxenam06/Operationalizing-Machine-Learning/assets/83720464/f484fcbc-8948-46e4-b1e9-0a597aac4c62)

### Screenshots of the `RunDetails` widget
![image](https://github.com/saxenam06/Operationalizing-Machine-Learning/assets/83720464/7d800a74-c40b-4506-ba47-971b77460b24)


### Screenshot of the best model trained with it's parameters.
![image](https://github.com/saxenam06/Operationalizing-Machine-Learning/assets/83720464/b699262d-88a1-45c3-9a64-67278e2a1ff3)

## Screen Recording
https://www.youtube.com/watch?v=d1QPgZBZwnQ

### Future work
Future enhancements for the project include
- Integrating a trigger as soon as there is a change in the dataset or new data arrives in blobstore. 
- Utilizing Apache Benchmark for performance optimization.
