Title: How to safely store Arduino secrets
Date: 2020-12-16 18:00
Author: Andrea Grandi
Category: Development
Tags: arduino, secrets, secret, security, password, passwords, storage, howto, safe, hide, secure
Slug: how-to-safely-store-arduino-secrets
Status: published
Summary: Best practices to store Arduino secrets safely

You just got a new Arduino board (maybe a wifi enabled one), you wrote a useful application and you are about to share it on GitHub.

If your code looks like this:

    :::arduino
    #include <WiFi101.h>

    char ssid[] = "myessid"
    char pass[] = "mypassword"
    ...

do **not** share it! You would leak your ESSID, password and maybe othere secrets to everyone.

## Store secrets in an external file

Create a separate file named `arduino_secrets.h`:

    :::arduino
    #define SECRET_SSID = "myessid"
    #define SECRET_PASS = "mypassword"

and change the main file in this way:

    :::arduino
    #include <WiFi101.h>
    #include <arduino_secrets.h>

    char ssid[] = SECRET_SSID
    char pass[] = SECRET_PASS
    ...

**Note:** using the **`SECRET_...`** naming convention is also useful if you use the **Arduino Web Editor** <https://create.arduino.cc/projecthub/Arduino_Genuino/store-your-sensitive-data-safely-when-sharing-a-sketch-e7d0f0> because these values will be automatically added to a secret tab and will only be visible to you, even if you share your project.

## Exclude secrets file from git

Moving secrets to `arduino_secrets.h` would be pointless if we pushed this file to GitHub. To avoid this mistake, add `arduino_secrets.h` to `.gitignore` (create it in the root of the project if it doesn't exist already).

## Add an example for secrets file

If you simply hide the original `arduino_secrets.h`, other users who would like to reuse your code may not know what to put inside. Create an example file named `arduino_secrets.h.example` with dummy values:

    :::arduino
    #define SECRET_SSID = "foo"
    #define SECRET_PASS = "foo"

and document that this needs to be renamed to `arduino_secrets.h`

## What if I need to build my code in a CI?

In case you want to build your code in a CI environment, the full source code needs to be there, but at the same time you still don't want to push your secrets to GitHub. What to do then?

### Store your secrets in environment variables

Create an environment variable in your CI (or set it locally on your machine if you want to build it locally) for each secret:

    :::shell
    export WIFI_SSID_NAME="myessid"
    export WIFI_PASSWORD="mypassword"

### Create a Makefile

Add a `Makefile` to your project, similar to this one:

    :::bash
    #!/bin/bash

    OUTPUT = "arduino_secrets.h"

    arduino_secrets:
        @echo "Generating $(OUTPUT)"
        @[ -e $(OUTPUT) ] && rm $(OUTPUT)
        @echo "#define SECRET_SSID \"$(WIFI_SSID_NAME)\"" >> $(OUTPUT)
        @echo "#define SECRET_PASS \"$(WIFI_PASSWORD)\"" >> $(OUTPUT)

If you run `make` you will generate a file named `arduino_secrets.h` containing the proper values.

## Conclusion

There may be alternative methods to safely store secrets. If you know a better one, you can leave a comment below.

## References

- <https://create.arduino.cc/projecthub/Arduino_Genuino/store-your-sensitive-data-safely-when-sharing-a-sketch-e7d0f0>
