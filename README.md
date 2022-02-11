# aad-aws-iam-login

A script, that updates your AWS profiles with valid STS credentials via your AAD identity.

Contrary to other helpers, like the awesome [awsume](https://awsu.me), we will not use one AWS profile to assume a profile with Another profile through "assume-role", but rather through a WebIdentity as a trust anchor. In normal enterprise architectures, that would be something like [Azure AD](https://aad.portal.azure.com/).

First, lets look at the exact configuration of Azure AD and the AWS IAM Identity provider: