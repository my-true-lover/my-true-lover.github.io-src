# Hi Kristin!  ## Writing a post 1. Create a file titled page<num>.md in the content folder.  2. Include the header from the earlier posts and fill in info for your new post.  3. Create a folder (photoFoldername) under the content/photos directory holding all photos you want included with your post.  4. In the header of your post include "gallery: photoFolderName" 5. Put all your photos in the folder Yay! You did it.  ## Previewing your website.  When in the root directory of your blog type "pelican".  This will generate a local version of the website in the output folder. Type "icecat output/index.html" to view the root of your website in icecat. Click around to make sure that everything looks good.  When you're ready to publish your website: ## Publishing your website

1. "make publish"

2. "cd output"

3. "aws s3 sync . s3://psalm63.thebeckmeyers.xyz"

4. "cd .."

5. "git add ."

6. "git commit -m "add post <post title>""

7. "git push"

## Making sure your mom doesn't hound you for pictures of Job

1. Post the thing to facebook if it includes pictures of Job.

2. Tag your mom and your grandma at least.
