# CDN (Content Delivery Network)

## Pull CDN

- Imagine a person loading your latest travel blog post.
- It probably has pictures in it, as does your site’s theme (e.g. icons, background images, etc.).
- For this example let’s have your hosting server be in Boston.
- You’ve just published your latest travel blog post and your biggest fan in Japan wants to read it.
- With a pull CDN, the very first time she does, the content isn’t on the CDN. During this first request, the CDN “pulls” the images and so forth to CDN server nearest your Japanese fan.
- That could be Tokyo or Hong Kong, whichever it is, the very first time the CDN has to pull the post, meaning your server and reader won’t see any gain in speed.
- The second time however (and usually for 1-30 days later) the CDN has the content loaded and it’s will be available to everyone who is closest to that Tokyo or Hong Kong CDN server.

## Push CDN

- Going along with the example above, instead of waiting around for the CDN to pull the content when it’s needed, you simply upload the entire content of your travel blog to the CDN beforehand.
- That way your pictures, theme files, videos, and the rest are always on the CDN servers around the world.

## How does the client know which CDN POP to connect to?

- Using Domain Name Resolution.
- The CDN has setup its own nameservers.
- During the DNS resolution sequence, those nameservers will be queried at the end.
- Those nameservers will then respond with the appropriate POP IP address based on various factors like geographic proximity, load etc.
- Geo proximity etc can be computed since the client's IP address is passed along the request.
- For more details, ask Aman.