const CACHE_NAME = 'my-pwa-cache-v1-work';
const cacheUrls = [
    '/',
    '/index.html',
    '/css/welcome.css',
    '/css/signin.css',
    '/app.js',
    '/css/Logo.png',
    '/assets/image2.jpg'
    // Add other assets and resources you want to cache
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(cacheUrls).catch((error) => {
                console.error('Failed to cache some resources during installation:', error);
            });
        })
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request).then((response) => {
            return response || fetch(event.request);
        })
    );
});

self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames
                    .filter((name) => name !== CACHE_NAME)
                    .map((name) => caches.delete(name))
            );
        })
    );
});
