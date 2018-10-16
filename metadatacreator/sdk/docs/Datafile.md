# Datafile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Relative path of the file within the dataset folder | 
**size** | **float** | Uncompressed file size in bytes | [optional] 
**time** | **datetime** | Time of file creation on disk, format according to chapter 5.6 internet date/time format in RFC 3339. Local times without timezone/offset info are automatically transformed to UTC using the timezone of the API server | [optional] 
**chk** | **str** | Checksum for the file, e.g. its sha-2 hashstring | [optional] 
**uid** | **str** | optional: user ID name as seen on filesystem | [optional] 
**gid** | **str** | optional: group ID name as seen on filesystem | [optional] 
**perm** | **str** | optional: Posix permission bits | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


