import ee 

# Composite an image collection and clip it to a boundary.

# Load Landsat 7 raw imagery and filter it to April-July 2000.
collection = ee.ImageCollection('LANDSAT/LE07/C01/T1') \
    .filterDate('2000-04-01', '2000-07-01')

# Reduce the collection by taking the median.
median = collection.median()

# Load a table of state boundaries and filter.
fc = ee.FeatureCollection('TIGER/2016/States') \
    .filter(ee.Filter.Or(
        ee.Filter.eq('NAME', 'Nevada'),
        ee.Filter.eq('NAME', 'Arizona')))

# Clip to the output image to the Nevada and Arizona state boundaries.
clipped = median.clipToCollection(fc)

# Display the result.
m.setCenter(-110, 40, 5)
visParams = {'bands': ['B3',  'B2',  'B1'], 'gain': [1.4, 1.4, 1.1]}
m.addLayer(clipped, visParams, 'clipped composite')
m