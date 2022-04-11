# CS4383-Quiz8
 
In this quiz, we were tasked to build a simple page in HTML and JavaScript that implements a simple cacluator through a Google Cloud Functions.

## Description of Solution

`calc.html` implements a frontend that takes two values from the user. The values are passed to a Google Cloud Function as query parameters described in `calc_function.py` that performs basic arithmetic on the values, then returns the result back to the frontend to display.

In the same frontend, the resulting value can be sent to a Google Cloud Function that publishes it to a topic in Google Pub/Sub called `food-order-topic`, to be retrieved by the subscriber `doordash-sub`.

## Google Cloud Function Configuration
The two Cloud Functions are implemented in Flask. `do_op` in `calc_functions.py` will take three values via query parameters: `operation` (`add`, `sub`, `mul`, `div`) and two values (denoted by `data1` and `data2`). The lack of any one of these parameters present results in the string "No operation!" returning, and if the second value is a zero, it will return "Div by Zero!"

example: `https://{CloudFunctionURL}?operation=add&data1=2&data2=3` will return 4

`pubsub.py` describes a function that takes a message and passes it to a topic Google Pub/Sub via POST request, with the message as a JSON in the request body.

Due to security policies required by both the server and client, there were two specific configurations that had to be made in order for the Cloud Function to be reachable. On the server-side, permissions were set on both Cloud Functions to give users invoking the function access through their browser (which in real world probably isn't the best practice).

Additionally, Cross-Origin Resource Sharing (CORS) had to be present in the response headers to allow cross-origin sharing. Otherwise the function call which resides outside the domain where the calculator frontend was served would be rejected.
