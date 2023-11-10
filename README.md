[![CI-CD-AWS-ElasticBeanstalk](https://github.com/Tserewara/wedding-gallery-backend/actions/workflows/python-app.yml/badge.svg)](https://github.com/Tserewara/wedding-gallery-backend/actions/workflows/python-app.yml)

# Tserewara Wedding Gallery

An unified gallery with all friend's photos

~[Click here to see live](https://gallery.tserewara.com)~

## Create a user

To create a user, you must add name, email and a password. You also can tell if you're the bride or the groom. If this option is chosen, the user will have privileges to see all photos and approve them. If it fails, an error message is shown bellow the button.

![Image](/docs/create-user.gif "create-user")


## Log in

To log in, you must enter email and password. If it fails, an error message is shown bellow the button.

![Image](/docs/login.gif "login")

## Upload a photo, approve and comment

When a regular user logs in, only the approved photos are shown. If that user uploads a photo, it is not displayed, until the husband or wife approve it. If the husband or the wife logs in, all the photos are loaded, with a button to approve. When the two of them upload a photo, it is immediately added to the feed. Once a photo is approved, the button will disappear, and a success message will be displayed on a toast notification. Then, this photo will become visible to regular users.
Anyone can like photos and add comments to them.

![Image](/docs/upload.gif "upload")

- If a user tries to upload a picture bigger than 30MB, or a file other than `jpg`, `jpeg` or `png` a notification will be displayed.
- In order to be fast, the gallery only loads 10 photos on the home. Bellow the last photo there is a button to load ten more. The photos are sorted in order of upload, so the last uploaded is first shown.


### Infra

- The back end is hosted on an instance of Elastic Beanstalk, under the custom domain tserewara.com
- The database is on atlas
- The photos are in a AWS S3 bucket 
- The front end is being served from AWS Cloudfront under the subdomain gallery.tserewara.com

### Aditional improvements

- Unit tests for the backend use cases with pytest
- CI/CD pipeline with Github Actions
- Clean Architecture
- Solid Principles
- Conventional commits

[Click here to see the front end repo here](https://github.com/Tserewara/wedding-gallery-frontend)
