
from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'testevents2' # Must be replaced by your <storage_account_name>
    account_key = 'mKQx3t7EUZ6eF71os1qfjv3CUeTJjGbl7J1n/oxGCs3r3mcEue8Jm3Ycj22cyxMippWD0/GKwmU5GdkD/7qhFQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'testevents2' # Must be replaced by your storage_account_name
    account_key = 'mKQx3t7EUZ6eF71os1qfjv3CUeTJjGbl7J1n/oxGCs3r3mcEue8Jm3Ycj22cyxMippWD0/GKwmU5GdkD/7qhFQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None