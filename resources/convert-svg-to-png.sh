#!/bin/bash

source_folder=$1
target_folder=$2

# Check if the target folder exists
if [ ! -d "$target_folder" ]; then
  # Create the target folder
  mkdir "$target_folder"
fi

# Loop through all files in the current directory
for file in $source_folder/*.svg; do
  # Convert the SVG file to PNG
  BASE=$(basename -s .svg $file)  
  svgexport "$file" "$target_folder/$BASE.png"
done

echo "FINISHED"
exit 0

