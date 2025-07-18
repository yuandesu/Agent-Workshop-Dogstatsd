from datadog import initialize, statsd
import time
import random

options = {}

initialize(**options)

while True:

  temperature = round(random.uniform(20,33),2)
  humidity = round(random.uniform(30,35),2)
  pressure = round(random.uniform(800,1000),2)
 
  #Count
  statsd.increment('temperature.count.increment', temperature, tags=["environment:dev", "unit:celsius"])
  statsd.decrement('temperature.count.decrement', temperature, tags=["environment:dev"])  
  statsd.increment('humidity.count.increment', humidity, tags=["environment:dev"])
  statsd.decrement('humidity.count.decrement', humidity, tags=["environment:dev"])  
  statsd.increment('pressuse.count.increment', pressure, tags=["environment:dev"])
  statsd.decrement('pressure.count.decrement', pressure, tags=["environment:dev"]) 
 
  #Gauge
  statsd.gauge('temperature.gauge', temperature,tags=["environment:dev"])
  statsd.gauge('humidity.gauge',humidity, tags=["environment:dev"])
  statsd.gauge('pressure.gauge',pressure, tags=["environment:dev"])
 
  #Histogram (.avg, .median, .count, .max, .95percentile)
  statsd.histogram('temperature.histogram', temperature, tags=["environment:dev"])
  statsd.histogram('humidity.histogram', humidity, tags=["environment:dev"])
  statsd.histogram('pressure.histogram', pressure, tags=["environment:dev"])
  
  #Distribution (avg, count, max, min)
  statsd.distribution('temperature.distribution', temperature, tags=["environment:dev"])
  statsd.distribution('humidity.distribution', humidity, tags=["environment:dev"])
  statsd.distribution('pressure.distribution', pressure, tags=["environment:dev"])


  time.sleep(10)
