# element_check
Nagios "page element" check. This simple script looks for a particular page element on a given web site, throwing an 'OK' Nagios exit code if the element is found, and a "critical' exit code if the given element is not found. This helps detect broken pages that have missing elements, while they still return 200/OK HTTP status codes and expected text strings.
