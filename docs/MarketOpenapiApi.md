# openapi_client.MarketOpenapiApi

All URIs are relative to *http://127.0.0.1:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app**](MarketOpenapiApi.md#create_app) | **POST** /app-server/openapi/apps | create an app model
[**create_app_version**](MarketOpenapiApi.md#create_app_version) | **POST** /app-server/openapi/apps/{appID}/versions | post an app version
[**get_app_hub_info**](MarketOpenapiApi.md#get_app_hub_info) | **GET** /app-server/openapi/apps/{appID}/apphubinfo | get app image save info
[**get_market_info**](MarketOpenapiApi.md#get_market_info) | **GET** /app-server/openapi/info | get mrket info
[**get_user_app_detail**](MarketOpenapiApi.md#get_user_app_detail) | **GET** /app-server/openapi/apps/{appID} | Query the specified application details
[**get_user_app_list**](MarketOpenapiApi.md#get_user_app_list) | **GET** /app-server/openapi/apps | A list of installable applications
[**get_user_app_version_detail**](MarketOpenapiApi.md#get_user_app_version_detail) | **GET** /app-server/openapi/apps/{appID}/versions/{version} | Query the specified version details of the specified application
[**get_user_app_versions**](MarketOpenapiApi.md#get_user_app_versions) | **GET** /app-server/openapi/apps/{appID}/versions | Query the specified application version list
[**update_app**](MarketOpenapiApi.md#update_app) | **PUT** /app-server/openapi/apps/{appID} | update app model base info


# **create_app**
> V1AppDetailInfoResponse create_app(body, market_domain=market_domain)

create an app model

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    body = openapi_client.V1AppCreateRequest() # V1AppCreateRequest | 
market_domain = 'market_domain_example' # str | the market domain (optional)

    try:
        # create an app model
        api_response = api_instance.create_app(body, market_domain=market_domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->create_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1AppCreateRequest**](V1AppCreateRequest.md)|  | 
 **market_domain** | **str**| the market domain | [optional] 

### Return type

[**V1AppDetailInfoResponse**](V1AppDetailInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Field validation |  -  |
**403** | No perm |  -  |
**404** | No found |  -  |
**500** | server failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_app_version**
> V1AppVersionBase create_app_version(app_id, body, market_domain=market_domain)

post an app version

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    app_id = 'app_id_example' # str | The app ID
body = openapi_client.V1CreateAppPaaSVersionRequest() # V1CreateAppPaaSVersionRequest | 
market_domain = 'market_domain_example' # str | the market domain (optional)

    try:
        # post an app version
        api_response = api_instance.create_app_version(app_id, body, market_domain=market_domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->create_app_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID | 
 **body** | [**V1CreateAppPaaSVersionRequest**](V1CreateAppPaaSVersionRequest.md)|  | 
 **market_domain** | **str**| the market domain | [optional] 

### Return type

[**V1AppVersionBase**](V1AppVersionBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | No perm |  -  |
**404** | No found |  -  |
**500** | server failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_hub_info**
> V1AppImageHubInfoResponse get_app_hub_info(app_id, market_domain=market_domain)

get app image save info

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    app_id = 'app_id_example' # str | The app ID
market_domain = 'market_domain_example' # str | the market domain (optional)

    try:
        # get app image save info
        api_response = api_instance.get_app_hub_info(app_id, market_domain=market_domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->get_app_hub_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID | 
 **market_domain** | **str**| the market domain | [optional] 

### Return type

[**V1AppImageHubInfoResponse**](V1AppImageHubInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | No perm |  -  |
**404** | No found |  -  |
**500** | server failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_market_info**
> V1MarketInfoResponse get_market_info(market_domain=market_domain)

get mrket info

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    market_domain = 'market_domain_example' # str | the market domain (optional)

    try:
        # get mrket info
        api_response = api_instance.get_market_info(market_domain=market_domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->get_market_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market_domain** | **str**| the market domain | [optional] 

### Return type

[**V1MarketInfoResponse**](V1MarketInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | No perm |  -  |
**500** | server failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_app_detail**
> V1AppDetailInfoResponse get_user_app_detail(app_id, market_domain)

Query the specified application details

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    app_id = 'app_id_example' # str | The app ID
market_domain = 'market_domain_example' # str | the market domain

    try:
        # Query the specified application details
        api_response = api_instance.get_user_app_detail(app_id, market_domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->get_user_app_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID | 
 **market_domain** | **str**| the market domain | 

### Return type

[**V1AppDetailInfoResponse**](V1AppDetailInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | No perm |  -  |
**404** | No found |  -  |
**500** | server failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_app_list**
> V1UserAppListResponse get_user_app_list(market_domain, query=query, query_all=query_all, page=page, page_size=page_size)

A list of installable applications

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    market_domain = 'market_domain_example' # str | the market domain
query = 'query_example' # str | The search criteria (optional)
query_all = True # bool | true (optional)
page = 56 # int | query page num (optional)
page_size = 56 # int | query page size, if -1 return all app (optional)

    try:
        # A list of installable applications
        api_response = api_instance.get_user_app_list(market_domain, query=query, query_all=query_all, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->get_user_app_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market_domain** | **str**| the market domain | 
 **query** | **str**| The search criteria | [optional] 
 **query_all** | **bool**| true | [optional] 
 **page** | **int**| query page num | [optional] 
 **page_size** | **int**| query page size, if -1 return all app | [optional] 

### Return type

[**V1UserAppListResponse**](V1UserAppListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | market not found |  -  |
**500** | server failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_app_version_detail**
> V1AppVersionDetailResponse get_user_app_version_detail(app_id, version, market_domain=market_domain, for_install=for_install, get_template=get_template)

Query the specified version details of the specified application

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    app_id = 'app_id_example' # str | The app ID
version = 'version_example' # str | The app version
market_domain = 'market_domain_example' # str | the market domain (optional)
for_install = True # bool | Whether used for installation (optional)
get_template = True # bool | Whether get templete (optional)

    try:
        # Query the specified version details of the specified application
        api_response = api_instance.get_user_app_version_detail(app_id, version, market_domain=market_domain, for_install=for_install, get_template=get_template)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->get_user_app_version_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID | 
 **version** | **str**| The app version | 
 **market_domain** | **str**| the market domain | [optional] 
 **for_install** | **bool**| Whether used for installation | [optional] 
 **get_template** | **bool**| Whether get templete | [optional] 

### Return type

[**V1AppVersionDetailResponse**](V1AppVersionDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | No perm |  -  |
**404** | No found |  -  |
**500** | server failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_app_versions**
> V1AppVersionListResponse get_user_app_versions(app_id, query_all, market_domain)

Query the specified application version list

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    app_id = 'app_id_example' # str | The app ID
query_all = True # bool | query all versions, must have write perm
market_domain = 'market_domain_example' # str | the market domain

    try:
        # Query the specified application version list
        api_response = api_instance.get_user_app_versions(app_id, query_all, market_domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->get_user_app_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID | 
 **query_all** | **bool**| query all versions, must have write perm | 
 **market_domain** | **str**| the market domain | 

### Return type

[**V1AppVersionListResponse**](V1AppVersionListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | No perm |  -  |
**404** | No found |  -  |
**500** | server failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app**
> V1AppDetailInfoResponse update_app(app_id, body, market_domain=market_domain)

update app model base info

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarketOpenapiApi(api_client)
    app_id = 'app_id_example' # str | The app ID
body = openapi_client.V1AppUpdateRequest() # V1AppUpdateRequest | 
market_domain = 'market_domain_example' # str | the market domain (optional)

    try:
        # update app model base info
        api_response = api_instance.update_app(app_id, body, market_domain=market_domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarketOpenapiApi->update_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| The app ID | 
 **body** | [**V1AppUpdateRequest**](V1AppUpdateRequest.md)|  | 
 **market_domain** | **str**| the market domain | [optional] 

### Return type

[**V1AppDetailInfoResponse**](V1AppDetailInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | No perm |  -  |
**404** | No found |  -  |
**500** | server failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
