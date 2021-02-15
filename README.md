# weather_texter
A script to pull tomorrow's weather and whatsapp it to me

This project pulls weather data for the following day from https://openweathermap.org/ and sends it to a specified phone number

You will need to sign up to https://openweathermap.org/ to get an API key.

I created a .bat file and used windows scheduler to execute the program every evening and text me the weather for the following day.
Output looks like this:
+--------+--------+-----------------+-----+------+
|   T    |   °C   |   description   |  c% |  ws  |
+--------+--------+-----------------+-----+------+
|   00   |   9    |       Rain      | 100 | 005  |
|   03   |   8    |      Clouds     | 100 | 005  |
|   06   |   7    |      Clouds     | 100 | 005  |
|   09   |   8    |       Rain      | 100 | 005  |
|   12   |   8    |       Rain      | 100 | 003  |
|   15   |   11   |       Rain      | 100 | 005  |
|   18   |   9    |      Clouds     | 069 | 004  |
|   21   |   8    |      Clear      | 005 | 005  |
+--------+--------+-----------------+-----+------+
