package driveguardian.cot;

import com.azure.storage.blob.BlobClient;
import com.azure.storage.blob.BlobContainerClient;
import com.azure.storage.blob.BlobServiceClient;
import com.azure.storage.blob.BlobServiceClientBuilder;
import com.azure.storage.blob.models.BlobItem;

import java.io.File;
import java.io.IOException;

public class blob {
    public static void main(String[] args) throws IOException {
        System.out.println("Hello World!");

        // Replace the connection string with your own Azure Storage connection string
        String connectStr = "DefaultEndpointsProtocol=https;AccountName=driveguardian;AccountKey=hql9CbBUtG2o7ZNGQSn4KOyGYYahBdGXFqx2qXl+kxsPT8R9vSRjWuhAjZ7SRwATV4ePqlKqGAQ1+AStgqpsXA==;EndpointSuffix=core.windows.net";
        String containerName = "test";
        String localPath = "./data";

        // Create a BlobServiceClient object
        BlobServiceClient blobServiceClient = new BlobServiceClientBuilder().connectionString(connectStr).buildClient();

        // Get the container client
        BlobContainerClient containerClient = blobServiceClient.getBlobContainerClient(containerName);

        // Create the local directory if it doesn't exist
        File localDirectory = new File(localPath);
        localDirectory.mkdirs();

        // List blobs in the container
        for (BlobItem blobItem : containerClient.listBlobs()) {
            String blobName = blobItem.getName();
            BlobContainerClient blobContainerClient = blobServiceClient.getBlobContainerClient(containerName);
            BlobClient blobClient = blobContainerClient.getBlobClient(blobName);

            // Replace invalid characters in the blob name
            String sanitizedBlobName = blobName.replaceAll("[^a-zA-Z0-9.-]", "_");

            // Download the blob locally
            String localFileName = localPath + File.separator + sanitizedBlobName;
            blobClient.downloadToFile(localFileName);

            System.out.println("Blob downloaded: " + sanitizedBlobName);
        }

        System.out.println("All blobs downloaded successfully.");
    }
}
