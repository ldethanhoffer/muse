# Muse
> ...your personal museum tour guide...

[![Jquery Version][npm-image]][npm-url]
[![Python][travis-image]][travis-url]
[![Downloads Stats][npm-downloads]][npm-url]

An intelligent recommendation system for paintings using image recognition



## Links



```sh
https:/museum-muse.herokuapp.com

https:/github.com/ldethanhoffer/muse

```


## Background

Museums are big business: in Canada alone they generate 2.5B $/year, employ 37.000 people and attract 54m visitors/year

However, recent studies have shown that the museum market has a alot of trouble both attracting a younger demographic
as well as building a loyal customer basis...

Enter [Muse][app-link]: a modern and intuitive way to discover and navigate museums
using state of the art AI.


## The data

To mimic a toy museum, 500 images accors 5 different artistic style were scared using 
the Google API


## The Model

To create an image recommendation system, we used transfer learning  on
the VGG-19 dataset by removing the classifying layer as well as the last
convolutional layer and simply used those pre-trained weights to obtain 
and embedding

Next, we used K-NN to obtain the closest recommendations using cosine 
similarity

## The Validation

Validating a cold start problem is typicaly quite hard, so instead we 
decided to ask [Muse][app-link] another problem: can it detect similarity
of styles. It turns out that it can with ~80% accuracy. A T-sne plot
shows how well [Muse][app-link] clusters different styles



## Release History

* 0.2.0
    * deployed as webapp using Flask on Heroku
* 0.1.0
    * deployed as php code on [louisdethanhoffer.com][personal-link]
* 0.0.1
    * Release MVP



<!-- Markdown link & img dfn's -->
[personal-link]: https://louisdethanhoffer.com
[app-link]: https://museum-muse.herokuapp.com
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
