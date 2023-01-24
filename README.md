![alt text](https://ubit-teamcity-iag.intel.com/app/rest/builds/buildType:%28id:HostingSDI_CloudInfrastructureProvisioning_DBaaSclient%29/statusIcon "TC Build Status Icon")


## DBaaSclient
A Python client for DBaaS REST API


#### Usage
```bash
export DBAAS_K=--API-KEY--
python
```

```python
>>>
from DBaaSclient import DBaaSclient
>>>
>>> # instantiate DBaaSclient instance
client = DBaaSclient.get_DBaaSclient()
>>>
>>> # get iap cost data for all DBaaS applications
client.get_iap_cost()
>>>
```


### Development using Docker ###

For instructions on installing Docker:
https://github.intel.com/EnterpriseDocker/docker-auto-install-scripts

Clone the repository to a directory on your development server:
```bash
cd
git clone https://github.intel.com/HostingSDI/DBaaSclient.git
cd DBaaSclient
```

Build the Docker image
```bash
docker build -t dbasclient:latest  .
```

Run the Docker image
```bash
docker run \
--rm \
-v $HOME/DBaaSclient:/DBaaSclient \
-it dbasclient:latest \
/bin/bash
```
Note: Run the image with the source directory mounted as a volume within the container; this will allow changes to be made to the source code and have those changes reflected inside the container where they can be tested using pybuilder

Execute the build
```bash
pyb -X
```
