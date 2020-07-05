1. Upload photo.
2. News feed.
3. Follow people.
4. Like/Comment photo.
5. Caching.
6. CDN
7. Hashtags.
8. Notifications.
9. Messaging.


# Tables:

Photos in S3.

##Photo table:
```
Photo ID | Owner | Path
```

##Likes table:
```
Photo ID | Liked by
```

##Like_count table:
```
Photo ID | Num Likes
```

##Comment table:
```
Photo Id | Commented by | Content
```

##Follower table:
```
Follower ID | Followed ID
```


- Client will hit the gateway first.
- Images can also be served from CDN.


# Image service

## Input from user to upload image
- Inserts into db and S3.
- Sends to News feed service.

## Input from News Feed service to fetch images.
- Serves the images from S3.
- Note that we should probably separate out image service into an image-read and an image-write service since the number of reads are much higher than writes.

# News feed service

## Input from Image service containing a image.
- Maintains a priority queue for each user which contains the top N images for news feed.
- Acts like a fanout service in which the photo is inserted into the priority queue of every follower.
- The priority queue can be ranked by the number of likes and comments for example.
- But wait, if the priority queue is size-limited, then how will we rerank when the number of likes and comments change.
- Its better that we store all the image ids in the priority queue.

## Input from user to get the news feed.
- Returns the top 100 photos from the priority queue.
- Will maintain a cache of the top 100 photos.

## Input from Like and Comment service to update data.
- Updates the priority queue.

# User graph service

## Input from user to follow some other user.
- Update the database.
- Sends this to the news feed service.

# Notifications
- Rather than following a push or pull strategy, we can do a hybrid approach.
- If a celebrity publishes a image, it will take a long time to push all images.
- So for a celebrity, it will be pull based.
- But in general, it can be push.

# CDN
- We will CDN for every country.
- If an Indian publishes an image, it will be pushed to the CDN as well.