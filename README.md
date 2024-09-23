# ISS Overhead Notifier

This Python project tracks the position of the International Space Station (ISS) and notifies you via email when it's overhead in your location and when it's nighttime, so you can look up and potentially see it in the sky! 🌌

## Features

- Fetches the current location of the ISS using the [Open Notify ISS API](http://open-notify.org/Open-Notify-API/ISS-Location-Now/).
- Uses the [Sunrise-Sunset API](https://sunrise-sunset.org/api) to determine whether it's nighttime at your location.
- Sends an email notification if the ISS is overhead and it's nighttime.
- The program runs continuously, checking the ISS position every 60 seconds.

## How It Works

1. **ISS Location Check**: The program uses the ISS API to fetch the current latitude and longitude of the ISS. If the ISS is within 5 degrees of your location (both latitude and longitude), it's considered "overhead."
   
2. **Nighttime Check**: The program checks whether it is currently night at your location by fetching the sunrise and sunset times from the Sunrise-Sunset API. If the current time is after sunset or before sunrise, it is considered nighttime.

3. **Email Notification**: If both the ISS is overhead and it is nighttime, the program sends you an email notifying you to look up in the sky.

## Setup



 **Edit the script**:
    - Open the `main.py` file and replace the following placeholders:
      - `MY_EMAIL`: Your email address.
      - `MY_PASSWORD`: Your email password or app-specific password (if using Gmail with 2-factor authentication).
      - `MY_LAT`: Your latitude.
      - `MY_LNG`: Your longitude.



