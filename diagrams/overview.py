# This is the overview diagrams file in python
from diagrams import Cluster, Diagram, Edge
# AWS Imports
from diagrams.aws.security import IAM, IdentityAndAccessManagementIamTemporarySecurityCredential as TSC
# Azure Imports
from diagrams.azure.identity import ActiveDirectory
# Generic Imports
from diagrams.onprem.auth import Oauth2Proxy
from diagrams.onprem.client import Client

with Diagram(name="Azure AAD login for AWS IAM", show=False, direction="LR"):
    with Cluster("Azure"):
        AAD = ActiveDirectory("Azure AAD")

    with Cluster("AWS"):
        IAM = IAM("IAM")
        STS_Token = TSC("STS Token")

    with Cluster("OnPrem"):
        OAuth = Oauth2Proxy("OAUTH Proxy")
        Client = Client("User Machine")

    Client >> AAD
    AAD >> OAuth
    IAM << OAuth
    STS_Token << IAM
    Client << STS_Token
