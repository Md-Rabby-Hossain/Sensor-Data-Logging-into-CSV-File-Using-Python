#include "DHT.h"

#define DHTPIN 5
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup()
{
  Serial.begin(115200);
  dht.begin();
}

void loop()
{
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Error");
    return;
  }

  Serial.print(temperature, 2);  // send two decimal places
  Serial.print(",");
  Serial.print(humidity, 2);
  Serial.println();

  delay(2000);
}
