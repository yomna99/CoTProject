from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

# Replace with your local directory path and Azure storage details
local_path = "data/test/images"
container_name = "testimage"
connection_string = "DefaultEndpointsProtocol=https;AccountName=driveguardian;AccountKey=hql9CbBUtG2o7ZNGQSn4KOyGYYahBdGXFqx2qXl+kxsPT8R9vSRjWuhAjZ7SRwATV4ePqlKqGAQ1+AStgqpsXA==;EndpointSuffix=core.windows.net"

def upload_files_to_azure():
    try:
        # Create the BlobServiceClient using the connection string
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container_name)
        # List all files in the local directory
        local_files = [f for f in os.listdir(local_path) if os.path.isfile(os.path.join(local_path, f))]
        print(len(local_files))
        for local_file in local_files:
            local_file_path = os.path.join(local_path, local_file)
            print(local_file_path)
            # Create a blob client using the local file name as the name for the blob
            blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file)

            print(f"Uploading {local_file}...")

            # Upload the file to Azure
            with open(local_file_path, "rb") as data:
                blob_client.upload_blob(data, overwrite=True)

            print(f"{local_file} uploaded successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

upload_files_to_azure()