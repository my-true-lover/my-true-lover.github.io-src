# Hi Kristin!
## Writing a post
1. Create a file with an `.md` extension in `data/Post`.
2. Include the header from the earlier posts and fill in info for your new post.
3. Create a folder under the `assets/photos` directory holding all photos
   you want included with your post.
4. Create a file in `data/Album` with extension `.yml` listing the name of
   the folder created in step 3 and all of the pictures in it (see
   `data/Album/holy-wow-six-months.yml` as an example).
5. Add the filename for all images to `data/Image/_all.yml`
6. In the header of your post include
   "album: <filename created in step 4 without the `.yml`>"
   
## Creating standalone album
1. Copy `data/Post/post2.yml` to a new file with a `.yml` extension in
   `data/Post`.
2. Follow steps 3-6 above.

## Previewing your website.

Type `source bin/activate` and then `statik -w`. This should open your
blog to preview in your default browser. When done, type `C-c` and then
`deactivate`.

## Publishing your website

1. `statik`
2. `cd public`
3. `aws s3 sync . s3://psalm63.thebeckmeyers.xyz`
4. `cd ..`
5. `git add .`
6. `git commit -m "add post <post title>"`
7. `git push`

## Making sure your mom doesn't hound you for pictures of Job

1. Post the thing to facebook if it includes pictures of Job.

2. Tag your mom and your grandma at least.
