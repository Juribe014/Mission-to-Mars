# Mission-to-Mars

# Summary 

Used BeautifulSoup and Splinter to scrape full-resolution images of Mars’s hemispheres and the titles of those images.

``` python
[{'img_url': 'https://marshemispheres.com/images/full.jpg',
  'title': 'Cerberus Hemisphere Enhanced'},
 {'img_url': 'https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg',
  'title': 'Schiaparelli Hemisphere Enhanced'},
 {'img_url': 'https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg',
  'title': 'Syrtis Major Hemisphere Enhanced'},
 {'img_url': 'https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg',
  'title': 'Valles Marineris Hemisphere Enhanced'}]
```

Stored the scraped data on a Mongo database, use a web application to display the data. THe image below shows the initial output off the app being initiated. To obtain the data, one must press the "Scrape New Data" button to begin scraping the appropiate images. 

![Scrape_image](https://user-images.githubusercontent.com/104809098/188524036-a51d3f38-cf65-4e91-a097-50679ac2801b.png)
