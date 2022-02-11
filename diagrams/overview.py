# coding=utf-8
from diagrams import Cluster, Diagram, Edge
# AWS Imports
from diagrams.aws.security import IAM, IdentityAndAccessManagementIamTemporarySecurityCredential as TSC
# Azure Imports
from diagrams.azure.identity import ActiveDirectory
# Generic Imports
from diagrams.onprem.client import Client

with Diagram(name="Azure AAD login for AWS IAM", show=False, direction="LR"):
    with Cluster("Azure"):
        AAD = ActiveDirectory("Azure AAD")

    with Cluster("AWS"):
        IAM = IAM("IAM")
        STS_Token = TSC("STS Token")

    with Cluster("OnPrem"):
        Client = Client("User Machine")

    Client >> AAD
    AAD >> Client
    IAM << Client
    STS_Token << IAM
    Client << STS_Token
