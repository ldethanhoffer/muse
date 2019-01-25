<!--

php functionality to Demo the MVP of Muse, uploaded to louisdethanhoffer.com

with thanks to Oliver Jean Capon

-->


<?php
    // PATH TO THE ORIGINAL IMAGES
    $original_images_path = "data/raw/";
    // PATH TO THE RECOMMENDED IMAGES
    $recommended_images_path = "output/recommendations/";
    // this scans the directory and returns an array of files and folders found
    $original_images = scandir($original_images_path);
    // here I'm looping through the array to create a new array of only images
    foreach($original_images as $image_name) {
        // get the length of the file name (including extension)
        $image_name_length = strlen($image_name);
        // if the file name ends in jpg, add it to the images array
        if (substr($image_name, $image_name_length - 3) == 'jpg'){
            // this images array is used further down in the html
            $images[] = $image_name;
        }
    }
?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta http-equiv="X-UA-Compatible" content="ie=edge" />
        <title>Document</title>
         <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.2/css/bulma.min.css" />
        <style type="text/css">
             .columns {
            display: flex;
            flex-wrap: wrap;
            max-width: 11000px;
            margin: 0 auto;
            justify-content: center;

        }
        .column {
            flex-grow: 1;
            border: thin solid black;
            padding: 5px;
            max-height:20%;
            max-width: 20%;
            margin:10px;
        } 
        .p {

           padding:100px;
           margin:100px;
        }
        </style>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/voca/1.4.0/voca.min.js"></script>
    </head>
    <body>
        <div>
            <p>
            Welcome to the Moma<br><br>
            Please select a painting:<br><br>
            </p>
        </div>

        <div class="columns">
            <?php foreach($images as $image): ?>
            <div class="column is-narrow">
                <img
                    src="<?php echo $original_images_path . $image; ?>"
                    alt="<?php echo $image; ?>"
                />
            </div>
            <?php endforeach; ?>
        </div>
        <script>
            // get the original images path from php
            var old_path = "<?php echo $original_images_path; ?>";
            // get the recommened images path from php
            var new_path = "<?php echo $recommended_images_path; ?>";
            // on each image, when clicked, run the following function
            $("img").one("click", function(event) {
                // get the old image source attribute
                var old_src = $(this).attr("src");
                // using the javascript Voca plugin
                var new_src = v
                    .chain(old_src) //using the old source variable
                    .insert("_rec", old_src.length - 4) // add _rec before the extension
                    .replace(old_path, new_path) // replace old path with new
                    .replace("jpg", "png"); // replace the file extention
                $(this).attr("src", new_src); // update the image with the new source
            });
        </script>
    </body>
</html>