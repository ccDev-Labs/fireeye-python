# fireeye.detection.PresignedUrlApi

All URIs are relative to *https://feapi.marketplace.apps.fireeye.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_presigned_url**](PresignedUrlApi.md#get_presigned_url) | **GET** /presigned-url/{report_id} | Get a presigned URL


# **get_presigned_url**
> object get_presigned_url(report_id, expiry=expiry)

Get a presigned URL

This endpoint fetches a presigned URL link to a browser viewable report.

### Example

* Api Key Authentication (FireEyeAPIKey):
```python
from __future__ import print_function
import time
import fireeye.detection
from fireeye.detection.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://feapi.marketplace.apps.fireeye.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fireeye.detection.Configuration(
    host = "https://feapi.marketplace.apps.fireeye.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: FireEyeAPIKey
configuration = fireeye.detection.Configuration(
    host = "https://feapi.marketplace.apps.fireeye.com",
    api_key = {
        'feye-auth-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['feye-auth-key'] = 'Bearer'

# Enter a context with an instance of the API client
with fireeye.detection.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireeye.detection.PresignedUrlApi(api_client)
    report_id = '874da611-f82a-4331-afde-5943f4facb92' # str | The report ID returned after successfully submitting a file.
expiry = 1 # int | Expiry (in hours) for browser viewable report presigned URL link. Default value is 72 hours.  Minimum is 1 hour, and maximum is 8760 hours (365 days). (optional)

    try:
        # Get a presigned URL
        api_response = api_instance.get_presigned_url(report_id, expiry=expiry)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PresignedUrlApi->get_presigned_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| The report ID returned after successfully submitting a file. | 
 **expiry** | **int**| Expiry (in hours) for browser viewable report presigned URL link. Default value is 72 hours.  Minimum is 1 hour, and maximum is 8760 hours (365 days). | [optional] 

### Return type

**object**

### Authorization

[FireEyeAPIKey](../README.md#FireEyeAPIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
