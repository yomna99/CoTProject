package driveguardian.cot;

import com.azure.storage.blob.BlobClient;
import com.azure.storage.blob.BlobContainerClient;
import com.azure.storage.blob.BlobServiceClient;
import com.azure.storage.blob.BlobServiceClientBuilder;
import com.azure.storage.blob.models.BlobItem;

import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.*;

public class blob {
    private static final String CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=driveguardian;AccountKey=hql9CbBUtG2o7ZNGQSn4KOyGYYahBdGXFqx2qXl+kxsPT8R9vSRjWuhAjZ7SRwATV4ePqlKqGAQ1+AStgqpsXA==;EndpointSuffix=core.windows.net";
    private static final String CONTAINER_NAME = "test";
    private static final String LOCAL_PATH = "./data";

    private final BlobServiceClient blobServiceClient;
    private final BlobContainerClient containerClient;
    private final Map<String, Boolean> processedBlobs;

    public blob() {
        this.blobServiceClient = new BlobServiceClientBuilder().connectionString(CONNECTION_STRING).buildClient();
        this.containerClient = blobServiceClient.getBlobContainerClient(CONTAINER_NAME);
        this.processedBlobs = new HashMap<>();
    }

    public void startSyncTask() {
        ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(1);

        // Run the sync task every 5 seconds (adjust as needed)
       // scheduler.scheduleAtFixedRate(this::syncBlobs, 0, 1, TimeUnit.SECONDS);
    }

    private void syncBlobs() {
        System.out.println("Checking for new blobs...");

        // Réinitialise la carte à chaque exécution
        processedBlobs.clear();

        for (BlobItem blobItem : containerClient.listBlobs()) {
            String blobName = blobItem.getName();

            if (!processedBlobs.containsKey(blobName) || !processedBlobs.get(blobName)) {
                downloadBlob(blobName);
                processedBlobs.put(blobName, true);
                System.out.println("Blob downloaded: " + blobName);
            }
        }
    }

    private void downloadBlob(String blobName) {
        BlobClient blobClient = containerClient.getBlobClient(blobName);
        String sanitizedBlobName = blobName.replaceAll("[^a-zA-Z0-9.-]", "_");
        String localFileName = LOCAL_PATH + File.separator + sanitizedBlobName;

        try {
            blobClient.downloadToFile(localFileName);
            System.out.println("Blob downloaded: " + blobName);
        } catch (Exception e) {
            e.printStackTrace();
            System.err.println("Error downloading blob: " + blobName);
        }
    }

    public static void main(String[] args) {
        blob syncService = new blob();
        syncService.startSyncTask();
    }
}
