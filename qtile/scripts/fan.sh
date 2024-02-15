#!/usr/bin/env bash

sensors | grep -i fan | awk '{print "fan: " $3 " RPM"}'
